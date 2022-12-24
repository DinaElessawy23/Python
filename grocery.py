import time
import os
grocery_dict = {
    "shop name" : "Market",
    "lists"     : ["banana", "apple", "orange", "tomato"],
    "price"     : [25,        33,       85,     99],
    "stock"     : [3,         5,        9,      10],

}

customer = {
    "bag"       : [],
    "quantity"  : [],
    "bill"      : [],
}


print("--------------------------- welcome to ITI Market -----------------------------")
time.sleep(2)

TT = True
while TT :
  #os.system("cls")
  print("Grocery owner  press 1 ")
  print("Customer       press 2 ")
  print("exit           press 0 ")
  print("---------------------------")

  x = int(input("Enter your choice: "))

  print("---------------------------")

  if x == 1:
   T = True
   while T :
    print("show all items press 1 ")
    print("add items      press 2 ")
    print("change price   press 3 ")
    print("exit           press 0 ")
    print("---------------------------")
    y = int(input("Enter your choice: "))
    print("---------------------------")
    if y == 1:
      print(grocery_dict["lists"])
    elif y == 2:
      z1 = input("Please add your items:  ")
      grocery_dict["lists"].append(z1)
      z2 = int(input("Please add items' price:  "))
      grocery_dict["price"].append(z2)
      z3 = int(input("Please add items quantity:  "))
      grocery_dict["stock"].append(z3)
      print("----------------------------------")
      print(grocery_dict["lists"])
      print(grocery_dict["price"])
      print(grocery_dict["stock"])
      print("----------------------------------")
    elif y == 3 :
      print(grocery_dict["lists"])
      o = input("Which element do you want to change it's price:   ")
      price = int(input("What is the new price"))
      grocery_dict["price"][grocery_dict["lists"].index(o)] = price

    else:
       T = False

  elif x == 2 :
    print("you want to buy element  press 1 ")
    #print("to print the  bills      press 2 ")
    print("Exit                     press 0 ")
    print("---------------------------")
    choice = int(input("Enter your choice: "))
    print("---------------------------")
    if choice == 1 :
      print(grocery_dict["lists"])
      print(grocery_dict["price"])
      print(grocery_dict["stock"])
      loop = True
      while loop:
        print("-------------------------------------")
        print("-------------------------------------")
        print("Continue buying  press 1")
        print("print bills      press 2")
        print("Finished         press 0")
        buy = int(input("your choice:  "))
        print("-------------------------------------")
        print("-------------------------------------")
        if buy == 1:
          element = input("Enter your element:  ")
          customer["bag"].append(grocery_dict["lists"][grocery_dict["lists"].index(element)])
          print(customer["bag"])
          quantity = int(input("Enter your quantity of this element:  "))
          customer["quantity"].append(quantity)
          grocery_dict["stock"][grocery_dict["lists"].index(element)] -= quantity
          print(grocery_dict["stock"])

        elif buy == 2:
          bills = 0
          print(len(customer["bag"]))
          for i in range(len(customer["bag"])):
            bills += grocery_dict["price"][grocery_dict["lists"].index(customer["bag"][i])] * customer["quantity"][i]
            print(bills)
        elif buy == 0:
          loop = False

    #elif choice == 2 :
     # bills = 0
      #for i in range(len(customer["bag"])):
      # bills += grocery_dict["price"][grocery_dict["lists"].index(customer["bag"][i])] * customer["quantity"][i]

      #bill = int(input("bills: "))
      #customer["bill"].append(bill)
      #print("bills = ".format(bills))

    else:
      TT = False


  else:
    TT = False
