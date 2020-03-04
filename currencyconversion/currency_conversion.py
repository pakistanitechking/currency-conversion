import requests


url = 'https://api.exchangerate-api.com/v4/latest/eur' #Api

data = requests.get(url)

exchange_api = data.json()
rates = exchange_api['rates']
#user input
usr_amt = int(input('Enter number of amounts : '))
usr_cur = input('which currency is this : ').upper()


if usr_cur in rates.keys():
    conv_cur = usr_amt * rates[f'{usr_cur}']
    print(f'For {usr_amt} Euro you will get {conv_cur} {usr_cur}')
else:
   print(f'{usr_cur} Does not exist')
# Ameerhamza,,,