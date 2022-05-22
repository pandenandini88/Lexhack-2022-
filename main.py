import random, time, tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from replit import audio

#from playsound import playsound


sound_file = 'the_calm_alarm.wav'

"""
# functions 
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    extra_time = input("Time's up! Are you done with your task?")
    extra_time = extra_time.lower()
    while extra_time == "no":
        t = input("How much more time do you need?? ")
        t = int(t)*60
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
            
        extra_time = input("Time's up! Are you done with your task?")
        extra_time = extra_time.lower()
      
      
  
#variables for countdown

  
# input time in seconds
#t = input("Enter the time in minutes: ")
#t = int(t) * 60
  
function call
countdown(t)"""

#variable setup

task_list = []

task_length = []

total_coins = 0

current_task = 0

#downtime arrays
downtime_list10 = [
    "Scrolling on social media for 10 mins", "Go on a brief walk",
    "listen to music for 10 mins"
]
downtime_list20 = [
    "Watch half-hour episode of shows", "Hang with friends",
    "drive for half an hour"
]
downtime_list40 = [
    "1h on video games", "1 episode of 1h show/movie",
    "Watch 2 episodes of half-hour show", "Nap for 1h"
]

downtime_list_full = []


def downtime():
    downtime_list_full.append(random.choice(downtime_list10))
    downtime_list_full.append(random.choice(downtime_list20))
    downtime_list_full.append(random.choice(downtime_list40))
    print(downtime_list_full)
    #buttons
    btn10 = Button(root, text=downtime_list_full[0] + " (10 Points)", bd='5',command=down10)
    btn10.place(x=10, y=500)
    btn10.pack_forget()
    btn10.pack(pady=20)
 
    btn20 = Button(root, text=downtime_list_full[1] + " (20 Points)", bd='5',command=down20)
    btn20.place(x=50, y=300)
    btn20.pack_forget()
    btn20.pack(pady=20)
  
    btn40 = Button(root, text=downtime_list_full[2] + " (40 points)", bd='5',command=down40)
    btn40.place(x=100, y=300)
    btn40.pack_forget()
    btn40.pack(pady=20)
    
    if total_coins < 40:
      btn40['state'] = DISABLED

    if total_coins < 20:
      btn20['state'] = DISABLED




  
#downtime timers
def down10():
  global total_coins
  total_coins -= 10
  countdown_extra_time(10)

def down20():
  global total_coins
  total_coins -= 20
  countdown_extra_time(30)
  
def down40():
  global total_coins
  total_coins -= 40
  countdown_extra_time(60)
  
"""#input system for tasks
answer = input("What needs to be done today? Enter to end list!")
while answer != "":
  task_list.append(answer)
  answer = input("What needs to be done today? Enter to end list!")

for i in range(len(task_list)):
  task_length.append(int(input("How many minutes are required for \""+task_list[i]+"\"?")))
"""
# creating Tk window
root = tkinter.Tk()
# setting geometry of tk window
root.geometry("300x250")

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Time Counter")

#frame for coins label
#total coins label
Upper_right = Label(root,text = total_coins)
Upper_right.place(relx = 1.0, rely = 0.0, anchor ='ne')

#tasklist
def tasking():
  tasks = input("Enter the number of items you want to complete today: ")
  inttasks = int(tasks)
  tasklist = [None] * inttasks
#task_length = [0] * inttasks

  pri = 1

  for i in range(0, inttasks):
      tasklist.append(input("#" + str(pri) + " priority item: "))
      task_length.append(input("How much time will this item take (minutes): "))
      pri+=1
  for x in range(len(task_list)):
      countdown(task_length[x])

#interface window
btnNew = Button(root, text='New Task', bd='5', command=tasking)
btnNew.pack_forget()
btnNew.place(x=100, y=144)
btnNew.pack(pady=20)
# Declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()


def countdown(total_minutes):

    # setting the default value as 0
    hour.set("00")
    minute.set(str(total_minutes))
    second.set("00")

    # Use of Entry class to take input from the user
    hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
    hourEntry.place(x=80, y=20)

    minuteEntry = Entry(root,
                        width=3,
                        font=("Arial", 18, ""),
                        textvariable=minute)
    minuteEntry.place(x=130, y=20)

    secondEntry = Entry(root,
                        width=3,
                        font=("Arial", 18, ""),
                        textvariable=second)
    secondEntry.place(x=180, y=20)

    btn = Button(root, text='Set Time Countdown', bd='5', command=submit)
    btnNew.pack_forget()
    btn.place(x=70, y=120)
    btnNew.pack(pady=20)


def submit():
    global total_coins
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(
            second.get())
    except:
        print("Please input the right value")
    while temp > -1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours = 0
        if mins > 60:

            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            timer_end()
            
            


# after every one sec the value of temp will be decremented
# by one
        temp -= 1


# button widget


def timer_end():
  global total_coins, total_time
  #playsound(sound_file)
  #source = audio.play_file("the_calm_alarm.mp3")
  messagebox.showinfo("Time Countdown", "Time's up ")
  """
  need_time = input("Do you need more time? ")
  need_time = need_time.lower()
  while need_time == yes:
    more_time = int(input("How much more time do you need?"))
    hour.set("00")
    minute.set(str(more_time))
    second.set("00")
  """
  
  
  extra_time = input("Do you need extra time? ")
  extra_time = extra_time.lower()
  while extra_time == "yes":
    more_time = int(input("How much more time do you need? "))
    countdown_extra_time(more_time)
    extra_time = input("Do you need extra time? ")
    extra_time = extra_time.lower()
    
  
  total_time = int(input("How many minutes did that task take you? "))
  
  total_coins += total_time
  print(total_coins)
  if total_coins >= 10:
    downtime()
  
  #extra time
  else:
      btnContinue = Button(root, text='Want To Start a New task?',       
      bd='5', command=tasking)
      btnContinue.pack_forget()
      btnContinue.place(x=100, y=144)
      btnContinue.pack(pady=20) 


def countdown_extra_time(total_minutes):
  # setting the default value as 0
  hour.set("00")
  minute.set(str(total_minutes))
  second.set("00")

  # Use of Entry class to take input from the user
  hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
  hourEntry.place(x=80, y=20)

  minuteEntry = Entry(root,
                      width=3,
                      font=("Arial", 18, ""),
                      textvariable=minute)
  minuteEntry.place(x=130, y=20)

  secondEntry = Entry(root,
                     width=3,
                      font=("Arial", 18, ""),
                      textvariable=second)
  secondEntry.place(x=180, y=20)
  submit_extra_time()
  """btn = Button(root, text='Set Time Countdown', bd='5', command=submit_extra_time)
  btnNew.pack_forget()
  btn.place(x=70, y=120)
  btnNew.pack(pady=20)"""

def submit_extra_time():
  try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(
            second.get())
  except:
        print("Please input the right value")
  while temp > -1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours = 0
        if mins > 60:

            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            #playsound(sound_file)
            #source = audio.play_file("the_calm_alarm.mp3")
            messagebox.showinfo("Time Countdown", "Time's up ")
            
            


        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


"""for x in range(len(task_list)):
  countdown(task_length[x])"""
# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()
