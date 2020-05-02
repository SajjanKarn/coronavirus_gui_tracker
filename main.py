from tkinter import *
from covid import Covid
from tkinter import ttk
from time import strftime

covid = Covid(source="worldometers")

root = Tk()

universal_font = ('Arial', 16)


def live_clock():
    time = strftime("%x - %I:%M:%S %p")
    time_label.configure(text=time)
    time_label.after(100, live_clock)


def get_country(event):
    selected_country = country_combobox.get()
    # total confirmed cases label and data

    country_name_label.configure(text=selected_country)
    #
    total_confirmed_data.configure(text=covid.get_status_by_country_name(selected_country)['confirmed'])
    total_deaths_data.configure(text=covid.get_status_by_country_name(selected_country)['deaths'])
    total_recovered_data.configure(text=covid.get_status_by_country_name(selected_country)['recovered'])


def world_statistics():
    world_label = Label(world_frame, text="World", font=universal_font, bg="#fae7cb", fg="black")
    world_label.place(x=20, y=50)

    corona_pic = PhotoImage(file="corona.png")  # set a other photo image
    img = corona_pic.zoom(10)  # with 250, I ended up running out of memory
    img = corona_pic.subsample(4)  # mechanically, here it is adjusted
    photo_icon = Label(world_frame, image=img, bg="#fae7cb")
    photo_icon.configure(textvariable=img)
    photo_icon.place(x=1300, y=20)

    # total confirmed cases label and data

    total_confirmed_label = Label(world_frame, text="Total Confirmed Cases", font=universal_font, bg="#fae7cb",
                                  fg="black")
    total_confirmed_label.place(x=300, y=50)

    total_confirmed_data = Label(world_frame, text=covid.get_total_confirmed_cases(), font=universal_font, bg="#fae7cb",
                                 fg="black")
    total_confirmed_data.place(x=370, y=100)

    # total deaths

    total_deaths_label = Label(world_frame, text="Total Deaths", font=universal_font, bg="#fae7cb", fg="black")
    total_deaths_label.place(x=700, y=50)

    total_deaths_data = Label(world_frame, text=covid.get_total_deaths(), font=universal_font, bg="#fae7cb", fg="#c70039")
    total_deaths_data.place(x=725, y=100)

    # total recovered
    total_recovered_label = Label(world_frame, text="Total Recovered", font=universal_font, bg="#fae7cb", fg="black")
    total_recovered_label.place(x=1000, y=50)

    total_recovered_data = Label(world_frame, text=covid.get_total_recovered(), font=universal_font, bg="#fae7cb",
                                 fg="#21bf73")
    total_recovered_data.place(x=1050, y=100)

    # contry label data
    total_confirmed_country = Label(country_frame, text="Total Confirmed Cases", font=universal_font, bg="#204051",
                                    fg="white")
    total_confirmed_country.place(x=300, y=50)

    total_deaths_country = Label(country_frame, text="Total Deaths", font=universal_font, bg="#204051", fg="white")
    total_deaths_country.place(x=700, y=50)

    # total recovered
    total_recovered_country = Label(country_frame, text="Total Recovered", font=universal_font, bg="#204051",
                                    fg="white")
    total_recovered_country.place(x=1000, y=50)


frame1 = Frame(root, bg="#27496d", height=70)
frame1.pack(fill=X)

covid_title = Label(frame1, text="Coronavirus Live Tracker", font=universal_font, bg="#27496d", fg="white")
covid_title.pack()

world_frame = Frame(root, bg="#fae7cb", height=200)
world_frame.pack(fill=X)

country_frame = Frame(root, bg="#204051", height=200)
country_frame.pack(fill=X)

world_statistics()

total_countries = covid.list_countries()
total_countries.sort()

country_combobox = ttk.Combobox(country_frame, values=total_countries)
country_combobox.place(x=20, y=100)

country_name_label = Label(country_frame, text="Select Country", font=universal_font, bg="#204051", fg="white")
country_name_label.place(x=20, y=50)

total_confirmed_data = Label(country_frame, text="",
                             font=universal_font, bg="#204051", fg="white")
total_confirmed_data.place(x=370, y=100)
total_deaths_data = Label(country_frame, text="",
                          font=universal_font, bg="#204051", fg="#d63447")
total_deaths_data.place(x=750, y=100)
total_recovered_data = Label(country_frame, text="",
                             font=universal_font, bg="#204051", fg="#21bf73")
total_recovered_data.place(x=1050, y=100)

country_combobox.bind("<<ComboboxSelected>>", get_country)

info_frame = Frame(root, bg="#27496d", height=70)
info_frame.pack(fill=X)

time_label = Label(info_frame, bg="#27496d", fg="white", font=('Arial', 10, 'bold'))
time_label.place(x=5, y=15)

alert = Label(info_frame, text="#Stay Home, Stay Safe", bg="#27496d", fg="white", font=('Arial', 10, 'bold'))
alert.place(x=650, y=15)

dev = Label(info_frame, text="Developer: Sajjan Karn", bg="#27496d", fg="white", font=('Arial', 10, 'bold'))
dev.place(x=1300, y=15)

live_clock()

root.title("Coronavirus Tracker")
root.geometry("1500x500")
root.resizable(False, False)
root.iconbitmap("covid.ico")
root.mainloop()
