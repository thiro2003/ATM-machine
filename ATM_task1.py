from tkinter import *
import mysql.connector as db
from tkinter import messagebox


#################  CLASS TO WITHDRAW MONEY FROM ACCOUNT  ####################################################################
class withdraw:
    def depomoney(self):
          
              bal=int(self.amt.get())
              Pind=int(self.pindepo.get())
              con=db.connect(host="localhost",user="root",password="thiro",database="ATM") 
              cursor=con.cursor()
              cursor.execute("select balance,pin from info where id=1")
              balpin=cursor.fetchall()
              baldata=balpin[0][0]
              pindata=balpin[0][1]
              
             
              
              if(Pind==pindata):
                  updatedbal=baldata- bal
                  cursor.execute(f"update info set balance={updatedbal}")
                  balance_msg=Label(self.root,text=f"Your balance is {updatedbal}",font=17,bg="#CD7F32",fg="white").place(x=170,y=500)
                  con.commit()
              else:
                messagebox.showerror("Error", "साहेब कृपया उपकार करा आणि माहिती बरोबर भरा 🙏")  
                      
                  
              
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600+550+100")
        self.root.title("ATM")
        self.root.iconbitmap(r"ATM.ico")
        self.root.configure(bg="#CD7F32")
        
        heading = Label(self.root, text="Withdraw Amount", bg="#CD7F32", fg="white", font=("Arial", 20))
        heading.pack(pady=100)
        
        pinl = Label(self.root, text="Enter pin :", font=("Arial", 17),bg="#CD7F32",fg="white")
        pinl.place(x=10, y=200)
        
        self.pindepo = Entry(self.root, font=("Arial", 17),bg="#CD7F32",fg="white")
        self.pindepo.place(x=260, y=200)
        
        amtl = Label(self.root, text="Enter Withdraw Amount :", font=("Arial", 17),bg="#CD7F32",fg="white")
        amtl.place(x=10, y=300)
        
        self.amt = Entry(self.root, font=("Arial", 17),bg="#CD7F32",fg="white")
        self.amt.place(x=260, y=300)
        
    
        # check balance
        deposit=Button(self.root,text="Deposit Money",bg="#CD7F32",fg="white",font=17,command=self.depomoney).place(x=230,y=400)
        #ac/pin/bal/

#################  CLASS TO CHANGE PIN OF ACCOUNT  ####################################################################

class change_pin :    
          def ckpin (self):
            currentpin=int(self.cpin.get())
            newpin=int(self.npin.get())
            con=db.connect(host="localhost",user="root",password="thiro",database="ATM")
            cursor=con.cursor()
            cursor.execute("select pin from info where id=1")
            orgpin=cursor.fetchone()
            orgpin=orgpin[0]
            if(currentpin==orgpin):
              updatedpin=newpin
              cursor.execute(f"update info set pin={updatedpin} where pin={currentpin}")
              balance_msg=Label(self.root,text=f"Your new pin is {updatedpin}",font=17,bg="#00A36C",fg="white").place(x=170,y=500)
              con.commit()
            else:
             messagebox.showerror("Error", "साहेब कृपया उपकार करा आणि माहिती बरोबर भरा 🙏")  
                
          def __init__(self, root):
            self.root = root
            self.root.geometry("600x600+550+100")
            self.root.title("ATM")
            self.root.iconbitmap(r"ATM.ico")
            self.root.configure(bg="#00A36C")
            
            heading = Label(self.root, text="Change Pin", bg="#00A36C", fg="white", font=("Arial", 20))
            heading.pack(pady=100)
            
            pinl = Label(self.root, text="Enter Current  Pin :", font=("Arial", 17),bg="#00A36C",fg="white")
            pinl.place(x=10, y=200)
            
            self.cpin = Entry(self.root, font=("Arial", 17),bg="#00A36C",fg="white")
            self.cpin.place(x=260, y=200)
            
            amtl = Label(self.root, text="Enter New Pin :", font=("Arial", 17),bg="#00A36C",fg="white")
            amtl.place(x=10, y=300)
            
            self.npin = Entry(self.root, font=("Arial", 17),bg="#00A36C",fg="white")
            self.npin.place(x=260, y=300)
            
        
            # check balance
            deposit=Button(self.root,text="Change Pin",bg="#00A36C",fg="white",font=17,command=self.ckpin).place(x=230,y=400)
            #ac/pin/bal/
        
        
     
        


