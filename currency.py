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



user_input = float(input("How many USD to TWD? "))
TWD = 28.95307
output = user_input * TWD
output = round(output, 2)     # change decimal to two points
print(str(user_input) + " USD was converted to: " + str(output) + " TWD. \nThank you for using our service.")