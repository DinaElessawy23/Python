TT = True

while TT:
  print("---------------------------------")
  print("Standard calculator   press 1 ")
  print("programmer Calculator press 2 ")
  print("exit                  press 0 ")
  print("---------------------------------")
  ch = int(input("enter your choice: "))
  print("---------------------------------")
  num1 = int(input("Enter num1: "))
  num2 = int(input("Enter num2: "))
  print("---------------------------------")
  if ch == 1:
    print("---------------------------------")
    print("Add      press 1")
    print("Sub      press 2")
    print("Muliply  press 3")
    print("Division press 4")
    print("Reminder press 5")
    print("Exit     press 0")
    print("---------------------------------")
    ch1 = int(input("Enter your choice: "))
    print("---------------------------------")
    if ch1 == 1:
      print("Addition = %d"%(num1 + num2))
    elif ch1 == 2:
      print("Subtraction = %d"%(num1 - num2))
    elif ch1 == 3:
      print("Muliplication = {}".format(num1 * num2))
    elif ch1 == 4:
      print("Division = " + str(num1 / num2))
    elif ch1 == 5:
      print("Reminder = " , str(num1 % num2))
    else:
      TT = False

  elif ch == 2 :
    print("------------------------------------------------")
    print("AND operator                         press 1 ")
    print("OR operator                          press 2 ")
    print("XOR operator                         press 3 ")
    print("NOT operator                         press 4 ")
    print("Shift right                          press 5 ")
    print("Shift left                           press 6 ")
    print("convert from decimal to binary       press 7 ")
    print("convert from decimal to hexadecimal  press 8 ")
    print("Exit                                 press 0 ")
    print("------------------------------------------------")
    ch2 = int(input("Your choice is: "))
    print("------------------------------------------------")
    
    if ch2 == 1:
      print("AND op = {}".format(num1 & num2))
    elif ch2 == 2:
      print("OR op = {}".format(num1 | num2))
    elif ch2 == 3:
      print("XOR op = ", str(num1 ^ num2))
    elif ch2 == 4:
      print("--------------------------------------------")
      print("Do u want to use NOT operator on num1  press 1 ")
      print("Do u want to use NOT operator on num2  press 2 ")
      print("--------------------------------------------")
      var = int(input("Your choice : "))
      print("--------------------------------------------")
      if var == 1:
        print("NOT on num1 = " + str(~num1))
      elif var == 2:
        print("NOT on num2 = " + str(~num2))
    elif ch2 == 5:
      print("--------------------------------------------")
      print("Do u want to use shift right operator on num1  press 1 ")
      print("Do u want to use shift right operator on num2  press 2 ")
      print("--------------------------------------------")
      var1 = int(input("Your choice : "))
      print("--------------------------------------------")
      shift = int(input("Enter number of shifts : "))
      print("--------------------------------------------")
      if var1 == 1:
        print("sift right on num1 = {}".format(num1 >> shift))
      elif var1 == 2:
        print("sift right on num2 = {}".format(num2 >> shift))

    elif ch2 == 6:
      print("--------------------------------------------")
      print("Do u want to use shift left  operator on num1  press 1 ")
      print("Do u want to use shift left  operator on num2  press 2 ")
      print("--------------------------------------------")
      var2 = int(input("Your choice : "))
      print("--------------------------------------------")
      shift1 = int(input("Enter number of shifts : "))
      print("--------------------------------------------")
      if var2 == 1:
        print("sift right on num1 = {}".format(num1 << shift1))
      elif var2 == 2:
        print("sift right on num2 = {}".format(num2 << shift1))

    elif ch2 == 7:
      print("--------------------------------------------")
      print("Do u want to convert from decimal to binary on num1  press 1 ")
      print("Do u want to convert from decimal to binary on num2  press 2 ")
      print("--------------------------------------------")
      var3 = int(input("Your choice : "))
      print("--------------------------------------------")
      if var3 == 1:
        print("Conversion to binary on num1 = {}".format(bin(num1)))
      elif var3 == 2:
        print("Conversion to binary on num2 = {}".format(bin(num2)))

    elif ch2 == 8:
      print("--------------------------------------------")
      print("Do u want to convert from decimal to hexadecimal on num1  press 1 ")
      print("Do u want to convert from decimal to hexadecimal on num2  press 2 ")
      print("--------------------------------------------")
      var4 = int(input("Your choice : "))
      print("--------------------------------------------")
      if var4 == 1:
        print("Conversion to binary on num1 = {}".format(hex(num1)))
      elif var4 == 2:
        print("Conversion to binary on num2 = {}".format(hex(num2)))

    elif ch2 == 0:
      TT = False

  else :
    TT = False