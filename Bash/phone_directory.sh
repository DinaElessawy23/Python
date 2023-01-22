#!/bin/bash

while :
do
clear
echo "Welcome to the phone directory"
echo "1. Add a Contact"
echo "2. Search Contacts"
echo "3. Delete a Contact"
echo "4. Edit a Contact"
echo "5. view phone directory"
echo "6. Quit"

read -p "Enter Your Choice : " usr_cmd
clear

case $usr_cmd in 
1)echo "ADD NEW CONTACT"
  read -p "Enter Name : " name
  read -p "Enter Number : " number
  clear
  echo "New Contact Info:"
  echo "->Name:$name. -> Number:$number"
  echo "$name : $number" >> phonedir.log
  echo "Saved Successfully"  
;;
2)echo "SEARCH CONTACTS"
  read -p "Enter Contact Name to Search : " search_query
  clear
  echo "Search Results"
  grep -i $search_query phonedir.log
;;
3)echo "DELETE CONTACT"
  read -p "Enter Contact Name to be Deleted : " delete_string
  sed  -i -e "/$delete_string/d" phonedir.log
  echo "Deleted Successfully"
;;
4)echo "EDIT CONTACT"
echo "1. Edit Name"
echo "2. Edit number"
read -p "Enter Your Choice : " usr_ch
clear
case $usr_ch in
1)  read -p "Enter Contact Name to be Edited : " con_Name
    read -p "Enter New Name : " New_Name
    sed  -i -e "s/$con_Name/$New_Name/" phonedir.log
  ;;
2)  
  read -p "Enter Contact Number to be Edited : " con_Num
  read -p "Enter New Number : " New_Number
  sed  -i -e "s/$con_Num/$New_Number/" phonedir.log
  ;;
 esac 
  echo "Edited Successfully"
;;
5)echo "PHONE DIRECTORY"
  echo ""
  cat phonedir.log
;;
6)break;;
*)echo "INVALID OPTION";;
esac

read -p "Press 6 to Quit , Anything else to return to Main Menu" confirm_exit

if [ $confirm_exit -eq 6 ]
then break
fi
done
