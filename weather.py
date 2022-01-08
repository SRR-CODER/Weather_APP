import json
from tkinter import *  
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import timezonefinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.configure(bg="lime")
# bg=PhotoImage(file="D:\PROGRAMS\PYTHON\Holiday-Project\\bg.png")
root.title("Weather APP")
root.geometry("1000x600+400+300")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=timezonefinder.TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        # print(result)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+your_api_key
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather APP","Invalid Entry")


    

#search box
Search_image=PhotoImage(file="D:\PROGRAMS\PYTHON\Holiday-Project\search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("Poppins",25,"bold"),bg="#808080",border=0,fg="Yellow")
textfield.place(x=50,y=35)
textfield.focus()


Search_icon=PhotoImage(file="D:\PROGRAMS\PYTHON\Holiday-Project\search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg='#808080',command=getWeather)
myimage_icon.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file="D:\PROGRAMS\PYTHON\Holiday-Project\logo.png")
logo=Label(image=Logo_image)
logo.place(x=660,y=10)

#bottom box
Frame_image=PhotoImage(file="D:\PROGRAMS\PYTHON\Holiday-Project\\box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="Wind",font=("Helvetica",15,'bold'),fg="Brown",bg="#ADFF2F")
label1.place(x=120,y=450)

label2=Label(root,text="Humidity",font=("Helvetica",15,'bold'),fg="Brown",bg="#ADFF2F")
label2.place(x=225,y=450)

label3=Label(root,text="Description",font=("Helvetica",15,'bold'),fg="Brown",bg="#ADFF2F")
label3.place(x=330,y=450)

label4=Label(root,text="Pressure",font=("Helvetica",15,'bold'),fg="Brown",bg="#ADFF2F")
label4.place(x=670,y=450)


t=Label(font=("arial",70,"bold"),fg="Brown")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#ADFF2F")
w.place(x=120,y=500)
h=Label(text="...",font=("arial",20,"bold"),bg="#ADFF2F")
h.place(x=225,y=500)
d=Label(text="...",font=("arial",20,"bold"),bg="#ADFF2F")
d.place(x=330,y=500)
p=Label(text="...",font=("arial",20,"bold"),bg="#ADFF2F")
p.place(x=670,y=500)





root.mainloop()
