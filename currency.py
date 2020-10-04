# currency exchange calculator 
# based on approximate set values 
# values used were collected for the date: 
# October 1, 2020

# convert 1 USD to -> 
'''
values from: 
https://www1.oanda.com/currency/comparison
Australian Dollar: 1.4003
Brazilian Real: 5.6274
British Pound: 0.77683
Canadian Dollar: 1.33632
Chinese Yuan: 6.80127
Danish Krone: 6.3495
Euro: 0.85284
Hong Kong Dollar: 7.74988
Hungarian Forint: 310.68414
Indian Rupee: 73.56519
Indonesian Rupiah: 14897.42782
Japanese Yen: 105.57228
Mexican Peso: 22.25874
New Zealand Dollar: 1.51507
Norwegian Kroner: 9.40294
Polish Zloty: 3.86343
Russian Rouble: 78.24798
Saudi Riyal: 3.74933
Singapore Dollar: 1.36727
South African Rand: 16.82467
Swedish Krona: 8.97499
Swiss Franc: 0.92104
Taiwan Dollar: 28.95307
Thai Baht: 31.59357
Turkish Lira: 7.75733
US Dollar: 1

'''

user_input = float(input("How many USD to TWD? "))
user_input *= 28.95307 
user_input = user_input     # change decimal to two points
print(user_input)