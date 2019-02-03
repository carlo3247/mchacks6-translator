import json
from watson_developer_cloud import LanguageTranslatorV3

with open('credentials/watsonkeys') as keyFile:
    watson_key = keyFile.readline().rstrip()
    watson_url = keyFile.readline().rstrip()

language_translator = LanguageTranslatorV3(
            version='2018-05-01',
                iam_apikey=watson_key,
                    url=watson_url)

translation = language_translator.translate(
            text='it is going lyrics',
                model_id='en-fr').get_result()

print(json.dumps(translation, indent=2, ensure_ascii=False))
