from selenium import webdriver
from selenium.webdriver.firefox.options import  Options as FirefoxOptions


def fun(param):
	urlsDict = {
		"mainUrl": "https://wsjp.pl/szukaj/podstawowe/wyniki?szukaj={}",
		"printUrl": "https://wsjp.pl/haslo/do_druku/{}/{}"
		}
	options = FirefoxOptions()
	options.add_argument("--headless")
	browser = webdriver.Firefox(options=options)
	
	try:
		browser.get(urlsDict["mainUrl"].format(param))
		wordFromList = browser.find_element("xpath", "/html/body/main/div/div[1]/ul/li[1]/a").get_attribute("href").split("/")
		browser.get(urlsDict["printUrl"].format(wordFromList[5],param))
		inflectedForms = browser.find_element("css selector", ".expand_fleksja")
		array = inflectedForms.text.split()
		returnArray = []

		halfParamLen = int(len(param)/2)

		for x in range(0, len(array)):
			if x>9 and not ('.' in array[x] ) and param[0:halfParamLen] in array[x] :
				returnArray.append(array[x])

		inflectedString=formatString(returnArray)
		
		print(inflectedString)
		
		return inflectedString
	except:
		return 0
   
def formatString(array):
	array = list(dict.fromkeys(array))
	returningString = ', '.join([str(elem) for elem in array])
	return returningString

fun('ulica')



