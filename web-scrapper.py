import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

word = str(sys.argv[1])

def inflection(param):

    urlsDict = {
        "mainUrl": "https://wsjp.pl/szukaj/podstawowe/wyniki?szukaj={}",
        "printUrl": "https://wsjp.pl/haslo/do_druku/{}/{}"
    }
    options = FirefoxOptions()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    try:
        browser.get(urlsDict["mainUrl"].format(param))
        wordFromList = browser.find_element(
            "link text", param).get_attribute("href").split("/")
        browser.get(urlsDict["printUrl"].format(wordFromList[5], param))
        inflectedForms = browser.find_element(
            "css selector", ".expand_fleksja")
        array = inflectedForms.text.split()
        browser.close()
        returnArray = []
        if len(param)>4:
            halfParamLen = int(len(param)/2)
        else:
            halfParamLen = 1
        for x in range(0, len(array)):
            if x > 9 and param[0:halfParamLen] in array[x]:
                returnArray.append(array[x])
        inflectedString = formatString(returnArray)
        
    except:
        inflectedString = 'error'
    print(inflectedString)
    return inflectedString

def formatString(array):
    array = list(dict.fromkeys(array))
    returningString = ', '.join([str(elem) for elem in array])
    return returningString

inflection(word)
