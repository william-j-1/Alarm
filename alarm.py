import time
from datetime import datetime
from tkinter import *
global time


clock = Tk()
clock.title("alarm")
clock.geometry("800x400")
#hour_box=Entry(clock,width=20,borderwidth=10).grid(row=0,column=-0)



# Used to create the individual labels for the hour,minutes and seconds of the project
label_hour=Label(clock,text="hour").grid(row=1,column=0)
hour_enter= Label(clock,width=10,height=5)
hour_enter.grid(row=0,column=0)
label_minute=Label(clock,text="minute").grid(row=1,column=1)
minute_enter=Label(clock,width=10,height=5)
minute_enter.grid(row=0,column=1)
label_second=Label(clock,text="seconds").grid(row=1,column=2)
second_enter=Label(clock,width=10,height=5)
second_enter.grid(row=0,column=2)

#used to constantly update the time and give the impression to the user
def Time_change():

    live_time = datetime.now()
    global hour
    hour=live_time.hour
    global minute
    minute=live_time.minute
    second=live_time.second
    hour_enter.config(text=hour)
    minute_enter.config(text=minute)
    second_enter.config(text=second)
    second_enter.after(20,Time_change)
Time_change()
hello="hello"

hour_counter= 0

minute_counter= 0
# used to increase the hour on the screen when it reaches
def increase_hour():
    global hour_counter
    hour_counter = hour_counter + 1
    if hour_counter>= 24:
        hour_counter = 0
    alarm_hour.delete(0,END)
    alarm_hour.insert(INSERT,hour_counter)


def increase_minute():
    global minute_counter
    minute_counter += 1
    if minute_counter>= 60:
        minute_counter = 0

    alarm_minute.delete(0,END)
    alarm_minute.insert(INSERT,minute_counter)
# used to set the alarm at the correct time
def submit():
    global Minute_time_to
    global Hour_time_to
    Minute_time_to = alarm_minute.get()
    Hour_time_to = alarm_hour.get()
    name =True
    while (name):
        live_alarm_time= datetime.now()
        live_alarm_time_hour=live_alarm_time.hour
        live_alarm_time_minute=live_alarm_time.minute
        time.sleep(30)

        current_minute = minute
        current_hour = hour
        #
        if live_alarm_time_minute == Minute_time_to and live_alarm_time_hour == Hour_time_to:
            print("hello")






alarm_hour_label=Label(clock,text="hour").grid(row=3,column=0)
alarm_hour=Entry(text=hour_counter)
alarm_hour.grid(row=2,column=0)

alarm_minute_label=Button(clock,text="minute").grid(row=3,column=1)
alarm_minute=Entry(clock)
alarm_minute.grid(row=2,column=1)

hour_increase_button=Button(clock,width=15,text="increase by hour",command=lambda:increase_hour())
hour_increase_button.grid(row=4,column=0)
minute_increase_button=Button(clock,width=15,text="increase by minute",command=lambda:increase_minute())
minute_increase_button.grid(row=4,column=1)


submit_button=Button(clock,width=15,text="submit",command=lambda:submit())
submit_button.grid(row=4,column=2)



clock.mainloop()




