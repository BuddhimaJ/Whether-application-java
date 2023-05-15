import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image,ImageTk
import ttkbootstrap

def get_weather(city):
    API_key = "cbc658f55cd6ce0abc32d89dfb47d9c1"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)
    
    if res.status_code == 404:
        messagebox.showerror("Error","City not found")
        return None

    weather = res.json
    icon_id = weather[weather][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather[weather][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f" https://openweathermap.org/img/wn{icon_id}@2x.png"
    return {icon_url,temperature,description,city,country}

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    ##
    icon_url,temperatuer,description,city,country = result
    location_label.configure(text=f"{city},{country}")

    image = Image.open(requests.get(icon_url,stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    Icon_label.configure(image=icon)
    Icon_label.image = icon

    temperature_label.configure(text = f"Temperature:{temperatuer:.2f}°C")
    description_label.configure(text=f"Description: {description}")

root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

#Entry widget 
city_entry = ttkbootstrap.Entry(root,font="Helvetica,18")
city_entry.pack(pady=10)

Search_button = ttkbootstrap.Button(root,text="search",command=search,bootstyle="warning")
Search_button.pack(pady=10)

Icon_label = tk.Label(root)
Icon_label.pack()

temperature_label = tk.Label(root, font="Helvetca,20")
temperature_label.pack()

location_label = tk.Label(root, font="Helvetca,20")
temperature_label.pack()

description_label = tk.Label(root, font="Helvetca,20")
description_label.pack()

root.mainloop()