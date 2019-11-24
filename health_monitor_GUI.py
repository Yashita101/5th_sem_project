from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk,Image

main_screen=Tk()
main_screen.geometry("800x600")
main_screen.title("Health Monitoring System")


def patient_homepage():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("800x600")

    c=Canvas(login_screen,width=800,height=600)
    c.pack()
    image=PhotoImage(file="/home/pi/Desktop/IOT_PROJECT/Raspberry-Pi-Heartbeat-Pulse-Sensor/5th-Sem-Project-master/globe.png")
    c.create_image(400,300,anchor="center",image=image)
    background_label = Label(login_screen, image=image)
    background_label.image = image

    button11=Button(login_screen, text="View Prescription",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,bg='#F0FFFF',relief=RIDGE,bd=4)
    button11.configure(width=20,height=2)
    button_window11=c.create_window(480,250,anchor=SE,window=button11)

    button12=Button(login_screen, text="View Graph",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,bg='#F0FFFF',relief=RIDGE,bd=4)
    button12.configure(width=20,height=2)
    button_window12=c.create_window(480,350,anchor=SE,window=button12)

    button13=Button(login_screen, text="Back",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=login_screen.destroy,bg='#F0FFFF',relief=RIDGE,bd=2)
    button13.configure(width=12,height=2)
    button_window13=c.create_window(110,56,anchor=SE,window=button13)

    button14=Button(login_screen, text="Logout",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=main_account,bg='#F0FFFF',relief=RIDGE,bd=2)
    button14.configure(width=12,height=2)
    button_window14=c.create_window(795,56,anchor=SE,window=button14)

    


