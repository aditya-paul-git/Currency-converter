with open('currency_data.txt') as f:
   lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter ammount you want to convert: "))
print("Enter the name of currency you want to convert "
      "from available options... :\n")
[print(item)for item in currencyDict.keys()]
currency_name = input("Enter currency name: ")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency_name])} {currency_name}")
