#Stock API file
import requests as requests

ticker = 'APPL'

class StockAPI:
    def getStock(ticker):
        result = requests.get('https://api.polygon.io/v2/aggs/ticker/'+ticker+'/range/1/day/2022-06-30/2022-06-30?adjusted=true&sort=asc&limit=120&apiKey=cIuSO8Ppb4LRsbWqirmxhU8ejDXNFVMW')
        result = result.json()
        
        return result

    print(getStock(ticker))