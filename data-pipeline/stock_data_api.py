#Stock API file
import requests as requests
import statistics

ticker = 'AAPL'
date_from = '2022-05-01'
date_to = '2022-05-20'
timespan = 'day'

class StockAPI:
    def getStock(ticker, timespan, date_from, date_to):
        result = requests.get('https://api.polygon.io/v2/aggs/ticker/'+ticker+'/range/1/'+timespan+'/'+date_from+'/'+date_to+'?adjusted=true&sort=asc&limit=120&apiKey=cIuSO8Ppb4LRsbWqirmxhU8ejDXNFVMW')
        result = result.json()
        allpoints = result['results']
        print('\nSTOCK: '+ticker+'\nFROM: '+date_from+'\nTO: '+date_to+'\nTIMESCALE: '+timespan+'\n')
        return allpoints
        
    def getStockAvg(ticker, timespan, date_from, date_to):
        result = requests.get('https://api.polygon.io/v2/aggs/ticker/'+ticker+'/range/1/'+timespan+'/'+date_from+'/'+date_to+'?adjusted=true&sort=asc&limit=120&apiKey=cIuSO8Ppb4LRsbWqirmxhU8ejDXNFVMW')
        result = result.json()
        
        close = []
        high = []
        low = []
        transactions = []
        open = []
        volume = []
        vw_price = []

        for day in result['results']:
            close.append(day['c'])
            high.append(day['h'])
            low.append(day['l'])
            transactions.append(day['n'])
            open.append(day['o'])
            volume.append(day['v'])
            vw_price.append(day['vw'])
        
        averages = {
            "Avg_Close": round(statistics.mean(close),2),
            "Avg_High": round(statistics.mean(high),2),
            "Avg_Low": round(statistics.mean(low),2),
            "Avg_Transaction_n": round(statistics.mean(transactions),2),
            "Avg_Open": round(statistics.mean(open),2),
            "Avg_Volume": round(statistics.mean(volume),2),
            "Avg_vwAVG": round(statistics.mean(vw_price),2),

        }

        return averages

    print(getStockAvg(ticker, timespan, date_from, date_to))