def prescription():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("800x600")

    c=Canvas(login_screen,width=800,height=600)
    c.pack()
    image=PhotoImage(file="/home/pi/Desktop/IOT_PROJECT/Raspberry-Pi-Heartbeat-Pulse-Sensor/5th-Sem-Project-master/globe.png")
    c.create_image(400,300,anchor="center",image=image)
    background_label = Label(login_screen, image=image)
    background_label.image = image

    label=Label(login_screen, text="Medicine Name",anchor=CENTER,justify=CENTER,font=('Times New Roman',14,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label.configure(width=15,height=2)
    label=c.create_window(350,150,anchor=SE,window=label)

    label1=Label(login_screen, text="Mg",anchor=CENTER,justify=CENTER,font=('Times New Roman',14,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label1.configure(width=15,height=2)
    label1=c.create_window(350,250,anchor=SE,window=label1)

    label2=Label(login_screen, text="Timings",anchor=CENTER,justify=CENTER,font=('Times New Roman',14,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label2.configure(width=15,height=2)
    label2=c.create_window(350,350,anchor=SE,window=label2)

    
    entry=Entry(c,textvariable=username_verify)
    c.create_window(500,125,window=entry,height=25,width=200)

    entry1=Entry(c, textvariable=username_verify)
    c.create_window(500,225,window=entry1,height=25,width=200)

    entry2=Entry(c, textvariable=username_verify)
    c.create_window(500,325,window=entry2,height=25,width=200)

    button1=Button(login_screen, text="Submit",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,bg='#F0FFFF',relief=RIDGE,bd=4)
    button1.configure(width=15,height=2)
    button_window1=c.create_window(475,450,anchor=SE,window=button1)

    button13=Button(login_screen, text="Back",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=login_screen.destroy,bg='#F0FFFF',relief=RIDGE,bd=2)
    button13.configure(width=12,height=2)
    button_window13=c.create_window(110,56,anchor=SE,window=button13)

    button14=Button(login_screen, text="Logout",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=login_screen.destroy,bg='#F0FFFF',relief=RIDGE,bd=2)
    button14.configure(width=12,height=2)
    button_window14=c.create_window(795,56,anchor=SE,window=button14)

    


def patient_detail():
    
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("800x600")

    c=Canvas(login_screen,width=800,height=600)
    c.pack()
    image=PhotoImage(file="/home/pi/Desktop/IOT_PROJECT/Raspberry-Pi-Heartbeat-Pulse-Sensor/5th-Sem-Project-master/globe.png")
    c.create_image(400,300,anchor="center",image=image)
    background_label = Label(login_screen, image=image)
    background_label.image = image

    label=Label(login_screen, text="Patient Id",anchor=CENTER,justify=CENTER,font=('Times New Roman',14,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label.configure(width=15,height=2)
    label=c.create_window(350,150,anchor=SE,window=label)

    label1=Label(login_screen, text="Patient Name",anchor=CENTER,justify=CENTER,font=('Times New Roman',14,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label1.configure(width=15,height=2)
    label1=c.create_window(350,250,anchor=SE,window=label1)

    label2=Label(login_screen, text="Diagnosis",anchor=CENTER,justify=CENTER,font=('Times New Roman',14,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label2.configure(width=15,height=2)
    label2=c.create_window(350,350,anchor=SE,window=label2)

    
    entry=Entry(c,textvariable=username_verify)
    c.create_window(500,125,window=entry,height=25,width=200)

    entry1=Entry(c, textvariable=username_verify)
    c.create_window(500,225,window=entry1,height=25,width=200)

    entry2=Entry(c, textvariable=username_verify)
    c.create_window(500,325,window=entry2,height=25,width=200)

    button1=Button(login_screen, text="Add Prescription",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=prescription,bg='#F0FFFF',relief=RIDGE,bd=4)
    button1.configure(width=15,height=2)
    button_window1=c.create_window(475,450,anchor=SE,window=button1)

    button13=Button(login_screen, text="Back",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=login_screen.destroy,bg='#F0FFFF',relief=RIDGE,bd=2)
    button13.configure(width=12,height=2)
    button_window13=c.create_window(110,56,anchor=SE,window=button13)

    button14=Button(login_screen, text="Logout",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=login_screen.destroy,bg='#F0FFFF',relief=RIDGE,bd=2)
    button14.configure(width=12,height=2)
    button_window14=c.create_window(795,56,anchor=SE,window=button14)
 

    

def doctor_homepage():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("800x600")

    c=Canvas(login_screen,width=800,height=600)
    c.pack()
    image=PhotoImage(file="/home/pi/Desktop/IOT_PROJECT/Raspberry-Pi-Heartbeat-Pulse-Sensor/5th-Sem-Project-master/globe.png")
    c.create_image(400,300,anchor="center",image=image)
    background_label = Label(login_screen, image=image)
    background_label.image = image

    label=Label(login_screen, text="DOCTOR HOMEPAGE",anchor=CENTER,justify=CENTER,font=('Times New Roman',18,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label.configure(width=25,height=2)
    label=c.create_window(570,150,anchor=SE,window=label)

    label1=Label(login_screen, text="Patient Id",anchor=CENTER,justify=CENTER,font=('Times New Roman',14,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label1.configure(width=17,height=2)
    label1=c.create_window(350,250,anchor=SE,window=label1)

    entry=Entry(c, textvariable=username_verify)
    c.create_window(500,225,window=entry,height=25,width=200)

    button1=Button(login_screen, text="OK",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=patient_detail,bg='#F0FFFF',relief=RIDGE,bd=4)
    button1.configure(width=8,height=1)
    button_window1=c.create_window(425,300,anchor=SE,window=button1)
 

    button1=Button(login_screen, text="View All Patients",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,bg='#F0FFFF',relief=RIDGE,bd=4)
    button1.configure(width=15,height=2)
    button_window1=c.create_window(450,425,anchor=SE,window=button1)
 

    button13=Button(login_screen, text="Back",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=login_screen.destroy,bg='#F0FFFF',relief=RIDGE,bd=2)
    button13.configure(width=12,height=2)
    button_window13=c.create_window(110,56,anchor=SE,window=button13)

    button14=Button(login_screen, text="Logout",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=login_screen.destroy,bg='#F0FFFF',relief=RIDGE,bd=2)
    button14.configure(width=12,height=2)
    button_window14=c.create_window(795,56,anchor=SE,window=button14)
 




def patient_login():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("800x600")

    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    

    c=Canvas(login_screen,width=800,height=600)
    c.pack()
    image=PhotoImage(file="/home/pi/Desktop/IOT_PROJECT/Raspberry-Pi-Heartbeat-Pulse-Sensor/5th-Sem-Project-master/globe.png")
    c.create_image(400,300,anchor="center",image=image)
    background_label = Label(login_screen, image=image)
    background_label.image = image


    label=Label(login_screen, text="Username",anchor=CENTER,justify=CENTER,font=('Times New Roman',14,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label.configure(width=15,height=2)
    label=c.create_window(350,250,anchor=SE,window=label)

    

    label1=Label(login_screen, text="Password",anchor=CENTER,justify=CENTER,font=('Times New Roman',14,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label1.configure(width=15,height=2)
    label1=c.create_window(350,350,anchor=SE,window=label1)

    
    label2=Label(login_screen, text="PATIENT LOGIN",anchor=CENTER,justify=CENTER,font=('Times New Roman',18,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label2.configure(width=25,height=2)
    label2=c.create_window(570,150,anchor=SE,window=label2)

    entry=Entry(c, textvariable=username_verify)
    c.create_window(500,225,window=entry,height=25,width=200)
    

    entry1=Entry(c, textvariable=password_verify)
    c.create_window(500,325,window=entry1,height=25,width=200)


    b=Button(login_screen, text="SUBMIT",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),command=patient_homepage,bg='#F0FFFF',relief=RIDGE,bd=4)
    b.configure(width=20,height=2)
    b_w=c.create_window(400,425,anchor=CENTER,window=b)

    button13=Button(login_screen, text="Back",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=login_screen.destroy,bg='#F0FFFF',relief=RIDGE,bd=2)
    button13.configure(width=12,height=2)
    button_window13=c.create_window(110,56,anchor=SE,window=button13)
 

 




def doctor_login():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("800x600")

    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    

    c=Canvas(login_screen,width=800,height=600)
    c.pack()
    image=PhotoImage(file="/home/pi/Desktop/IOT_PROJECT/Raspberry-Pi-Heartbeat-Pulse-Sensor/5th-Sem-Project-master/globe.png")
    c.create_image(400,300,anchor="center",image=image)
    background_label = Label(login_screen, image=image)
    background_label.image = image


    label=Label(login_screen, text="Username",anchor=CENTER,justify=CENTER,font=('Times New Roman',14,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label.configure(width=15,height=2)
    label=c.create_window(350,250,anchor=SE,window=label)

    

    label1=Label(login_screen, text="Password",anchor=CENTER,justify=CENTER,font=('Times New Roman',14,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label1.configure(width=15,height=2)
    label1=c.create_window(350,350,anchor=SE,window=label1)

    
    label2=Label(login_screen, text="DOCTOR LOGIN",anchor=CENTER,justify=CENTER,font=('Times New Roman',18,'bold'),state=NORMAL,bg='#F0FFFF',relief=SOLID,bd=1)
    label2.configure(width=25,height=2)
    label2=c.create_window(570,150,anchor=SE,window=label2)

    entry=Entry(c, textvariable=username_verify)
    c.create_window(500,225,window=entry,height=25,width=200)
    

    entry1=Entry(c, textvariable=password_verify)
    c.create_window(500,325,window=entry1,height=25,width=200)


    b=Button(login_screen, text="SUBMIT",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),command=doctor_homepage,bg='#F0FFFF',relief=RIDGE,bd=4)
    b.configure(width=20,height=2)
    b_w=c.create_window(400,425,anchor=CENTER,window=b)

    button13=Button(login_screen, text="Back",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=login_screen.destroy,bg='#F0FFFF',relief=RIDGE,bd=2)
    button13.configure(width=12,height=2)
    button_window13=c.create_window(110,56,anchor=SE,window=button13)
 


def login_page():
    
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Health Monitoring System")
    login_screen.geometry("800x600")
    
    c1=Canvas(login_screen,width=800,height=600)
    c1.pack()
    image=PhotoImage(file="/home/pi/Desktop/IOT_PROJECT/Raspberry-Pi-Heartbeat-Pulse-Sensor/5th-Sem-Project-master/globe.png")
    background_label = Label(login_screen, image=image)
    background_label.image = image      
    c1.create_image(400,300,anchor="center",image=image)
    
    button11=Button(login_screen, text="DOCTOR LOGIN",command=doctor_login,anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,bg='#F0FFFF',relief=RIDGE,bd=4)
    button11.configure(width=20,height=2)
    button_window11=c1.create_window(480,250,anchor=SE,window=button11)

    button12=Button(login_screen, text="PATIENT LOGIN",command=patient_login,anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,bg='#F0FFFF',relief=RIDGE,bd=4)
    button12.configure(width=20,height=2)
    button_window12=c1.create_window(480,350,anchor=SE,window=button12)

    button13=Button(login_screen, text="Back",anchor=CENTER,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,command=login_screen.destroy,bg='#F0FFFF',relief=RIDGE,bd=2)
    button13.configure(width=12,height=2)
    button_window13=c1.create_window(110,56,anchor=SE,window=button13)
    

c=Canvas(main_screen,width=800,height=600,bg="white")
c.pack()
image8=PhotoImage(file = "/home/pi/Desktop/IOT_PROJECT/Raspberry-Pi-Heartbeat-Pulse-Sensor/5th-Sem-Project-master/home.png")
c.create_image(400,300,anchor="center",image=image8)

button=Button(main_screen, text="LOGIN",relief=FLAT,anchor=S,justify=CENTER,font=('calibri',12,'bold'),command=login_page,bg='#EBF4FA',activebackground='#add8e6',bd=0)
button.configure(width=10,height=2)
button_window=c.create_window(800,30,anchor=SE,window=button)

button1=Button(main_screen, text="SIGN UP",relief=FLAT,anchor=S,justify=CENTER,font=('calibri',12,'bold'),state=NORMAL,bg='#EBF4FA',activebackground='#add8e6',bd=0)
button1.configure(width=10,height=2)
button_window1=c.create_window(700,30,anchor=SE,window=button1)





main_screen.mainloop()
