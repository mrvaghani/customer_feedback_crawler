# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json
# Instantiates a client
client = language.LanguageServiceClient()

def NLPGaugeSentiment(review_obj):
    list = []
    text = review_obj['review_description']
    review_loc = review_obj['reviewer_location']
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # Detects the entity sentiment of the text
    response = client.analyze_entity_sentiment(document=document, encoding_type='UTF8')
#    return response
    entities = response.entities

    for i in range(0,len(entities)):
        return_data = {}
        # print('name:  {}'.format(entities[i].name))
        # print('score:  {}'.format(entities[i].sentiment.score))
        return_data['name'] = entities[i].name
        return_data['sentiment_score'] = entities[i].sentiment.score
        return_data['sentiment_magnitude'] = entities[i].sentiment.magnitude
        return_data['reviewer_location'] = review_loc
        # list.append([entities[i].name, entities[i].sentiment.score, entities[i].sentiment.magnitude])
        list.append(return_data)
    return (list)

processed_list = []
with open('reviews.json') as json_file:
    review_list = json.load(json_file)
    for review in review_list:
        processed_list.extend(NLPGaugeSentiment(review))
print(json.dumps(processed_list))

##print(processed_list)
