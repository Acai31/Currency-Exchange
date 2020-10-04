# currency exchange calculator 

# values used were collected for the date: 
# October 1, 2020

# values from: 
# https://www1.oanda.com/currency/comparison


def main(): 
    print(values)
    que = int(input("Helo, please enter a number of what you would like to do today: \n1) exchange currencies \n2) view exchange rates \n"))
    if que == 1:
        exchange_currency()
    elif que == 2:
        print_currencies()



# values for converting
# value equivalent of 1 USD
# put values into dictionary so can call easily
values = dict()
values["AUD"] = 1.4003
values["BRL"] = 5.6274
values["GBP"] = 0.77683
values["CAD"] = 1.33632
values["CNY"] = 6.80127
values["DKK"] = 6.34950
values["EUR"] = 0.85284
values["HKD"] = 7.74988
values["HUF"] = 310.68414
values["INR"] = 73.56519
values["IDR"] = 14897.42782
values["JPY"] = 105.57228
values["MXN"] = 22.25874
values["NZD"] = 1.51507
values["NOK"] = 9.40294
values["PLN"] = 3.86343
values["RUB"] = 78.24798
values["SAR"] = 3.74933
values["SGD"] = 1.36727
values["ZAR"] = 16.82467
values["SEK"] = 8.97499
values["CHF"] = 0.92104
values["TWD"] = 28.95307
values["THB"] = 31.59357
values["TRY"] = 7.75733
values["USD"] = 1

# Get user input to see which currencies they would like to exchange
def exchange_currency():
    print("\n(if you do not know your exchange symbol, please enter \"help\" to refer to the exchange rates page)\n")
    before_currency = input("Please enter the Exchange Symbol of the currency you wish to exchange: ")
    if before_currency.lower() == "help":
        print_currencies()
    else: 

        if before_currency in values:
            exchange_before = values[before_currency]
        else: 
            print("Error: Exchange Symbol not found or not supported. ")
            exchange_currency()
        before_value = int(input("How much " + str(before_currency) + " do you wish to exchange? "))
        # ^ ASSUMES INPUT WILL BE INTEGER TRY EXCEPT CHECK IF INT OTHERWISE PRINT ERROR MESSAGE
        

        after_currency = input("Please enter the Exchange Symbol of the currency you wish to receive: ")
        if after_currency in values:
            exchange_after = values[after_currency]
        else: 
            print("Error: Exchange Symbol not found or not supported. ")

        after_value = before_value // exchange_before * exchange_after
        after_value = round(after_value, 2)
        print("\n" + '\033[1m' + str(before_value) + " " + str(before_currency) + '\033[0m' + " was converted to " + '\033[1m' + str(after_value) + " " + str(after_currency) + '\033[0m')
        print("Thank you for using this service, we hope to see you soon! \n")








# Print list of available currencies and values as well as their currency exchange symbols
def print_currencies(): 
    print("\n" + '\033[1m' + '\033[92m' + "Currency Exchange Rates: " + '\033[0m' + 
  """
  AUD     Australian Dollar: 1.4003
  BRL     Brazilian Real: 5.6274
  GBP     British Pound: 0.77683
  CAD     Canadian Dollar: 1.33632
  CNY     Chinese Yuan: 6.80127
  DKK     Danish Krone: 6.3495
  EUR     Euro: 0.85284
  HKD     Hong Kong Dollar: 7.74988
  HUF     Hungarian Forint: 310.68414
  INR     Indian Rupee: 73.56519
  IDR     Indonesian Rupiah: 14897.42782
  JPY     Japanese Yen: 105.57228
  MXN     Mexican Peso: 22.25874
  NZD     New Zealand Dollar: 1.51507
  NOK     Norwegian Kroner: 9.40294
  PLN     Polish Zloty: 3.86343
  RUB     Russian Rouble: 78.24798
  SAR     Saudi Riyal: 3.74933
  SGD     Singapore Dollar: 1.36727
  ZAR     South African Rand: 16.82467
  SEK     Swedish Krona: 8.97499
  CHF     Swiss Franc: 0.92104
  TWD     Taiwan Dollar: 28.95307
  THB     Thai Baht: 31.59357
  TRY     Turkish Lira: 7.75733
  USD     US Dollar: 1
  """
    )

main()