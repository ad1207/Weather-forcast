#Weather Finder
from tkinter import *
from pip._vendor import requests


def clear_all():
    city.delete(0, END)
    temperature.delete(0, END)
    wind.delete(0, END)
    humid.delete(0, END)
    city.focus_set()


def get_info():
    temperature.delete(0, END)
    wind.delete(0, END)
    humid.delete(0, END)
    cityname = str(city.get())
    citydata = requests.get('https://api.weatherapi.com/v1/current.json?key=9fd40fc55d0f408fb6253313212312&q=%s&aqi=no'%cityname)
    cityda = citydata.json()
    temp=str(cityda["current"]['temp_c'])+'°C/'+str(cityda["current"]['temp_f'])+'°F'
    windd=str(cityda["current"]['wind_kph'])+' km/h'
    humidity=str(cityda["current"]['humidity'])+'%'
    temperature.insert(0,temp)
    wind.insert(0,windd)
    humid.insert(0,humidity)
    


root = Tk()

root.configure(background='grey')
root.geometry("400x250")

root.title("Weather")

title = Label(root,text="Weather Forecast",bg='grey',fg='black',font=('Arial',15))
label1 = Label(root, text="City Name :", fg='white',bg='grey')
label2 = Label(root, text="Temperature:", fg='white',bg='grey')
label3 = Label(root, text="Wind:", fg='white',bg='grey')
label4 = Label(root, text="Humidity:", fg='white',bg='grey')

title.grid(row=1,column=1,padx=10,pady=10)
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