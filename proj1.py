import tkinter as tk
import tkinter.messagebox as tmb
import time
from tkinter import *
from PIL import ImageTk, Image
import requests

def ret_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']



        f_str = 'Your City Is: %s \nWeather Condition: %s \nCurrent Temparature (F): %s \nPressure: %s \nHumidity: %s' %(name, desc, temp, pressure, humidity)
    except:
        f_str = 'Something Went Wrong!'

    return f_str

def get_weather(city):
    key = '5cb8c9b8dbe0c8ddf37e39e45a6edd9b'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    para = {'APPID': key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=para)
    weather = response.json()


    label2['text'] = ret_response(weather)

root = tk.Tk()
root.title('Know Temperature')
root.iconbitmap('E:/tkinter_project/a.ico')

canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()

# background_image = ImageTk.PhotoImage(file="./a.jpg")
# background_label= tk.Label(root, image=background_image)
# background_label.place(relheight=1.5,relwidth=1)

var = StringVar()
label1 = Label(root, textvariable=var,bg="lightyellow", bd=2, relief="solid",font="Times 12")
label1.place(rely=0.02,relx=0.2,relheight=0.15,relwidth=0.6)
var.set("Hey!? How are you doing?\nKnow Temparature Here")
# label.pack()

frame1 = tk.Frame(root, bg='forestgreen')
frame1.place(relx = 0.1, rely= 0.18, relheight= 0.08, relwidth=0.8)

e1 = Entry(frame1, bd=3, bg='pink', relief="solid", font=('gigi',10))
e1.place(rely=0.1, relheight=0.8, relwidth=0.6,relx=0.1 )

button = tk.Button(frame1, text="Submit", bg= 'red', fg='white', bd=3, relief="solid", command=lambda: get_weather(e1.get()))
button.place(rely=0.2, relheight=0.6, relx=0.75, relwidth=0.2 )
# button.pack()

frame2 = tk.Frame(root, bg='lemonchiffon2', bd=3, relief="solid")
frame2.place(relx = 0.1, rely= 0.28, relheight= 0.7, relwidth=0.8)

label2 = tk.Label(frame2, anchor='nw',justify='left', bd=4, font=('gigi',18))
label2.place(relwidth=1, relheight=1)

class Clock():
    def __init__(self):
        self.root = label1
        self.label = tk.Label(label1, text="Watch", font=('Helvetica', 10), bg ='black', fg='red')
        self.label.pack()
        self.update_clock()


    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=Clock()

root.mainloop()

