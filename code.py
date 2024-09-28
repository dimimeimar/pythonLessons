from funcs import *

names = ["LG-TV","APPLE-SMARTPHONE","DELL-LAPTOP"]
prices = [399,459,677]

while True:
    sel = menu()
    if sel == "1":
        displayProducts(names,prices)
    elif sel == "2":
        newName = input("Enter the name of the product to be inserted:")
        newPrice = float(input("Enter the price :"))
        names.append(newName)
        prices.append(newPrice)
    elif sel == "3":
        nameToSearch = input("Enter the name of the product you want to search:")
        pos = searchProduct(names,nameToSearch)
        if pos == -1:
            print("Product not found !!!")
        else:
            print("Product found and its price is :" , prices[pos])
    elif sel == "4":
        nameToSearch = input("Enter the name of the product you want to search:")
        deleteByName(names,prices,nameToSearch)
    else:
        print("GoodBye !!!")
        break