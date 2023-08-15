from apiaccess import PredictItScraper
import threading


predict_it = PredictItScraper()
# Check if it's a market for number of tweets
#rule = predict_it.get('/api/Market/%d' % id)['rule']

def gethotones():
    #contract_data = predict_it.get('/Market/%d/Contracts' % 6653)
    contract_data = predict_it.get('marketdata/all')
    #print(contract_data["markets"][0]['contracts'][0]['bestSellNoCost'])
    i=0
    j=0
    totals = []

    for market in range(len(contract_data["markets"])-1): 
        i=0  
        total = 0
        for contract in (contract_data["markets"][j]['contracts']):
            if (contract_data["markets"][j]['contracts'][i]['bestBuyNoCost'])!= None:
                total += 1-(contract_data["markets"][j]['contracts'][i]['bestBuyNoCost'])
            i+=1
        totals.append(total)
        j+=1

    hotoneswithseanevans = []

    for market in range(len(totals)): 
        if totals[market]>1.1:
            hotoneswithseanevans.append(str(market)+ " at " + str(totals[market]))

    return hotoneswithseanevans
    """for market in hotoneswithseanevans: 
        print(contract_data["markets"][market]["shortName"] + " = " + str(totals[market]))"""
    
gethotones()