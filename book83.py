#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 08:19:55 2022

@author: AnantSrivastava
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 20:54:21 2022

@author: AnantSrivastava
"""

 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 17:13:43 2022

@author: AnantSrivastava
"""

import webbrowser
from tkinter import*

import smtplib
from PIL import ImageTk, Image
from tkinter import ttk
root=Tk()
root.attributes('-fullscreen', True)
root.configure(bg="#35DEED")
mummy=ImageTk.PhotoImage(Image.open("uwu.jpg"))
papa=ImageTk.PhotoImage(Image.open("papa.jpg"))
bahg=ImageTk.PhotoImage(Image.open("bg.jpg"))






person_image=Label(root, height=400,width=400)
person_image.place(relx=0.003,rely=0.3)

label_heading=Label(root, text="Reserve a Parent!", font=("times",40,"bold"),fg="Orange",bg="#35DEED",width=100,height=4)
label_heading.place(relx=0.5,rely=0.16,anchor=CENTER)



label_select_dish=Label(root,text="Select Human ", font=("times",15), highlightcolor= "red")
label_select_dish.place(relx=0.42,rely=0.26,anchor=CENTER)


dish=["Mummy","Papa"]
dish_dropdown=ttk.Combobox(root, state="readonly",value=dish)
dish_dropdown.place(relx=0.42,rely=0.3,anchor=CENTER)


label_select_addons=Label(root,text="Select Duration", font=("times",15), highlightcolor= "red")
label_select_addons.place(relx=0.42,rely=0.36,anchor=CENTER)


toppings=["10 Mins", "15 Mins","20 Mins","25 Mins","30 Mins"]
toppings_dropdown=ttk.Combobox(root,state="readonly",values=toppings)
toppings_dropdown.place(relx=0.42, rely=0.4,anchor=CENTER)


label_select_day=Label(root,text="Select Day", font=("times",15), highlightcolor= "red")
label_select_day.place(relx=0.42,rely=0.46,anchor=CENTER)


day=["Today", "Tomorrow"]
day_dropdown=ttk.Combobox(root,state="readonly",values=day)
day_dropdown.place(relx=0.42, rely=0.5,anchor=CENTER)


label_select_loc=Label(root,text="Select Location", font=("times",15), highlightcolor= "red")
label_select_loc.place(relx=0.58,rely=0.26,anchor=CENTER)


loc=["Anant's Room", "Aradhana's Room","Zimbabwbe"]
loc_dropdown=ttk.Combobox(root,state="readonly",values=loc)
loc_dropdown.place(relx=0.58, rely=0.3,anchor=CENTER)



label_select_name=Label(root,text="Select Your Name", font=("times",15), highlightcolor= "red")
label_select_name.place(relx=0.58,rely=0.36,anchor=CENTER)


name=["Anant", "Aradhana"]
name_dropdown=ttk.Combobox(root,state="readonly",values=name)
name_dropdown.place(relx=0.58, rely=0.4,anchor=CENTER)


label_select_name=Label(root,text="Slurp or NO Slurp", font=("times",15), highlightcolor= "red")
label_select_name.place(relx=0.58,rely=0.46,anchor=CENTER)


slurp=["YEAAHHHHH SLURPPPPP", "NO SLURP(Im a loser)"]
slurp_dropdown=ttk.Combobox(root,state="readonly",values=slurp)
slurp_dropdown.place(relx=0.58, rely=0.5,anchor=CENTER)











dish_amount=Label(root,font=("times",25,"bold"))
dish_amount.place(relx=0.5,rely=0.75,anchor=CENTER)



lol_amount=Label(root,font=("times",25,"bold"))
lol_amount.place(relx=0.5,rely=0.9,anchor=CENTER)
lol_amount.config(fg="#FF0000")







def book():
    global message
    global person
    person=dish_dropdown.get()
    time=toppings_dropdown.get()
    day=day_dropdown.get()
    loc=loc_dropdown.get()
    name=name_dropdown.get()
    slurp=slurp_dropdown.get()
    
    dish=StringVar()
    
    
   
    
    
    
        
    
    message=(person) +" you been booked by "+(name)+ " for "+ (time) +" at "+(loc)+ ". "+(person)+" you been booked for "+(day)
    dish_amount ["text"]=(person) +" has been booked by "+(name)+ " for "+(time)+" at "+(loc)+ ". "+(person)+" has been booked for "+(day)
    lol_amount ["text"]=" "
    if dish_dropdown.index("end") == 0:
        noname()
        
    if slurp_dropdown.index("end") == 0:
        noslurp()
        
    if toppings_dropdown.index("end") == 0:
        notime()
        
    if day_dropdown.index("end") == 0:
        noday()
        
    if loc_dropdown.index("end") == 0:
         noloc()
         
    if name_dropdown.index("end") == 0:
         nouser()
        
    
    if person=="Mummy":
             person_image['image']=mummy
             
    if person=="Papa":
             person_image['image']=papa
         
    
        
        
        
        
        
counter=0       
def noname():
     lol_amount ["text"]=" PLEASE SELECT NAME!!! "
     counter+1
     
def noslurp():
     lol_amount ["text"]=" PLEASE SELECT SLURPING OPTION!!! "
     dish_amount ["text"]=" "
     counter+1
     
def notime():
    lol_amount ["text"]=" PLEASE SELECT A TIME!!! "
    dish_amount ["text"]=" "
    counter+1
    
def noday():
    lol_amount ["text"]=" PLEASE SELECT A DAY!!! "
    dish_amount ["text"]=" "
    counter+1
    
def noloc():
    lol_amount ["text"]="PLEASE SELECT A LOCATION!!! "
    dish_amount ["text"]=" "
    counter+1
    
def nouser():
    lol_amount ["text"]=" PLEASE SELECT YOUR NAME!!! "
    dish_amount ["text"]=" "
    counter+1
    
    if (counter<4):
        lol_amount ["text"]="PLEASE FILL IN ALL OPTIONS"
        dish_amount ["text"]=" "
        
def send():
    global message
    global person
    print (message)
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("emailforwhitehat@gmail.com","msdyyxpwhnapqplc")
    
    if person=="Papa":
        server.sendmail("emailforwhitehat@gmail.com","email.ashishs@gmail.com",message)
        print("email sent to papa")
        server.quit()
        
    if person=="Mummy":
        server.sendmail("emailforwhitehat@gmail.com","nupurbhatnagar9@gmail.com",message)
        print("email sent to mother")
        server.quit()

        
#email.ashishs@gmail.com

#nupurbhatnagar9@gmail.com

    
    
send=Button(root, text="SEND EMAIL CONFERMATION",command=send)
send.place(relx=0.5, rely=0.64,anchor=CENTER)

btn=Button(root, text="CONFIRM RESERVATION",command= book)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)





root.mainloop()
