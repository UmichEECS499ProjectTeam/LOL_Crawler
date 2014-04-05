# -*- coding: utf8 -*-

import json
#filename = "/Users/huzhx/Desktop/SI650/wikia_champions/champsHomepage.json"
#json_data=open(filename)
#output = {}
#data = json.load(json_data)

def loadjson(filename):
    json_data=open(filename)
    return json.load(json_data)


def parseurldoc(adata):
    str = ""
    alist = []
    for i in adata["urldoc"]:
        str += i.strip() + " "

    str = str.split()
    for i in str:
        alist.append(i.encode("utf-8")) 
    return alist

#output = []
#for adata in data:
#    adocoutput = {}
#    url = adata["url"].encode("utf-8")
#    adocoutput[url] = parseurldoc(adata)
#    output.append(adocoutput) 

def getoutput(data):
    output = []
    for adata in data:
        adocoutput = {}
        url = adata["url"].encode("utf-8")
        adocoutput[url] = parseurldoc(adata)
        output.append(adocoutput)
    return output


def printout(anoutput,filename):
    f = open(filename, 'w')
    url = anoutput.keys()[0]
    
    f.write(url) 
    f.write('\n')
    for i in anoutput[url]:
        f.write(i)
        f.write('\n')
    f.close()  


#for i in output:
#    champname = i.keys()[0].split('/')[-1]
#    filename = '/Users/huzhx/Desktop/SI650/wikia_champions/champsdocs/%s.txt' % champname
#    printout(i,filename)
    
def outputfile(depth, output):
    for i in output:
        uniquename = i.keys()[0].split('/')[depth:]
        #filename = '/Users/huzhx/Desktop/SI650/wikia_champions/champsdocs/%s.txt' % uniquename
        filename = '/Users/huzhx/Desktop/scrape/urlcontent/%s.txt' % uniquename
        printout(i,filename)

#xaa = "/Users/huzhx/Desktop/scrape/xaa.json"
#xaaD = loadjson(xaa)
#xaaO = getoutput(xaaD)
#outputfile(0, xaaO)

for i in range(ord('a'), ord('l')):
    u = "/Users/huzhx/Desktop/scrape/xa%s.json" % chr(i)
    d = loadjson(u)
    o = getoutput(d)
    outputfile(0, o)

#Homepage = "/Users/huzhx/Desktop/SI650/wikia_champions/champsHomepage.json"
#Homepage = "/Users/huzhx/Desktop/SI650/wikia_champions/champsHomepage_v2.json"
#Homepage = "/Users/huzhx/Desktop/SI650/wikia_champions/champsHomepage_v3.json"
#Homepage_data = loadjson(Homepage)
#Homepage_output = getoutput(Homepage_data)
#outputfile(-1, Homepage_output)


#Background="/Users/huzhx/Desktop/SI650/wikia_champions/champsBackground.json"
#Background="/Users/huzhx/Desktop/SI650/wikia_champions/champsBackground_v2.json"
#Background="/Users/huzhx/Desktop/SI650/wikia_champions/champsBackground_v3.json"
#Background_data = loadjson(Background)
#Background_output = getoutput(Background_data)
#outputfile(-2, Background_output)


#Strategy="/Users/huzhx/Desktop/SI650/wikia_champions/champsStrategy.json"
#Strategy="/Users/huzhx/Desktop/SI650/wikia_champions/champsStrategy_v2.json"
#Strategy="/Users/huzhx/Desktop/SI650/wikia_champions/champsStrategy_v3.json"
#Strategy_data = loadjson(Strategy)
#Strategy_output = getoutput(Strategy_data)
#outputfile(-2, Strategy_output)


#SkinsTrivia="/Users/huzhx/Desktop/SI650/wikia_champions/champsSkinsTrivia.json"
#SkinsTrivia="/Users/huzhx/Desktop/SI650/wikia_champions/champsSkinsTrivia_v2.json"
#SkinsTrivia="/Users/huzhx/Desktop/SI650/wikia_champions/champsSkinsTrivia_v3.json"
#SkinsTrivia_data = loadjson(SkinsTrivia)
#SkinsTrivia_output = getoutput(SkinsTrivia_data)
#outputfile(-2, SkinsTrivia_output)



