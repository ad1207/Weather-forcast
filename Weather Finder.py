#Weather Finder
from tkinter import *
from pip._vendor import requests
from pip._vendor.requests.exceptions import Timeout


def clear_all():
    noint.grid_forget()
    noname.grid_forget()
    city.delete(0, END)
    temperature.delete(0, END)
    wind.delete(0, END)
    humid.delete(0, END)
    city.focus_set()


def get_info():
    noint.grid_forget()
    noname.grid_forget()    
    temperature.delete(0, END)
    wind.delete(0, END)
    humid.delete(0, END)
    cityname = str(city.get())
    if(cityname==''):
        noname.grid(row=2,column=1)
        return    
    try:
        citydata = requests.get('https://api.weatherapi.com/v1/current.json?key=9fd40fc55d0f408fb6253313212312&q=%s&aqi=no'%cityname,timeout=10)
        cityda = citydata.json()
        temp=str(cityda["current"]['temp_c'])+'°C/'+str(cityda["current"]['temp_f'])+'°F'
        windd=str(cityda["current"]['wind_kph'])+' km/h'
        humidity=str(cityda["current"]['humidity'])+'%'
        temperature.insert(0,temp)
        wind.insert(0,windd)
        humid.insert(0,humidity)
    except(requests.ConnectionError, requests.Timeout) as exception:
        noint.grid(row=2,column=1)
    except(KeyError) as exception:
        noname.grid(row=2,column=1)



root = Tk()

root.configure(background='grey')
root.geometry("400x280")

root.title("Weather")
titleframe= Frame(root,bg='grey')
title = Label(titleframe,text="Weather Forecast",bg='grey',fg='black',font=('Arial',15))
label1 = Label(root, text="City Name :", fg='white',bg='grey')
label2 = Label(root, text="Temperature:", fg='white',bg='grey')
label3 = Label(root, text="Wind:", fg='white',bg='grey')
label4 = Label(root, text="Humidity:", fg='white',bg='grey')
noname = Label(titleframe,text='Please Enter Valid City Name',fg='red' ,bg='grey')
noint = Label(titleframe,text="No Internet Connection", fg='red' ,bg='grey')
titleframe.grid(row=1,column=1,padx=10,pady=10)
title.grid(row=1,column=1,padx=10)
label1.grid(row=2, column=0, padx=10, pady=10)
label2.grid(row=4, column=0, padx=10, pady=10)
label3.grid(row=5, column=0, padx=10, pady=10)
label4.grid(row=6, column=0, padx=10, pady=10)

city = Entry(root)
temperature = Entry(root)
wind = Entry(root)
humid = Entry(root)

city.grid(row=2, column=1, padx=10, pady=10)
temperature.grid(row=4, column=1, padx=10, pady=10)
wind.grid(row=5, column=1, padx=10, pady=10)
humid.grid(row=6, column=1, padx=10, pady=10)

frame = Frame(root)
frame.grid(row=3, column=1)

button1 = Button(frame, text="Submit", bg="blue", fg="black", command=get_info)

button2 = Button(frame, text="Clear", bg="blue", fg="black", command=clear_all)

button1.grid(row=0, column=1, pady=0)
button2.grid(row=0, column=0, pady=0)

root.mainloop()
