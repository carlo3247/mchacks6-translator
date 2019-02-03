import re

translatorList = {
                'arabic': 'ar',
                'chinese': 'zh',
                'czech': 'cs', 
                'danish': 'da', 
                'dutch': 'nl',
                'finnish': 'fi', 
                'french': 'fr', 
                'german': 'de', 
                'hindi': 'hi', 
                'italian': 'it', 
                'japanese': 'ja', 
                'korean': 'ko', 
                'norwegian': 'nb', 
                'polish': 'pl', 
                'portuguese': 'pt',
                'russian': 'ru',
                'spanish': 'es',
                'swedish': 'sv',
                'turkish': 'tr'
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
