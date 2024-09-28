def menu():
    print("1.Display products")
    print("2.Insert new")
    print("3.Search product")
    print("4.Delete a product by name")
    print("5.Exit")
    sel = input("Enter operation(1,2,3,4 or 5) :")
    while sel not in ["1","2","3","4","5"]:
        sel = input("no such choice , Enter operation(1,2,3,4 or 5) again:")
    return sel


def displayProducts(products,costs):
    for i in range(len(products)):
        print(products[i],costs[i])


def searchProduct(names,nameToSearch):
    for i in range(len(names)):
        if names[i] == nameToSearch:
            return i
    return -1

def deleteByName(names,prices,nameToSearch):
    for i in range(len(names)):
        if names[i] == nameToSearch:
            names.pop(i)
            price.pop(i)
            print("Successfully deleted")
            return
    print("Item not found")
