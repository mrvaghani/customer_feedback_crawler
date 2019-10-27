

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)


# Customer Feedback Python Crawler
Crawl public domain and social media data to get customers's' sentiments of JetBlue using Google API for natural language processing. Display this information using Javascript visualization tools.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

* Make sure you have Python 3.7 or higher
* Git


### Installing

A step by step series of examples that tell you how to get a development env running

Clone the  repo from Git

```
git clone https://github.com/mrvaghani/customer_feedback_crawler.git
cd customer_feedback_crawler
```

Activate Virtual Environment

Windows:


```markdown
env\Scripts\activate
```

Unix

```markdown
source venv/bin/activate
```

Install requirements:

```markdown
pip install -r requirements.txt
```

Run the application:

```markdown
scrapy runspider app.py -o reviews.json
```

This will create a file `reviews.json` in the same direction as the script

```json
[
  {
    "reviews": [
      {
        "ratings": "5.0",
        "reviewer_location": " CA",
        "review_time_utc": "1546318800.0",
        "review_description": "I love the service. A very tall male flight attendant took a lot of time teaching me how to use the computerized TV and making my seat more comfortable, all the while squatting down to my level to be heard. He also admired my hat when I boarded and politely ask if he could stow it up front so as not to get it crushed in flight. At end of flight he was waiting with a smile, hat in hand and gently placed it on my head. Also, their bathrooms are always very clean.",
        "num_found_useful": "7"
      },
      {
        "ratings": "5.0",
        "reviewer_location": " MA",
        "review_time_utc": "1546318800.0",
        "review_description": "Have used JetBlue for last 17 years. Prices and rewards are good. Flights have had a great on time record and planes are comfortable and clean. Staff has been professional and helpful. Services including TV and snacks add to pleasant flights.",
        "num_found_useful": "5"
      },
      {
        "ratings": "5.0",
        "reviewer_location": " Georgia",
        "review_time_utc": "1546318800.0",
        "review_description": "The skyscapes and ticket agents are very knowledgeable. The assistance to check keep the passenger alert, saving the anxiety of missing the flights. I enjoy the effort of the airline to store food on the plane to keep the children quiet and calm anytime on the airplane, to help for delays with landing.",
        "num_found_useful": "5"
      },
      {
        "ratings": "1.0",
        "reviewer_location": " NY",
        "review_time_utc": "1546318800.0",
        "review_description": "This review base on customer service. On our flight from NY to San Diego the service was good but on our flight back the services were terrible. When we took off and everything was settle seatbelt sign is still on. I understand that but I have to go to restroom and I decided to be nice and throws out my own garbage. So when I went towards the back ask where the trash can is the guy \"William\" looks at me like I kill his family or something and took my coffee cup out of my hand and throws it out without saying a word and then make an announcement while I was standing next to him stating \"do not get up while seatbelt sign is still on.\" I'm like wtf really??? I'm going to restroom throws out my ** trash to be nice. And there's this lady. Idk her name but the way she talks is so sarcastic like wtf.",
        "num_found_useful": "3"
      }
    ]
  }
]
```

## Running the tests

We scraped all the recent reviews off the Consumer Affairs website to start. Using that data, we were able to gain 4 features for every review: star rating, state location, time, and description. We processed the description using entity sentiment analysis and then correlated that analysis to every state. In our intial tests we do not discriminate among the entities found with in the review, and instead analyze all entities and then normalized the aggregate scores. At first this may seem like a naive approach, we recognize that the feeling a customer may have can color the whole review, inclusive of all objects. Therefore while analyzing all entities allows us to capture this.

## Deployment

TBD

## Built With

* [Scrapy](https://scrapy.org/doc/) - The web framework used
* [Google Cloud Language Processing API] - Machine learning function-as-a-service

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* Mehul Vaghani
* Lee Zhang
* Christian

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

TBD

## TODO
TBD
