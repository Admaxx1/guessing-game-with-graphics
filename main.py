
import random
from tkinter import *
from tkinter import colorchooser
import pygame
import threading

print('By Admaxx1')

window = Tk()

setting_image = PhotoImage(file='setting.png')
on_switch = PhotoImage(file='switch-on.png')
off_switch = PhotoImage(file='switch-off.png')

window.title('Number guessing game')

color = colorchooser

window.geometry('600x400')

label_numbers = Label(window,text='Guess a number between 1-10 (both included)',font=('Arial',20))
label_numbers.pack()
numbers = [0,1,2,3,4,5,6,7,8,9,10]
number = random.choice(numbers)

def guess():
   global number
   try:
    def play_again():
        global number
        button_submit.config(text='SUBMIT',command=guess)
        label_numbers.config(text='Guess a number between 0-10 (both included)')
        entry.config(state=NORMAL)
        entry.delete(0,END)


    if int(entry.get()) == int(number):

        label_numbers.config(text='YOU ARE CORRECT!!!!!')
        pygame.mixer.init()
        pygame.mixer.music.load('success-fanfare-trumpets-6185.mp3')
        pygame.mixer.music.play(loops=0)
        entry.config(state=DISABLED)
        number = random.choice(numbers)
        button_submit.config(text='PLAY AGAIN', command=play_again)
    else:
        label_numbers.config(text="That's wrong!")
        entry.config(state=DISABLED)
        button_submit.config(text='PLAY AGAIN',command=play_again)
    if int(entry.get()) > 10 or int(entry.get()) < 0:
        label_numbers.config(text='PLEASE CHOOSE A NUMBER IN THE RANGE')
        entry.config(state=DISABLED)
        button_submit.config(text='PLAY AGAIN', command=play_again)
   except ValueError:
       label_numbers.config(text='Please write in an Integer')
       entry.config(state=DISABLED)
       button_submit.config(text='PLAY AGAIN', command=play_again)

def change_color():
    changed_color = color.askcolor()[1]
    window.config(bg=changed_color)

def bg_music():



    pygame.init()
    pygame.mixer.music.load('price-of-freedom-33106.mp3')
    pygame.mixer.music.play(loops=1000)

music = threading.Thread(target=bg_music())
music.start()


entry= Entry(window,width=20,font=('consolas',20),bg='light yellow')
entry.pack()
entry.insert(True,'Type in here')


button_submit=Button(window,text='SUBMIT',
                     font=('comic sans',20),bg='black',
                     fg='lime',activeforeground='lime',
                     activebackground='black',
                     command=guess)
button_submit.pack()

change_color_button = Button(window,text='change background color',
                     font=('comic sans',20),bg='pink',
                     fg='black',activeforeground='black',
                     activebackground='pink',
                     command=change_color)
change_color_button.pack(pady=30)
color_switch = True

def settings():

    entry.pack_forget()
    button_submit.pack_forget()
    change_color_button.pack_forget()
    label_numbers.pack_forget()


    def switchon():

        on_switch_button.config(image=on_switch)
        pygame.init()
        pygame.mixer.music.load('price-of-freedom-33106.mp3')
        pygame.mixer.music.play(loops=1000)
        on_switch_button.config(command=switchoff)

    def switchoff():
        global bgmusic
        pygame.init()
        pygame.mixer.music.stop()
        on_switch_button.config(image=off_switch)
        on_switch_button.config(command=switchon)


    def color_switchon():
        global color_switch
        color_switch = True
        color_switchon_button.config(image=on_switch)
        color_switchon_button.config(command=color_switchoff)



    def color_switchoff():
        global bgmusic
        global color_switch
        color_switch=False
        color_switchon_button.config(image=off_switch)
        color_switchon_button.config(command=color_switchon)

    def close():
      if color_switch is True:
        label_numbers.pack()
        on_switch_button.place_forget()
        labelswitch.place_forget()
        entry.pack()
        button_submit.pack()
        change_color_button.pack(pady=30)

        close_button.place_forget()
        color_switchon_button.place_forget()
        labelswitch_color.place_forget()
      else:
          label_numbers.pack()
          on_switch_button.place_forget()
          labelswitch.place_forget()
          entry.pack()
          button_submit.pack()
          change_color_button.pack_forget()

          close_button.place_forget()
          color_switchon_button.place_forget()
          labelswitch_color.place_forget()



    close_button = Button(window,text='CLOSE',font=('Consolas',20),command= close)
    close_button.place(x=500,y=0)

    on_switch_button = Button(window, image=on_switch, borderwidth=0, command=switchoff)
    on_switch_button.place(x=260, y=7)

    if color_switch is True:
        color_switchon_button = Button(window, image=on_switch, borderwidth=0, command=color_switchoff)
        color_switchon_button.place(x=260, y=49)
    else:
        color_switchon_button = Button(window, image=off_switch, borderwidth=0, command=color_switchoff)
        color_switchon_button.place(x=260, y=49)



    labelswitch_color = Label(window, text='color button: ', font=('Arial', 20))
    labelswitch_color.place(x=0, y=42)
    labelswitch = Label(window,text='Background music: ',font=('Arial',20))
    labelswitch.place(x=0, y=0)



setting_button =Button(window,image=setting_image,borderwidth=0,command=settings)
setting_button.place(x=550,y=350)

change_color_button.pack(pady=30)

window.mainloop()







