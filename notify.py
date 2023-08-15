import datetime
import threading 
import scrape
import pause

spicy = []

def notifyme():
    #threading.Timer(60, notifyme).start()
    while True:
        if scrape.gethotones() not in spicy:
            spicy.append(scrape.gethotones())
        #now = datetime.datetime.now()
        #print (now.strftime("%Y-%m-%d %H:%M:%S"))   
        print(spicy)
        pause.minutes(1)
notifyme()