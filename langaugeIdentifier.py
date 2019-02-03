import re

translatorList = {
                'chinese': 'zh-HK',
                'danish': 'da-DK', 
                'dutch': 'nl-NL',
                'finnish': 'fi-FI', 
                'french': 'fr-CA', 
                'german': 'de-DE', 
                'italian': 'it-IT', 
                'japanese': 'ja-JP', 
                'korean': 'ko-KR', 
                'norwegian': 'nb-NO', 
                'polish': 'pl-PL', 
                'portuguese': 'pt-PT',
                'russian': 'ru-RU',
                'spanish': 'es-ES',
                'swedish': 'sv-SE',
                }

def findLang(inputString):
    listOfWords= re.split('\W+', inputString.lower())
    for word in re.split('\W+', inputString.lower()):
        if word in translatorList:
            return translatorList.get(word)
    return ''

def main():
    print(findLang('Hello I am english, please translate this to russian not korean'))
    
if __name__ == '__main__':
    main()
