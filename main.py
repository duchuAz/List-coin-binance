import requests

data = requests.get('https://api.binance.com/api/v1/exchangeInfo').json()
symbols = map(lambda x: 'BINANCE:{}'.format(x['symbol']), data['symbols'])
symbols = filter(lambda x: 'USDT' in x, symbols)

print(','.join(symbols))