import requests
from bs4 import BeautifulSoup
import os, io, sys, time, re, csv
import threading
from datetime import datetime
import datetime
import random
now = datetime.datetime.now()
sd=now.month
#print (sd)
rd=4
if sd<=rd:
        sk="proxy.txt"
        fky="keyword.txt"
        if len(sk)<=2 and len(fky)<=2:
                print ("please set path proxy ")
        else:
            with open(fky, 'r+') as fkky:
                for row in fkky:
                    print (" Start Extracting All questions of : " +str(row) )
                    data=[]
                    with open (sk, 'r+') as fils:
                        for rr in fils:
                              data.append(rr)
                    prs=random.choice(data)
                    proxier = {
                    "http": str(prs),
                    "https": str(prs),
                     }
                   
                    url = "https://www.quora.com/search?q="+str(row)
                    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                        
                    response = requests.get(url, headers=headers)
                    data=response.content
                    time.sleep(3)
                    
                    print (prs)
                    
                    shoup=BeautifulSoup(data)

                    rsk=shoup.findAll('a', attrs={'class': 'question_link'})
                    links=[]
                    for a in rsk:
                         try:
                            links.append(a['href'])
                         except KeyError:
                            pass                   
                    print (links)
                    par = "output.txt"
                    with open(par, 'a+', encoding='utf-8') as file :
                        for raw in links:
                            rk=raw.replace("-"," ").replace("/","")
                            rd="https://www.quora.com"+raw
                            file.writelines("url:  "+str(rd) +'\n')
                            file.writelines("Questions:  "+str(rk)+"?"+ '\n')
                            file.writelines("------"+'\n')
                   
                               
                    print (" All questions of : " +str(row)+"   Successfully Done")



else:
        print ("someThing error")
