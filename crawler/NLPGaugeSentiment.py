# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

def NLPGaugeSentiment(text):
    list = []
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # Detects the entity sentiment of the text
    response = client.analyze_entity_sentiment(document=document, encoding_type='UTF8')
    return response
#    entities = response.entities
#    for i in range(0,len(entities)):
#        print('name:  {}'.format(entities[i].name))
#        print('score:  {}'.format(entities[i].sentiment.score))
#        list.append([entities[i].name, entities[i].sentiment.score, entities[i].sentiment.magnitude])
#    return list

list = NLPGaugeSentiment('you just brought piss to a shit fight')
print(list)
