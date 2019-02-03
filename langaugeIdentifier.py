import re
def findLang(inputString):
    inputString = inputString.lower();
    listOfWords= re.split('\W+', inputString)
    #print(listOfWords)

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
        for key in translatorList:
            if(key == listOfWords[x]):
                result = translatorList[key]
                print(result)
                flag = 1
        if(flag == 1):
            break 
    
    return result

def main():
    findLang('Hello I am english, please translate this to russian not korean')
    
if __name__ == '__main__':
    main()