#################  CLASS TO CHECK BALANCE IN ACCOUNT  ####################################################################

class CKBAL:
    def check(self):
        userpin=int(self.pinck.get())
        con=db.connect(host="localhost",user="root",password="thiro",database="ATM")
        cursor=con.cursor()
        cursor.execute("select pin from info where id=1")
        data=cursor.fetchall()
        Dpin=data[0][0]
        print(Dpin)
        if(userpin==Dpin):
            cursor.execute(f"select balance from info where pin={Dpin}")
            balance=cursor.fetchone()
            print(balance[0])
            balance_msg=Label(self.root,text=f"Your balance is {balance[0]}",font=17,bg="#800020",fg="white").place(x=170,y=500)
        else:
            messagebox.showerror("Error", "साहेब कृपया उपकार करा आणि माहिती बरोबर भरा 🙏")  
                
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600+550+100")
        self.root.title("ATM")
        self.root.iconbitmap(r"ATM.ico")
        self.root.configure(bg="#800020")
        
        heading = Label(self.root, text="Check balance", bg="#DC143C", fg="white", font=("Arial", 20))
        heading.pack(pady=100)
        
        pinl = Label(self.root, text="Enter pin :", font=("Arial", 17),bg="#DC143C",fg="white")
        pinl.place(x=100, y=200)
        
        self.pinck = Entry(self.root, font=("Arial", 17),bg="#DC143C",fg="white")
        self.pinck.place(x=260,y=200)
        deposit=Button(self.root,text="Check Balance",bg="#DC143C",fg="white",font=17,command=self.check).place(x=230,y=400)
            
#################  CLASS TO AMOUNT IN ACCOUNT  ####################################################################
           
class DEPO:
    def depomoney(self):
          
              bal=int(self.amt.get())
              Pind=int(self.pindepo.get())
              con=db.connect(host="localhost",user="root",password="thiro",database="ATM") 
              cursor=con.cursor()
              cursor.execute("select balance,pin from info where id=1")
              balpin=cursor.fetchall()
              baldata=balpin[0][0]
              pindata=balpin[0][1]
              
             
              
              if(Pind==pindata):
                  updatedbal=baldata+ bal
                  cursor.execute(f"update info set balance={updatedbal}")
                  balance_msg=Label(self.root,text=f"Your balance is {updatedbal}",font=17,bg="#FF2400",fg="white").place(x=170,y=500)
                  con.commit()
              else:
                messagebox.showerror("Error", "साहेब कृपया उपकार करा आणि माहिती बरोबर भरा 🙏")  
                      
                  
              
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600+550+100")
        self.root.title("ATM")
        self.root.iconbitmap(r"ATM.ico")
        self.root.configure(bg="#FF2400")
        
        heading = Label(self.root, text="Deposit Money", bg="#FF2400", fg="white", font=("Arial", 20))
        heading.pack(pady=100)
        
        pinl = Label(self.root, text="Enter pin :", font=("Arial", 17),bg="#FF2400",fg="white")
        pinl.place(x=10, y=200)
        
        self.pindepo = Entry(self.root, font=("Arial", 17),bg="#FF2400",fg="white")
        self.pindepo.place(x=260, y=200)
        
        amtl = Label(self.root, text="Enter Deposit Amount :", font=("Arial", 17),bg="#FF2400",fg="white")
        amtl.place(x=10, y=300)
        
        self.amt = Entry(self.root, font=("Arial", 17),bg="#FF2400",fg="white")
        self.amt.place(x=260, y=300)
        
    
        # check balance
        deposit=Button(self.root,text="Deposit Money",bg="#C04000",fg="white",font=17,command=self.depomoney).place(x=230,y=400)
        #ac/pin/bal/

