import tkinter as tk                
import time

current_balance=1000

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
		
        self.shared_data = {'Balance':tk.IntVar()}
		
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage, DepositPage, BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#19579a')
        self.controller = controller

        self.controller.title('ATM')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file='atm.png'))

        heading_label = tk.Label(self,
                                                     text='ATM MACHINE',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#19579a')
        heading_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#19579a')
        space_label.pack()

        password_label = tk.Label(self,
                                                      text='Enter your password',
                                                      font=('orbitron',13),
                                                      bg='#19579a',
                                                      fg='white')
        password_label.pack(pady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self,
                                                              textvariable=my_password,
                                                              font=('orbitron',12),
                                                              width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)
		
        def handle_focus_in(_):
            password_entry_box.configure(fg='black',show='*')
            
        password_entry_box.bind('<FocusIn>',handle_focus_in)
		
        def check_password():
           if my_password.get() == '123':
               my_password.set('')
               incorrect_password_label['text']=''
               controller.show_frame('MenuPage')
           else:
               incorrect_password_label['text']='Incorrect Password'
                
        enter_button = tk.Button(self,
                                                     text='Enter',
                                                     command=check_password,
                                                     relief='raised',
                                                     borderwidth = 3,
                                                     width=40,
                                                     height=3,bg='#123e6e',fg='white')
        enter_button.pack(pady=10)

        incorrect_password_label = tk.Label(self,
                                                                        text='',
                                                                        font=('orbitron',15),
                                                                        fg='#cc0000',
                                                                        bg='#ea8f62',
                                                                        anchor='n')
        incorrect_password_label.pack(fill='both',expand=True)
		
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo
		
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(1000,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()
		





class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#19579a')
        self.controller = controller
        heading_label = tk.Label(self,
                                                     text='ATM MACHINE',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#19579a')
        heading_label.pack(pady=25)		
		
        main_menu_label = tk.Label(self,
                                                           text='Main Menu',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#19579a')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                                           text='Please make a selection',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#19579a',
                                                           anchor='w')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self,bg='#ea8f62')
        button_frame.pack(fill='both',expand=True)

        def withdraw():
            controller.show_frame('WithdrawPage')
            
        withdraw_button = tk.Button(button_frame,
                                                            text='Withdraw',
                                                            command=withdraw,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5,bg='#123e6e',fg='white')
        withdraw_button.grid(row=0,column=0,pady=5)

        def deposit():
            controller.show_frame('DepositPage')
            
        deposit_button = tk.Button(button_frame,
                                                            text='Deposit',
                                                            command=deposit,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5,bg='#123e6e',fg='white')
        deposit_button.grid(row=1,column=0,pady=5)

        def balance():
            controller.show_frame('BalancePage')
            
        balance_button = tk.Button(button_frame,
                                                            text='Balance',
                                                            command=balance,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5,bg='#123e6e',fg='white')
        balance_button.grid(row=2,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,
                                                            text='Exit',
                                                            command=exit,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5,bg='#123e6e',fg='white')
        exit_button.grid(row=3,column=0,pady=5)
		
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo
		
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(1000,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()

class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#19579a')
        self.controller = controller
        heading_label = tk.Label(self,
                                                     text='ATM MACHINE',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#19579a')
        heading_label.pack(pady=25)		
		
        Choose_amount_label = tk.Label(self,
                                                           text='Choose the amount you want to withdraw',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#19579a')
        Choose_amount_label.pack()
		
        button_frame = tk.Frame(self,bg='#ea8f62')
        button_frame.pack(fill='both',expand=True)
		
		
        def withdraw(amount):
           global current_balance
           if amount>current_balance:
            incorrect_Amount_label['text']="Insufficient Funds | Balance Avaliable : $ ",current_balance
           else:
            current_balance -= amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')           
        
        incorrect_Amount_label = tk.Label(self,
                                                                        text='',
                                                                        font=('orbitron',15),
                                                                        fg='#cc0000',
                                                                        bg='#ea8f62',
                                                                        anchor='n')
        incorrect_Amount_label.pack(fill='both',expand=True)
            
        tow_hundred_button = tk.Button(button_frame,
                                                       text='200',
                                                       command=lambda:withdraw(200),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5,bg='#123e6e',fg='white')
        tow_hundred_button.grid(row=0,column=0,pady=5)

        four_hundred_button = tk.Button(button_frame,
                                                       text='400',
                                                       command=lambda:withdraw(400),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5,bg='#123e6e',fg='white')
        four_hundred_button.grid(row=1,column=0,pady=5)

        six_hundred_button = tk.Button(button_frame,
                                                       text='600',
                                                       command=lambda:withdraw(600),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5,bg='#123e6e',fg='white')
        six_hundred_button.grid(row=2,column=0,pady=5)

        eight_hundred_button = tk.Button(button_frame,
                                                       text='800',
                                                       command=lambda:withdraw(800),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5,bg='#123e6e',fg='white')
        eight_hundred_button.grid(row=3,column=0,pady=5)

        one_thousand_button = tk.Button(button_frame,
                                                       text='1000',
                                                       command=lambda:withdraw(1000),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5,bg='#123e6e',fg='white')
        one_thousand_button.grid(row=0,column=1,pady=5,padx=810)

        two_thousand_button = tk.Button(button_frame,
                                                       text='2000',
                                                       command=lambda:withdraw(2000),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5,bg='#123e6e',fg='white')
        two_thousand_button.grid(row=1,column=1,pady=5)

        three_thousand_button = tk.Button(button_frame,
                                                       text='3000',
                                                       command=lambda:withdraw(3000),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5,bg='#123e6e',fg='white')
        three_thousand_button.grid(row=2,column=1,pady=5)

        cash = tk.StringVar()
        other_amount_entry = tk.Entry(button_frame,
                                                              textvariable=cash,
                                                              width=59,
                                                              justify='right')
        other_amount_entry.grid(row=3,column=1,pady=5,ipady=30)

        other_amount_label = tk.Label(button_frame,
                                                           text='Other Amount',
                                                           font=('orbitron',13),
                                                           fg='black',
                                                           bg='#ea8f62',
                                                           anchor='w')
        other_amount_label.grid(row=4,column=1,pady=5)
		
        def other_amount(_):
            global current_balance
            current_balance -= int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('MenuPage')
            
        other_amount_entry.bind('<Return>',other_amount)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
		
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo
		
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(1000,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()		
class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#19579a')
        self.controller = controller
        self.controller.title('ATM')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file='atm.png'))

        heading_label = tk.Label(self,
                                                     text='ATM MACHINE',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#19579a')
        heading_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#19579a')
        space_label.pack()

        amount_label = tk.Label(self,
                                                      text='Enter your amount',
                                                      font=('orbitron',13),
                                                      bg='#19579a',
                                                      fg='white')
        amount_label.pack(pady=10)

        my_amonut = tk.StringVar()
        amonut_entry_box = tk.Entry(self,
                                                              textvariable=my_amonut,
                                                              font=('orbitron',12),
                                                              width=22)
        #amonut_entry_box.focus_set()
        amonut_entry_box.pack(ipady=7)

        def deposit():
            global current_balance
            current_balance += int(my_amonut.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            my_amonut.set('')
		   
        enter_button = tk.Button(self,
                                                     text='Enter',
                                                     command=deposit,
                                                     relief='raised',
                                                     borderwidth = 3,
                                                     width=40,
                                                     height=3,bg='#123e6e',fg='white')
        enter_button.pack(pady=10)
		
        button_frame = tk.Frame(self,bg='#ea8f62')
        button_frame.pack(fill='both',expand=True)
		
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
		
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()		
class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#19579a')
        self.controller = controller
        heading_label = tk.Label(self,
                                                     text='ATM MACHINE',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#19579a')
        heading_label.pack(pady=25)			

        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label = tk.Label(self,
                                                  textvariable=controller.shared_data['Balance'],
                                                  font=('orbitron',13),
                                                  fg='white',
                                                  bg='#19579a',
                                                  anchor='w')
        balance_label.pack(fill='x')
		
        button_frame = tk.Frame(self,bg='#ea8f62')
        button_frame.pack(fill='both',expand=True)

        def Menu():
            controller.show_frame('MenuPage')
            
        Menu_button = tk.Button(button_frame,
                                                            text='Menu',
                                                            command=Menu,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5,bg='#123e6e',fg='white')
        Menu_button.grid(row=0,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,
                                                            text='Exit',
                                                            command=exit,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5,bg='#123e6e',fg='white')
        exit_button.grid(row=1,column=0,pady=5)

		
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
	
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop() 