# currency exchange calculator 
# based on approximate set values 
# values used were collected for the date: 
# October 1, 2020

# convert 1 USD to -> 
'''
values from: 
https://www1.oanda.com/currency/comparison
australian_dollar = 1.4003
brazilian_real = 5.6274
british_pound = 0.77683
canadian_dollar = 1.33632
chinese_yuan = 6.80127
danish_krone = 6.34950
euro = 0.85284
hong_kong_dollar = 7.74988
hungarian_forint = 310.68414
indian_rupee = 73.56519
indonesian_rupiah = 14897.42782
japanese_yen = 105.57228
mexican_peso = 22.25874
new_zealand_dollar = 1.51507
norwegian_kroner = 9.40294
polish_zloty = 3.86343
russian_rouble = 78.24798
saudi_riyal = 3.74933
singapore_dollar = 1.36727
south_african_rand = 16.82467
swedish_krona = 8.97499
swiss_franc = 0.92104
taiwan_dollar = 28.95307
thai_baht = 31.59357
turkish_lira = 7.75733
us_dollar = 1

'''

'''
user_input = float(input("How many USD to TWD? "))
TWD = 28.95307
output = user_input * TWD
output = round(output, 2)     # change decimal to two points
print(str(user_input) + " USD was converted to: " + str(output) + " TWD. \nThank you for using our service.")
'''

# when called upon print list of available currencies and values
def print_currencies(): 
    print('\033[1m' + '\033[92m' + "CURRENCIES AVAILABLE TO EXCHANGE: " + '\033[0m' + 
    """
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
    """
    )
print_currencies()