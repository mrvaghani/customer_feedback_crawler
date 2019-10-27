import scrapy
from scrapy.selector import Selector
import datetime
from datetime import date, timezone
import time
import pytz


class QuotesSpider(scrapy.Spider):
    name = 'reviews'
    start_urls = [
        'https://www.consumeraffairs.com/travel/jetblue.html',
    ]

    def parse(self, response):
        detailed_review_object_list = []
        review_selector_list = response.xpath('//div[@id="reviews-container"]//div[@class="js-paginator-data"]').xpath('//div[@class="rvw js-rvw"]')
        for _review_selector in review_selector_list:
            _current_review_selector_body = _review_selector.get()
            # _review_rating = _review_selector.xpath('//div[@class="rvw__hdr-stat"]//img/@data-rating').get()  # '5.0'
            _review_rating = Selector(text=_current_review_selector_body).xpath(
                '//div[@class="rvw__hdr-stat"]//img/@data-rating').get()

            # _author_info = _review_selector.xpath('//div[@class="rvw-aut__inf"]/strong/text()').get()  # 'Julie of Ceres,, CA'
            _author_info = Selector(text=_current_review_selector_body).xpath(
                '//div[@class="rvw-aut__inf"]/strong/text()').get()

            _author_state: str = _author_info.split(',')[-1]  # 'CA'

            # _review_date_text = _review_selector.xpath('//div[@class="rvw-bd ca-txt-bd-2"]/span/text()').get()  #'Original review: March 18, 2019'
            _review_date_text = Selector(text=_current_review_selector_body).xpath(
                '//div[@class="rvw-bd ca-txt-bd-2"]/span/text()').get().split(':')[-1]

            # Let's remove whitespace to make it easier to convert to datetime object
            _review_date_text = _review_date_text.replace(' ', '')
            # _review_date_text = 'March18,2019'
            _review_date_text = _review_date_text[-4:]
            # _date_pattern = '%b.%d,%Y'  # 'Oct.21,2019'
            _date_pattern = '%Y'  # '2019'
            _struct_time_format = (time.strptime(_review_date_text, _date_pattern))
            _date_time_format = datetime.datetime(*_struct_time_format[:6])
            eastern = pytz.timezone('US/Eastern')
            utc = pytz.utc
            aware_date_time = eastern.localize(_date_time_format)
            utc_review_date_time = aware_date_time.astimezone(utc).timestamp()

            # This will be the list of all paragraphs that we find in a review that we will be using to process.
            _review_description_paragraph_list: list = Selector(text=_current_review_selector_body).xpath('//div[@class="rvw-bd ca-txt-bd-2"]/p').getall()
            _clean_review_description_list: list = []

            # Let's check if there is a collapsed div that we need to process.
            if Selector(text=_current_review_selector_body).xpath('//div[@class="rvw-bd ca-txt-bd-2"]/div[@class="js-collapsed"]').get() is not None:

                # We need to get all the paragraphs in the collapsed div that we found
                _collapsed_paragraph_list = Selector(text=_current_review_selector_body).xpath('//div[@class="rvw-bd ca-txt-bd-2"]/div[@class="js-collapsed"]/p').getall()

                # Let's add these new paragraphs to our original list for processing
                _review_description_paragraph_list.extend(_collapsed_paragraph_list)

            for para in _review_description_paragraph_list:
                if Selector(text=para).xpath('//p/text()').get() is not None:  # If the paragraph is not empty
                    _clean_review_description_list.append(Selector(text=para).xpath('//p/text()').get())

            _clean_review_description = ''.join(_clean_review_description_list)
            _num_found_useful_text: str = Selector(text=_current_review_selector_body).xpath('//div[@class="rvw-foot"]/span[@class="rvw-foot__helpful-count js-helpful-count ca-txt--clr-gray"]/strong/text()').get()

            # We need to extract the number from the text we get from _num_found_useful_text --> E.g. '97 people'
            _num_found_useful: str = _num_found_useful_text.split(' ')[0]

            detailed_review_object = {
                'ratings': _review_rating,
                'reviewer_location': _author_state,
                'review_time_utc': str(utc_review_date_time),
                'review_description': _clean_review_description,
                'num_found_useful': _num_found_useful
            }
            detailed_review_object_list.append(detailed_review_object)
        _return_data = {
            'reviews': detailed_review_object_list
        }
        return _return_data

        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)

