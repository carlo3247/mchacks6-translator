import re
def findLang(inputString):
    inputString = inputString.lower();
    listOfWords= re.split('\W+', inputString)
    #print(listOfWords)
    languageList = ['arabic', 
                'chinese', 
                'czech', 
                'danish', 
                'dutch',
                'finnish', 
                'french', 
                'german', 
                'hindi', 
                'italian', 
                'japanese', 
                'korean', 
                'norwegian', 
                'polish', 
                'portuguese',
                'russian',
                'spanish',
                'swedish',
                'turkish']
       
    translatorList = {'arabic': 'ar',
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
                    'turkish': 'tr'}
    flag = 0
    result = ''
    for x in range(0, len(listOfWords)):
        for y in range(0, len(languageList)):
            if(languageList[y] == listOfWords[x]):
                result = translatorList[languageList[y]]
                #print('This is ' + languageList[y])
                #print('It corresponds to ' + result)
                flag = 1
        if(flag == 1):
            break 
    
    return result

def main():
    findLang('hello I am russian, not french')
    
if __name__ == '__main__':
    main()
    
