import re
def findLang(inputString):
    inputString = inputString.lower();
    listOfWords= re.split('\W+', inputString)
    print(listOfWords)
    languageList = ['arabic', 
                'catalan', 
                'chinese', 
                'czech', 
                'danish', 
                'dutch',
                'finnish', 
                'french', 
                'german', 
                'hindi', 
                'hungarian', 
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
    flag = 0
    for x in range(0, len(listOfWords)):
        for y in range(0, len(languageList)):
            if(languageList[y] == listOfWords[x]):
                print('This is ' + languageList[y])
                flag = 1
        if(flag == 1):
            break 
       
def main():
    findLang('english Arabic chinese bruh dude wow arabic woah crazy ')
    
if __name__ == '__main__':
    main()
    