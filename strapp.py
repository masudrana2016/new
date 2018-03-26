from bs4 import BeautifulSoup
import os, io, sys, time, re, csv
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import threading
from datetime import datetime
import datetime
import random
now = datetime.datetime.now()
sd=now.day
print sd
rd=31
if sd<=rd:
        sk="proxy.txt"
        fky="keyword.txt"
        if len(sk)<=2 and len(fky)<=2:
                print "please set path proxy "
        else:
            with open(fky, 'r+') as fkky:
                for row in fkky:
                    print " Start Extracting All questions of : " +str(row) 
                    data=[]
                    with open (sk, 'r+') as fils:
                        for rr in fils:
                              data.append(rr)
                    prs=random.choice(data)
                    options = webdriver.ChromeOptions()
                    options.add_argument("--headless")
                    options.add_argument("--proxy-server=socks5://"+str(prs));
                    options.add_argument('--no-sandbox')
                    driver = webdriver.Chrome(chrome_options=options)
                    driver.get("https://www.quora.com/search?q="+str(row)
                    
                    print prs
                    for x in range(0,8):
                        time.sleep(1)
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    data = driver.page_source
                    shoup=BeautifulSoup(data, "lxml")

                    rsk=shoup.findAll('a', attrs={'class': 'question_link'})
                    links=[]
                    for a in rsk:
                         try:
                            links.append(a['href'])
                         except KeyError:
                            pass                   
                    print "succesfully done all url"
                    par = "output.txt"
                    with open(par, 'a+') as file :
                        for raw in links:
                            rk=raw.replace("-"," ").replace("/","")
                            rd="https://www.quora.com"+raw
                            file.writelines("url:  "+rd +'\n')
                            file.writelines("Questions:  "+rk+"?"+ '\n')
                            file.writelines("------"+'\n')
                    driver.close()
                    print " All questions of : " +str(row)+"   Successfully Done"



else:
        print "someThing error"


            

