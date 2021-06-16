words=["laptop",'april','marvel','endgame','flames','vampire','vitamin','snacks','parrot','switzerland','chocolate','apple','grapes','carrot','cosmos','attendance','frappuccino','guinness','philippines','syllables','elephant','connecticut','psychology','manganese','autumn']

def labelSlider(): #function def for creating a slider for speedlabel
    global count,sliderwords #sets the scope to global
    text = 'Welcome to Typing Speed Tester Game!'
    if(count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    speedLabel.configure(text=sliderwords)
    speedLabel.after(150,labelSlider) #make random letter appear after some period of time

def time():
    global timer,score,miss
    if (timer >= 11):
        pass
    else:
        timerLabelCount.configure(fg='red')

    if(timer > 0):
        timer -= 1
        timerLabelCount.configure(text=timer)
        timerLabelCount.after(900,time)
    else:
        gameplayLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        mb = messagebox.askretrycancel('Notification','For playing again hit Retry')
        if(mb==True):
            score =0
            miss =0
            timer = 60
            timerLabelCount.configure(text=timer)
            WordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)

def startgame(event): #function for word entry
    global score,miss
    if (timer ==60):
        time()
    gameplayLabel.configure(text='')
    if(wordEntry.get() == WordLabel['text']):
        score+=1
        scoreLabelCount.configure(text=score)
    else:
        miss+=1


    random.shuffle(words) #shuffles all the words randomly
    WordLabel.configure(text=words[0]) #configures the words
    wordEntry.delete(0,END) #deletes the previous entered word


from tkinter import * # imports all functions and libraries of tkinter
import random #imports all functions and libraries of random
from tkinter import messagebox

############################################### Root Method

root = Tk() #creates screen
root.geometry('800x600+400+100') #displays the screen at the center according to the dimensions (width,height,rightshift,upshift)
root.configure(bg= 'mistyrose') #background color
root.title('speedtester') # title
root.iconbitmap(r'C:\Users\MARWAH\Downloads\speedtest.ico') #changes the icon

############################################## Variables

score=0
timer=60
count=0
sliderwords=''
miss=0

############################################## Label Method

speedLabel = Label(root,text="Welcome to Typing Speed Tester Game!",font=('arial',20,'italic bold'),bg='mistyrose',fg='navy')
speedLabel.place(x=120,y=30)
labelSlider() #calling the function

random.shuffle(words) # calling the shuffle function

WordLabel = Label(root,text=words[0],font=('arial',20,'bold'),bg='mistyrose',fg='chocolate')
WordLabel.place(x=330,y=300)

scoreLabel = Label(root,text="Your score :" ,font=('arial',20,'bold'),bg='mistyrose',fg='crimson')
scoreLabel.place(x=10,y=150)

scoreLabelCount = Label(root,text=score,font=('arial',15,'bold'),bg='mistyrose',fg='black')
scoreLabelCount.place(x=50,y=200)

timerLabel = Label(root,text="Time left :" ,font=('arial',20,'bold'),bg='mistyrose',fg='crimson')
timerLabel.place(x=600,y=150)

timerLabelCount = Label(root,text=timer,font=('arial',15,'bold'),bg='mistyrose',fg='Black')
timerLabelCount.place(x=650,y=200)

gameplayLabel = Label(root,text='Type Word and Hit Enter', font=('arial',15,'italic'),bg='mistyrose',fg='grey')
gameplayLabel.place(x=300,y=420)

############################################## Entry Method

wordEntry= Entry(root,font=('arial',20),bd=10,justify='center')
wordEntry.place(x=250,y=350)
wordEntry.focus_set() #sets the cursor without clicking on the entry box

###############################################

root.bind('<Return>',startgame) #binds event with the function
root.mainloop() # displays screen
