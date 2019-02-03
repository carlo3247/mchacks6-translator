import json
from watson_developer_cloud import LanguageTranslatorV3

model_dict = {
        ('en', 'es'): 'en-es',
        }

with open('credentials/watsonkeys') as keyFile:
    watson_key = keyFile.readline().rstrip()
    watson_url = keyFile.readline().rstrip()

language_translator = LanguageTranslatorV3(
            version='2018-05-01',
                iam_apikey=watson_key,
                    url=watson_url)

def get_model_code(from_lang, to_lang):
        return from_lang[0:2] + '-' + to_lang[0:2]

def translate(text, from_lang, to_lang):
    model_code = get_model_code(from_lang, to_lang)
    translation = language_translator.translate(text=text, model_id=model_code).get_result()

    results = translation['translations']
    if len(results) > 0:
        return results[0]['translation']
    else:
        return ''
