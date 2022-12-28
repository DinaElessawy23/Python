from tkinter import *
from PIL import ImageTk, Image
import csv

root=Tk()
root.title("Juice Shop")
root.geometry("800x700")
root.resizable(False,False)
my_dict={
"size" :["samll","medium","large"],
"price" :[30,40,50],
}
my_dict2=[
{"size" :"samll","price" :30},
{"size" :"medium","price" :40},
{"size" :"large","price" :50}
]
fields=["size","price"]
bill=[]
total=0

img = ImageTk.PhotoImage(Image.open("Background.png")) 
	 
label_bg=Label(root,image=img)
label_bg.place(x=0,y=0,relwidth=1,relheight=1)
heading=Label(root,text="Juice Shop",font="arial 30 bold",bg="#000",fg="#ea3548")
heading.pack(side=TOP)

def small_size():
     global total
     print("added 1 small with price : ",my_dict["price"][0])
     bill.append(my_dict["price"][0])
     total+=my_dict["price"][0] 
def medium_size():
     global total
     print("added 1 medium with price : ",my_dict["price"][1])
     bill.append(my_dict["price"][1])
     total+=my_dict["price"][1]
def large_size():
     global total
     print("added 1 large with price : ",my_dict["price"][2])
     bill.append(my_dict["price"][2])
     total+=my_dict["price"][2]
def print_bill():
     print(bill); 
def Total_Cost():
     print("Total cost is : ",total)
small = ImageTk.PhotoImage(Image.open('small.jpg'))

medium = ImageTk.PhotoImage(Image.open("medium.jpg"))

large = ImageTk.PhotoImage(Image.open("large.jpg"))
	 
button1=Button(root,image=small,bg="#000",bd=0,command=small_size)
button1.place(x=7,y=300)
button2=Button(root,image=medium,bg="#000",bd=0,command=medium_size)
button2.place(x=137,y=300)
button3=Button(root,image=large,bg="#000",bd=0,command=large_size)
button3.place(x=267,y=300)
Label(root,font=("arial",12),text="small",bg="#000",fg="#fff").place(x=7,y=300)
Label(root,font=("arial",12),text="medium",bg="#000",fg="#fff").place(x=137,y=300)
Label(root,font=("arial",12),text="large",bg="#000",fg="#fff").place(x=267,y=300)
B_2  =Button(root , text = "Exit" ,bg="#ea3548",bd=0,fg="#fff",width=20,height=2,font=("arial",10,"bold"), command = root.destroy)
B_2.place(x=635,y=500)
B_3  =Button(root , text = "print Bill" ,bg="#ea3548",bd=0,fg="#fff",width=20,height=2,font=("arial",10,"bold"), command = print_bill)
B_3.place(x=635,y=400)
B_1  =Button(root , text = "Total Cost" ,bg="#ea3548",bd=0,fg="#fff",width=20,height=2,font=("arial",10,"bold"), command = Total_Cost)
B_1.place(x=635,y=450)

root.mainloop()

file_name="dic.csv"
with open(file_name,'w',newline = '' ) as csvfile:
   writer=csv.DictWriter(csvfile,fieldnames=fields)
   writer.writeheader()
   for rows in my_dict2:
    writer.writerow(rows)