#################  MAIN METHOD TO ACCESS THE ACCOUNT  ####################################################################

class ATM:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600+550+100")
        self.root.title("ATM")
        self.root.iconbitmap(r"ATM.ico")
        self.root.configure(bg="#8A2BE2")
        
        heading = Label(self.root, text="ATM Machine", bg="white", fg="black", font=("Arial", 20))
        heading.pack(pady=100)
        
        acl = Label(self.root, text="Enter the A/c no :", font=("Arial", 17))
        acl.place(x=100, y=200)
        
        self.ac = Entry(self.root, font=("Arial", 17))
        self.ac.place(x=290, y=200)
        
        acp = Label(self.root, text="Enter the Pin :", font=("Arial", 17))
        acp.place(x=100, y=300)
        
        self.Pin = Entry(self.root, font=("Arial", 17))
        self.Pin.place(x=270, y=300)
        
        submit_button = Button(self.root, width=10, font=("Arial", 17), text="Submit", command=self.submit)
        submit_button.place(x=260, y=400)
        
    def submit(self):
        Ac = int(self.ac.get())
        pin = int(self.Pin.get())
        con=db.connect(host="localhost",user="root",password="thiro",database="ATM")
        cursor=con.cursor()
        cursor.execute("select * from info")
        rows=cursor.fetchall()
        ac=rows[0][1]
        ppin=rows[0][2]
        if(ppin==pin and ac==Ac):
#################  CLASS TO SHOW VARIOUS OPERATION IN ATM  ####################################################################
         
         class Home:
             def depo(self):
                 if __name__ == "__main__":
                    root = Tk()
                    atm_app = DEPO(root)
                    root.mainloop()   
             def ckbaldef(self):
                 if __name__ == "__main__":
                    root = Tk()
                    atm_app = CKBAL(root)
                    root.mainloop()   
             def change_pin_method(self):
                 if __name__ == "__main__":
                    root = Tk()
                    atm_app = change_pin(root)
                    root.mainloop()  
             def withdraw_money_method(self):
                 if __name__ == "__main__":
                    root = Tk()
                    atm_app =withdraw (root)
                    root.mainloop()                
             def __init__(self, root):
                 self.root = root
                 self.root.geometry("600x600+550+100")
                 self.root.title("ATM")
                 self.root.iconbitmap(r"ATM.ico")
                 self.root.configure(bg="#DC143C")
                 
                 heading = Label(self.root, text="ATM Machine", bg="#DC143C", fg="white", font=("Arial", 20))
                 heading.pack(pady=100)
                 
                 # deposit money
                 deposit=Button(self.root,text="Deposit Money",bg="#301934",fg="white",font=17,command=self.depo).place(x=100,y=250)
                 # check balance
                 checkbal=Button(self.root,text="Check Balance",bg="#1434A4",fg="white",font=17,command=self.ckbaldef).place(x=350,y=250)
                 
                  # change pin
                 changepin=Button(self.root,text="Change Pin",bg="#00A36C",fg="white",font=17,command=self.change_pin_method).place(x=100,y=400)
                 # check balance
                 witdrawamt=Button(self.root,text="Withdraw Money",bg="#CD7F32",fg="white",font=17,command=self.withdraw_money_method).place(x=350,y=400)
                 
                 
                 
                 
        if __name__ == "__main__":
                    root = Tk()
                    atm_app = Home(root)
                    root.mainloop()        
        else:
            print("invalid") 
            messagebox.showerror("Error", "साहेब कृपया उपकार करा आणि माहिती बरोबर भरा 🙏")  
            
        
            

if __name__ == "__main__":
    root = Tk()
    atm_app = ATM(root)
    root.mainloop()
    
    
    
    #########     PIN=123 AND ACCOUND NUMBER=123   #################
    # THANK YOU
