from tkinter import*
from tkinter import messagebox
import winsound
import time
import movie
import music
import science
import logic
#=========colour mode========
#c6a66d
#d2be83
#B35900
#e1671a
#f7e171
#========Create GUI==========
root=Tk()

#==============GUI window music============
winsound.PlaySound("Lightfox - Pluck  .wav",winsound.SND_ASYNC+winsound.SND_LOOP)

#==============GUI window title============
root.title('Try My Riddle !')

#==============GUI window icon============
root.iconbitmap("App icon.ico")

#==============GUI window background============
bg=PhotoImage(file="appcolour.png")
cover=Label(root,image=bg,bd=0)
cover.place(x=0, y=0)
name=""
ID=""
while name!="Ng Jing Ping" :
    name=input("Enter Your Name:")
while ID!="101211418":
    ID=input("Enter Your ID Number:")
#===write (replace) data into the text file "report.txt"===============
file=open("report.txt","w")
file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file.write("\n                   Welcome to Try My Riddle!                   \n")
file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file.write("\nApplication report:\n")
file.write("This application have 80 questions in four categories.\n")
file.write("Four categories included Logic, Science, Music, Movie.\n")
file.write("Each categories have 20 questions.\n")
file.write("Created by Syntaxo\n")
file.write("Created by Aynsley Aaron Chong & Ng Jing Ping\n")
file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file.write("\nLogic Question:\n")
file.write("The Answer for Question  1 is A Clock\n")
file.write("The Answer for Question  2 is Short\n")
file.write("The Answer for Question  3 is Envelop\n")
file.write("The Answer for Question  4 is A Bottle\n")
file.write("The Answer for Question  5 is Post Office\n")
file.write("The Answer for Question  6 is An Egg\n")
file.write("The Answer for Question  7 is All Months\n")
file.write("The Answer for Question  8 is Trouble\n")
file.write("The Answer for Question  9 is Seven\n")
file.write("The Answer for Question 10 is W\n")
file.write("The Answer for Question 11 is Doorbell\n")
file.write("The Answer for Question 12 is Incorrectly\n")
file.write("The Answer for Question 13 is Sponge\n")
file.write("The Answer for Question 14 is Dictionary\n")
file.write("The Answer for Question 15 is Relationship\n")
file.write("The Answer for Question 16 is Your Age\n")
file.write("The Answer for Question 17 is Table\n")
file.write("The Answer for Question 18 is Add Letter G\n")
file.write("The Answer for Question 19 is Riverbank\n")
file.write("The Answer for Question 20 is V\n")
file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file.write("\nScience Question:\n")
file.write("The Answer for Question  1 is Elbert Einstein\n")
file.write("The Answer for Question  2 is Mercury\n")
file.write("The Answer for Question  3 is Esophagus\n")
file.write("The Answer for Question  4 is Thermoplastic\n")
file.write("The Answer for Question  5 is Coal\n")
file.write("The Answer for Question  6 is Atomic Number\n")
file.write("The Answer for Question  7 is Photosynthesis\n")
file.write("The Answer for Question  8 is Sodium Chloride\n")
file.write("The Answer for Question  9 is Mercury\n")
file.write("The Answer for Question 10 is Carbon Dioxide\n")
file.write("The Answer for Question 11 is Helium\n")
file.write("The Answer for Question 12 is Iron\n")
file.write("The Answer for Question 13 is Barometer\n")
file.write("The Answer for Question 14 is Oxygen And Hydrogen\n")
file.write("The Answer for Question 15 is Vitamin D\n")
file.write("The Answer for Question 16 is Tongue\n")
file.write("The Answer for Question 17 is Carbon Dioxide\n")
file.write("The Answer for Question 18 is Bone Marrow\n")
file.write("The Answer for Question 19 is Copper And Tin\n")
file.write("The Answer for Question 20 is White\n")
file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file.write("\nMusic Question:\n")
file.write("The Answer for Question  1 is Demi Lovato\n")
file.write("The Answer for Question  2 is Owl City\n")
file.write("The Answer for Question  3 is Katy Perry\n")
file.write("The Answer for Question  4 is Justin Bieber\n")
file.write("The Answer for Question  5 is Maroon 5\n")
file.write("The Answer for Question  6 is 2013\n")
file.write("The Answer for Question  7 is Halsey\n")
file.write("The Answer for Question  8 is Umbrella\n")
file.write("The Answer for Question  9 is Shape Of You\n")
file.write("The Answer for Question 10 is Katy Perry\n")
file.write("The Answer for Question 11 is Something Just Like This\n")
file.write("The Answer for Question 12 is Canadian\n")
file.write("The Answer for Question 13 is Thinking out Loud\n")
file.write("The Answer for Question 14 is Beyonce\n")
file.write("The Answer for Question 15 is Symphony\n")
file.write("The Answer for Question 16 is Can’t stop the feeling\n")
file.write("The Answer for Question 17 is New Kids On The Block\n")
file.write("The Answer for Question 18 is Adam Levine\n")
file.write("The Answer for Question 19 is The Beatles\n")
file.write("The Answer for Question 20 is Grenade\n")
file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file.write("\nMovie Question:\n")
file.write("The Answer for Question  1 is Mystique\n")
file.write("The Answer for Question  2 is It\n")
file.write("The Answer for Question  3 is Oasis\n")
file.write("The Answer for Question  4 is San Andreas\n")
file.write("The Answer for Question  5 is Suicide Squad\n")
file.write("The Answer for Question  6 is Henry Cavill\n")
file.write("The Answer for Question  7 is Wade Wilson\n")
file.write("The Answer for Question  8 is Horror\n")
file.write("The Answer for Question  9 is Finding Nemo\n")
file.write("The Answer for Question 10 is Alice In Wonderland\n")
file.write("The Answer for Question 11 is Monster Inc\n")
file.write("The Answer for Question 12 is Fiona\n")
file.write("The Answer for Question 13 is Roger Moore\n")
file.write("The Answer for Question 14 is Toto\n")
file.write("The Answer for Question 15 is Frodo Baggins\n")
file.write("The Answer for Question 16 is Sixth Sense\n")
file.write("The Answer for Question 17 is Toys Story\n")
file.write("The Answer for Question 18 is Donkey\n")
file.write("The Answer for Question 19 is Pixar\n")
file.write("The Answer for Question 20 is Star Wars\n")
file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
file.write("                       User   Report                            \n")
file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#===write (append) data into the text file "report.txt"===============
#input your name
file.write("\nUsername: Ng Jing Ping")
#input your ID
file.write("\nID:101211418")
file.write("\nYou open at ")
file.close()
file=open("report.txt","a")
named_tupled = time.localtime() # get struct_time
timereport= time.strftime("%d %b %Y %I:%M:%S %p", named_tupled)
file.write(timereport)
file.write(" before.")
file.close()

#=========Print Detail info==========
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                  Welcome to Try My Riddle!                    ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Enjoy......")
named_tuple = time.localtime() # get struct_time
timenow = time.strftime("%d %b %Y %I:%M:%S %p", named_tuple)
print("Time now is", timenow)
print("Created by Syntaxo")
print("Created by Aynsley Aaron Chong & Ng Jing Ping")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def brek():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def correct():
    print("Congratulations!")
    print("Your guess is correct.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def wrong():
    print("Try agian!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
#========================================================Detail info==============================================================================
#====import or get the information form the text file "about.txt"===============
file=open("about.txt","r")
info=file.read()
file.close()

#========================================================Time=====================================================================================
localtime=time.asctime(time.localtime(time.time()))

#==============================================================Display============================================================================
#===logic====
#Frame
#Question
#Answer
x=[]
def logics2():
    m11=[]
    def check11():
        msg=x
        v=100
        guess=Entry_eleven.get()
        user_guess=guess.title()
        Entry_eleven.delete(0 ,END)
        guesscount=m11
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Doorbell":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.eleven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 11 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.eleven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m12=[]
    def check12():
        msg=x
        v=100
        guess=Entry_twelve.get()
        user_guess=guess.title()
        Entry_twelve.delete(0 ,END)
        guesscount=m12
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Incorrectly":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.twelve()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 12 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.twelve()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m13=[]
    def check13():
        msg=x
        v=100
        guess=Entry_thirteen.get()
        user_guess=guess.title()
        Entry_thirteen.delete(0 ,END)
        guesscount=m13
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Sponge":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.thirteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 13 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.thirteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m14=[]
    def check14():
        msg=x
        v=100
        guess=Entry_fourteen.get()
        user_guess=guess.title()
        Entry_fourteen.delete(0 ,END)
        guesscount=m14
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Dictionary":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.fourteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 14 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.fourteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m15=[]
    def check15():
        msg=x
        v=100
        guess=Entry_fifteen.get()
        user_guess=guess.title()
        Entry_fifteen.delete(0 ,END)
        guesscount=m15
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Relationship":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.fifteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 15 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.fifteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m16=[]
    def check16():
        msg=x
        v=100
        guess=Entry_sixteen.get()
        user_guess=guess.title()
        Entry_sixteen.delete(0 ,END)
        guesscount=m16
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Your Age":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.sixteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 16 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.sixteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m17=[]
    def check17():
        msg=x
        v=100
        guess=Entry_seventeen.get()
        user_guess=guess.title()
        Entry_seventeen.delete(0 ,END)
        guesscount=m17
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Table":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.seventeen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 17 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.seventeen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m18=[]
    def check18():
        msg=x
        v=100
        guess=Entry_eighteen.get()
        user_guess=guess.title()
        Entry_eighteen.delete(0 ,END)
        guesscount=m18
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Add Letter G":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.eighteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 18 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.eighteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m19=[]
    def check19():
        msg=x
        v=100
        guess=Entry_nineteen.get()
        user_guess=guess.title()
        Entry_nineteen.delete(0 ,END)
        guesscount=m19
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Riverbank":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.nineteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 19 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.nineteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m20=[]
    def check20():
        msg=x
        v=100
        guess=Entry_twenty.get()
        user_guess=guess.title()
        Entry_twenty.delete(0 ,END)
        guesscount=m20
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="V":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.twenty()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 20 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.twenty()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return
            
    lgs=StringVar()
    clo_8=PhotoImage(file="close display.png")
    closeimage8=Label(root,image=clo_8,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    closeimage8.place(x=400,y=0)
    log2=Frame(root,bg="#c6a66d",relief=SUNKEN)
    log2.place(x=400,y=0)
    label_2=Label(log2,text=" Logic   :",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d")
    label_2.grid(row=0,column=0,sticky=W) 
    lgscore=Label(root,text="Score",font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    lgscore.place(x=0,y=500)
    backlg=Button(root,text="Back",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d",command=logics)
    backlg.place(x=1000,y=600)
    numlgscore=Label(root,textvariable=lgs,font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    numlgscore.place(x=0,y=600)
    Question_eleven=Label(log2,text="11.What never asks questions but is often answered?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_eleven.grid(row=1,columnspan=10,sticky=W)
    Answer_eleven=Label(log2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_eleven.grid(row=2,column=0)
    Entry_eleven=Entry(log2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_eleven.grid(row=2,column=1)
    check11=Button(log2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check11)
    check11.grid(row=2,column=2)
    Question_twelve=Label(log2,text="12.Which word in the dictionary is spelled incorrectly?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_twelve.grid(row=3,columnspan=10,sticky=W)
    Answer_twelve=Label(log2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_twelve.grid(row=4,column=0)
    Entry_twelve=Entry(log2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_twelve.grid(row=4,column=1)
    check12=Button(log2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check12)
    check12.grid(row=4,column=2)
    Question_thirteen=Label(log2,text="13.Whats full of holes but still holds water?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_thirteen.grid(row=5,columnspan=10,sticky=W)
    Answer_thirteen=Label(log2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_thirteen.grid(row=6,column=0)
    Entry_thirteen=Entry(log2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_thirteen.grid(row=6,column=1)
    check13=Button(log2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check13)
    check13.grid(row=6,column=2)
    Question_fourteen=Label(log2,text="14.Where does Friday come before Thursday?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_fourteen.grid(row=7,columnspan=10,sticky=W)
    Answer_fourteen=Label(log2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_fourteen.grid(row=8,column=0)
    Entry_fourteen=Entry(log2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_fourteen.grid(row=8,column=1)
    check14=Button(log2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check14)
    check14.grid(row=8,column=2)
    Question_fifteen=Label(log2,text="15.What ship has two mates, but no captain?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_fifteen.grid(row=9,columnspan=10,sticky=W)
    Answer_fifteen=Label(log2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_fifteen.grid(row=10,column=0)
    Entry_fifteen=Entry(log2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_fifteen.grid(row=10,column=1)
    check15=Button(log2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check15)
    check15.grid(row=10,column=2)
    Question_sixteen=Label(log2,text="16.What goes up but never goes down?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_sixteen.grid(row=11,columnspan=10,sticky=W)
    Answer_sixteen=Label(log2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_sixteen.grid(row=12,column=0)
    Entry_sixteen=Entry(log2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_sixteen.grid(row=12,column=1)
    check16=Button(log2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check16)
    check16.grid(row=12,column=2)
    Question_seventeen=Label(log2,text="17.What has four legs, but can't walk?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_seventeen.grid(row=13,columnspan=10,sticky=W)
    Answer_seventeen=Label(log2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_seventeen.grid(row=14,column=0)
    Entry_seventeen=Entry(log2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_seventeen.grid(row=14,column=1)
    check17=Button(log2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check17)
    check17.grid(row=14,column=2)
    Question_eighteen=Label(log2,text="18.How you make the number one disappear?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_eighteen.grid(row=15,columnspan=10,sticky=W)
    Answer_eighteen=Label(log2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_eighteen.grid(row=16,column=0)
    Entry_eighteen=Entry(log2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_eighteen.grid(row=16,column=1)
    check18=Button(log2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check18)
    check18.grid(row=16,column=2)
    Question_nineteen=Label(log2,text="19.What bank never has any money?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_nineteen.grid(row=17,columnspan=10,sticky=W)
    Answer_nineteen=Label(log2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_nineteen.grid(row=18,column=0)
    Entry_nineteen=Entry(log2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_nineteen.grid(row=18,column=1)
    check19=Button(log2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check19)
    check19.grid(row=18,column=2)
    Question_twenty=Label(log2,text="20.What is the center of gravity?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_twenty.grid(row=19,columnspan=10,sticky=W)
    Answer_twenty=Label(log2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_twenty.grid(row=20,column=0)
    Entry_twenty=Entry(log2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_twenty.grid(row=20,column=1)
    check20=Button(log2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check20)
    check20.grid(row=20,column=2)

x=[]
def logics():
    x.clear()
    print("Welome back to logic categories")
    brek()
    m=[]
    def check1():
        msg=x
        v=100
        guess=Entry_one.get()
        user_guess=guess.title()
        Entry_one.delete(0 ,END)
        guesscount=m
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="A Clock":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.one()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 1 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.one()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return
            
            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return
            
    m2=[]
    def check2():
        msg=x
        v=100
        guess=Entry_two.get()
        user_guess=guess.title()
        Entry_two.delete(0 ,END)
        guesscount=m2
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Short":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.two()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 2 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.two()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return
            
            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m3=[]
    def check3():
        msg=x
        v=100
        guess=Entry_three.get()
        user_guess=guess.title()
        Entry_three.delete(0 ,END)
        guesscount=m3
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Envelop":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.three()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 3 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.three()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return
            
    m4=[]
    def check4():
        msg=x
        v=100
        guess=Entry_four.get()
        user_guess=guess.title()
        Entry_four.delete(0 ,END)
        guesscount=m4
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="A Bottle":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.four()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 4 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.four()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m5=[]
    def check5():
        msg=x
        v=100
        guess=Entry_five.get()
        user_guess=guess.title()
        Entry_five.delete(0 ,END)
        guesscount=m5
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Post Office":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.five()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 5 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return

                else:
                    logic.five()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m6=[]
    def check6():
        msg=x
        v=100
        guess=Entry_six.get()
        user_guess=guess.title()
        Entry_six.delete(0 ,END)
        guesscount=m6
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="An Egg":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.six()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 6 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.six()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m7=[]
    def check7():
        msg=x
        v=100
        guess=Entry_seven.get()
        user_guess=guess.title()
        Entry_seven.delete(0 ,END)
        guesscount=m7
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="All Months":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.seven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 7 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.seven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m8=[]
    def check8():
        msg=x
        v=100
        guess=Entry_eight.get()
        user_guess=guess.title()
        Entry_eight.delete(0 ,END)
        guesscount=m8
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Trouble":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.eight()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 8 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.eight()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m9=[]
    def check9():
        msg=x
        v=100
        guess=Entry_nine.get()
        user_guess=guess.title()
        Entry_nine.delete(0 ,END)
        guesscount=m9
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Seven":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.nine()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 9 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.nine()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m10=[]
    def check10():
        msg=x
        v=100
        guess=Entry_ten.get()
        user_guess=guess.title()
        Entry_ten.delete(0 ,END)
        guesscount=m10
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="W":
                    msg.append(v)
                    total=sum(msg)
                    s=total
                    lgs.set(s)
                    logic.ten()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at logic categories question 10 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    logic.ten()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return
            
    lgs=StringVar()
    lgs.set("0")
    clo_4=PhotoImage(file="close display.png")
    closeimage4=Label(root,image=clo_4,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    closeimage4.place(x=400,y=0)
    main_3=PhotoImage(file="scorebackground.png")
    mainimage3=Label(root,image=main_3,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    mainimage3.place(x=0,y=500)
    log=Frame(root,bg="#c6a66d",relief=SUNKEN)
    log.place(x=400,y=0)
    label_1=Label(log,text=" Logic   :",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d")
    label_1.grid(row=0,column=0,sticky=W) 
    lgscore=Label(root,text="Score",font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    lgscore.place(x=0,y=500)
    nextlg=Button(root,text="Next",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d",command=logics2)
    nextlg.place(x=1000,y=600)
    numlgscore=Label(root,textvariable=lgs,font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    numlgscore.place(x=0,y=600)
    Question_one=Label(log,text="1.What has a face and two hands but no arms or legs?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_one.grid(row=1,columnspan=10,sticky=W)
    Answer_one=Label(log,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_one.grid(row=2,column=0,)
    Entry_one=Entry(log,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_one.grid(row=2,column=1)
    check1=Button(log,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check1)
    check1.grid(row=2,column=2)
    Question_two=Label(log,text="2.What five-letter word becomes shorter when you add two letters to it?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_two.grid(row=3,columnspan=10,sticky=W)
    Answer_two=Label(log,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_two.grid(row=4,column=0)
    Entry_two=Entry(log,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_two.grid(row=4,column=1)
    check2=Button(log,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check2)
    check2.grid(row=4,column=2)
    Question_three=Label(log,text="3.What word begins and ends with an E but only has one word?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_three.grid(row=5,columnspan=10,sticky=W)
    Answer_three=Label(log,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_three.grid(row=6,column=0)
    Entry_three=Entry(log,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_three.grid(row=6,column=1)
    check3=Button(log,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check3)
    check3.grid(row=6,column=2)
    Question_four=Label(log,text="4.What has a neck but no head?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_four.grid(row=7,columnspan=10,sticky=W)
    Answer_four=Label(log,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_four.grid(row=8,column=0)
    Entry_four=Entry(log,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_four.grid(row=8,column=1)
    check4=Button(log,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check4)
    check4.grid(row=8,column=2)
    Question_five=Label(log,text="5.What starts with P, ends with E and has thousand of letters?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_five.grid(row=9,columnspan=10,sticky=W)
    Answer_five=Label(log,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_five.grid(row=10,column=0)
    Entry_five=Entry(log,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_five.grid(row=10,column=1)
    check5=Button(log,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check5)
    check5.grid(row=10,column=2)
    Question_six=Label(log,text="6.What has to be broken before you can use it?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_six.grid(row=11,columnspan=10,sticky=W)
    Answer_six=Label(log,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_six.grid(row=12,column=0)
    Entry_six=Entry(log,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_six.grid(row=12,column=1)
    check6=Button(log,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check6)
    check6.grid(row=12,column=2)
    Question_seven=Label(log,text="7.Which month has 28 days?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_seven.grid(row=13,columnspan=10,sticky=W)
    Answer_seven=Label(log,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_seven.grid(row=14,column=0)
    Entry_seven=Entry(log,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_seven.grid(row=14,column=1)
    check7=Button(log,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check7)
    check7.grid(row=14,column=2)
    Question_eight=Label(log,text="8.What is easy to get into, but hard to get out of?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_eight.grid(row=15,columnspan=10,sticky=W)
    Answer_eight=Label(log,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_eight.grid(row=16,column=0)
    Entry_eight=Entry(log,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_eight.grid(row=16,column=1)
    check8=Button(log,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check8)
    check8.grid(row=16,column=2)
    Question_nine=Label(log,text="9.I am an odd number. Take away one letter and I become even. What number am I?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_nine.grid(row=17,columnspan=10,sticky=W)
    Answer_nine=Label(log,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_nine.grid(row=18,column=0)
    Entry_nine=Entry(log,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_nine.grid(row=18,column=1)
    check9=Button(log,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check9)
    check9.grid(row=18,column=2)
    Question_ten=Label(log,text="10.What is at the end of a rainbow?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_ten.grid(row=19,columnspan=10,sticky=W)
    Answer_ten=Label(log,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_ten.grid(row=20,column=0)
    Entry_ten=Entry(log,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_ten.grid(row=20,column=1)
    check10=Button(log,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check10)
    check10.grid(row=20,column=2)            
               
#==science==
#Frame
#Question
#Answer
b=[]
def sciences2():
    m11=[]
    def check11():
        msg2=b
        v=100
        guess=Entry_eleven.get()
        user_guess=guess.title()
        Entry_eleven.delete(0 ,END)
        guesscount=m11
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Helium":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.eleven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 11 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                else:
                    science.eleven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m12=[]
    def check12():
        msg2=b
        v=100
        guess=Entry_twelve.get()
        user_guess=guess.title()
        Entry_twelve.delete(0 ,END)
        guesscount=m12
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Iron":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.twelve()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    msg2="0000"
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 12 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.twelve()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m13=[]
    def check13():
        msg2=b
        v=100
        guess=Entry_thirteen.get()
        user_guess=guess.title()
        Entry_thirteen.delete(0 ,END)
        guesscount=m13
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Barometer":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.thirteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 13 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.thirteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m14=[]
    def check14():
        msg2=b
        v=100
        guess=Entry_fourteen.get()
        user_guess=guess.title()
        Entry_fourteen.delete(0 ,END)
        guesscount=m14
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Oxygen And Hydrogen":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.fourteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 14 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.fourteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m15=[]
    def check15():
        msg2=b
        v=100
        guess=Entry_fifteen.get()
        user_guess=guess.title()
        Entry_fifteen.delete(0 ,END)
        guesscount=m15
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Vitamin D":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.fifteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 15 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.fifteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return
 
    m16=[]
    def check16():
        msg2=b
        v=100
        guess=Entry_sixteen.get()
        user_guess=guess.title()
        Entry_sixteen.delete(0 ,END)
        guesscount=m16
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Tongue":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.sixteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 16 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.sixteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m17=[]
    def check17():
        msg2=b
        v=100
        guess=Entry_seventeen.get()
        user_guess=guess.title()
        Entry_seventeen.delete(0 ,END)
        guesscount=m17
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Carbon Dioxide":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.seventeen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 17 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.seventeen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m18=[]
    def check18():
        msg2=b
        v=100
        guess=Entry_eighteen.get()
        user_guess=guess.title()
        Entry_eighteen.delete(0 ,END)
        guesscount=m18
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Bone Marrow":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.eighteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 18 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.eighteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m19=[]
    def check19():
        msg2=b
        v=100
        guess=Entry_nineteen.get()
        user_guess=guess.title()
        Entry_nineteen.delete(0 ,END)
        guesscount=m19
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Copper And Tin":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.nineteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 19 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.nineteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m20=[]
    def check20():
        msg2=b
        v=100
        guess=Entry_twenty.get()
        user_guess=guess.title()
        Entry_twenty.delete(0 ,END)
        guesscount=m20
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="White":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.twenty()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 20 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.twenty()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    scis=StringVar()
    clo_8=PhotoImage(file="close display.png")
    closeimage8=Label(root,image=clo_8,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    closeimage8.place(x=400,y=0)
    sci2=Frame(root,bg="#c6a66d",relief=SUNKEN)
    sci2.place(x=400,y=0)
    label_2=Label(sci2,text=" Science:",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d")
    label_2.grid(row=0,column=0,sticky=W) 
    sciscore=Label(root,text="Score",font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    sciscore.place(x=0,y=500)
    backsci=Button(root,text="Back",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d",command=sciences)
    backsci.place(x=1000,y=600)
    numsciscore=Label(root,textvariable=scis,font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    numsciscore.place(x=0,y=600)
    Question_eleven=Label(sci2,text="11.Which element has atomic number 2 ?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_eleven.grid(row=1,columnspan=10,sticky=W)
    Answer_eleven=Label(sci2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_eleven.grid(row=2,column=0)
    Entry_eleven=Entry(sci2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_eleven.grid(row=2,column=1)
    check11=Button(sci2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check11)
    check11.grid(row=2,column=2)
    Question_twelve=Label(sci2,text="12.Which metal makes the strongest magnets?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_twelve.grid(row=3,columnspan=10,sticky=W)
    Answer_twelve=Label(sci2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_twelve.grid(row=4,column=0)
    Entry_twelve=Entry(sci2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_twelve.grid(row=4,column=1)
    check12=Button(sci2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check12)
    check12.grid(row=4,column=2)
    Question_thirteen=Label(sci2,text="13.What device is used to measure air pressure?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_thirteen.grid(row=5,columnspan=10,sticky=W)
    Answer_thirteen=Label(sci2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_thirteen.grid(row=6,column=0)
    Entry_thirteen=Entry(sci2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_thirteen.grid(row=6,column=1)
    check13=Button(sci2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check13)
    check13.grid(row=6,column=2)
    Question_fourteen=Label(sci2,text="14.Which two elements make up water?",font = ('Times',13,"bold"),fg="#B35900",bg="#c6a66d")
    Question_fourteen.grid(row=7,columnspan=10,sticky=W)
    Answer_fourteen=Label(sci2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_fourteen.grid(row=8,column=0)
    Entry_fourteen=Entry(sci2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_fourteen.grid(row=8,column=1)
    check14=Button(sci2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check14)
    check14.grid(row=8,column=2)
    Question_fifteen=Label(sci2,text="15.Which vitamin does sunlight provide to humans?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_fifteen.grid(row=9,columnspan=10,sticky=W)
    Answer_fifteen=Label(sci2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_fifteen.grid(row=10,column=0)
    Entry_fifteen=Entry(sci2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_fifteen.grid(row=10,column=1)
    check15=Button(sci2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check15)
    check15.grid(row=10,column=2)
    Question_sixteen=Label(sci2,text="16.What is the most strongest muscle in the human body?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_sixteen.grid(row=11,columnspan=10,sticky=W)
    Answer_sixteen=Label(sci2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_sixteen.grid(row=12,column=0)
    Entry_sixteen=Entry(sci2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_sixteen.grid(row=12,column=1)
    check16=Button(sci2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check16)
    check16.grid(row=12,column=2)
    Question_seventeen=Label(sci2,text="17.Which gas do plants absorb from the atmosphere?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_seventeen.grid(row=13,columnspan=10,sticky=W)
    Answer_seventeen=Label(sci2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_seventeen.grid(row=14,column=0)
    Entry_seventeen=Entry(sci2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_seventeen.grid(row=14,column=1)
    check17=Button(sci2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check17)
    check17.grid(row=14,column=2)
    Question_eighteen=Label(sci2,text="18.Where are red blood cells made?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_eighteen.grid(row=15,columnspan=10,sticky=W)
    Answer_eighteen=Label(sci2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_eighteen.grid(row=16,column=0)
    Entry_eighteen=Entry(sci2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_eighteen.grid(row=16,column=1)
    check18=Button(sci2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check18)
    check18.grid(row=16,column=2)
    Question_nineteen=Label(sci2,text="19.Which two metals have to be combined to make bronze?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_nineteen.grid(row=17,columnspan=10,sticky=W)
    Answer_nineteen=Label(sci2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_nineteen.grid(row=18,column=0)
    Entry_nineteen=Entry(sci2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_nineteen.grid(row=18,column=1)
    check19=Button(sci2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check19)
    check19.grid(row=18,column=2)
    Question_twenty=Label(sci2,text="20.What colour blood cells defend our bodies against illness?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_twenty.grid(row=19,columnspan=10,sticky=W)
    Answer_twenty=Label(sci2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_twenty.grid(row=20,column=0)
    Entry_twenty=Entry(sci2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_twenty.grid(row=20,column=1)
    check20=Button(sci2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check20)
    check20.grid(row=20,column=2)
    
b=[]
def sciences():
    b.clear()
    print("Welome back to science categories")
    brek()
    m1=[]
    def check1():
        msg2=b
        v=100
        guess=Entry_one.get()
        user_guess=guess.title()
        Entry_one.delete(0 ,END)
        guesscount=m1
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Elbert Einstein":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.one()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 1 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.one()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m2=[]
    def check2():
        msg2=b
        v=100
        guess=Entry_two.get()
        user_guess=guess.title()
        Entry_two.delete(0 ,END)
        guesscount=m2
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Mercury":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.two()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 2 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.two()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m3=[]
    def check3():
        msg2=b
        v=100
        guess=Entry_three.get()
        user_guess=guess.title()
        Entry_three.delete(0 ,END)
        guesscount=m3
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Esophagus":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.three()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 3 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.three()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m4=[]
    def check4():
        msg2=b
        v=100
        guess=Entry_four.get()
        user_guess=guess.title()
        Entry_four.delete(0 ,END)
        guesscount=m4
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Thermoplastic":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.four()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 4 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.four()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m5=[]
    def check5():
        msg2=b
        v=100
        guess=Entry_five.get()
        user_guess=guess.title()
        Entry_five.delete(0 ,END)
        guesscount=m5
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Coal":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.five()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 5 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.five()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m6=[]
    def check6():
        msg2=b
        v=100
        guess=Entry_six.get()
        user_guess=guess.title()
        Entry_six.delete(0 ,END)
        guesscount=m6
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Atomic Number":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.six()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 6 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.six()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m7=[]
    def check7():
        msg2=b
        v=100
        guess=Entry_seven.get()
        user_guess=guess.title()
        Entry_seven.delete(0 ,END)
        guesscount=m7
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Photosynthesis":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.seven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 7 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.seven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m8=[]
    def check8():
        msg2=b
        v=100
        guess=Entry_eight.get()
        user_guess=guess.title()
        Entry_eight.delete(0 ,END)
        guesscount=m8
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Sodium Chloride":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.eight()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 8 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.eight()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m9=[]
    def check9():
        msg2=b
        v=100
        guess=Entry_nine.get()
        user_guess=guess.title()
        Entry_nine.delete(0 ,END)
        guesscount=m9
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Mercury":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.nine()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 9 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.nine()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m10=[]
    def check10():
        msg2=b
        v=100
        guess=Entry_ten.get()
        user_guess=guess.title()
        Entry_ten.delete(0 ,END)
        guesscount=m10
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Carbon Dioxide":
                    msg2.append(v)
                    total=sum(msg2)
                    s=total
                    scis.set(s)
                    science.ten()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at science categories question 10 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    science.ten()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return
        
    scis=StringVar()
    scis.set("0")
    clo_5=PhotoImage(file="close display.png")
    closeimage5=Label(root,image=clo_5,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    closeimage5.place(x=400,y=0)
    main_3=PhotoImage(file="scorebackground.png")
    mainimage3=Label(root,image=main_3,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    mainimage3.place(x=0,y=500)
    sci=Frame(root,width=880,height=720,bg="#c6a66d",relief=SUNKEN)
    sci.place(x=400,y=0)
    label_2=Label(sci,text=" Science:",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d")
    label_2.grid(row=0,column=0,sticky=W)
    sciscore=Label(root,text="Score",font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    sciscore.place(x=0,y=500)
    nextsci=Button(root,text="Next",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d",command=sciences2)
    nextsci.place(x=1000,y=600)
    numsciscore=Label(root,textvariable=scis,font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    numsciscore.place(x=0,y=600)
    Question_one=Label(sci,text="1.Who created the famous equation E=mc2?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_one.grid(row=1,columnspan=10,sticky=W)
    Answer_one=Label(sci,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_one.grid(row=2,column=0,)
    Entry_one=Entry(sci,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_one.grid(row=2,column=1)
    check1=Button(sci,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check1)
    check1.grid(row=2,column=2)
    Question_two=Label(sci,text="2.What chemical elements is commonly known as quicksilver?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_two.grid(row=3,columnspan=10,sticky=W)
    Answer_two=Label(sci,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_two.grid(row=4,column=0)
    Entry_two=Entry(sci,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_two.grid(row=4,column=1)
    check2=Button(sci,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check2)
    check2.grid(row=4,column=2)
    Question_three=Label(sci,text="3.What is the name of the muscular tube that connects the throat with the stomach?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_three.grid(row=5,columnspan=10,sticky=W)
    Answer_three=Label(sci,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_three.grid(row=6,column=0)
    Entry_three=Entry(sci,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_three.grid(row=6,column=1)
    check3=Button(sci,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check3)
    check3.grid(row=6,column=2)
    Question_four=Label(sci,text="4.What type of plastic can be softened by heat?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_four.grid(row=7,columnspan=10,sticky=W)
    Answer_four=Label(sci,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_four.grid(row=8,column=0)
    Entry_four=Entry(sci,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_four.grid(row=8,column=1)
    check4=Button(sci,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check4)
    check4.grid(row=8,column=2)
    Question_five=Label(sci,text="5.What is the only fossil fuel still in a solid state?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_five.grid(row=9,columnspan=10,sticky=W)
    Answer_five=Label(sci,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_five.grid(row=10,column=0)
    Entry_five=Entry(sci,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_five.grid(row=10,column=1)
    check5=Button(sci,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check5)
    check5.grid(row=10,column=2)
    Question_six=Label(sci,text="6.On the periodic table, elements are arranged in order of what?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_six.grid(row=11,columnspan=10,sticky=W)
    Answer_six=Label(sci,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_six.grid(row=12,column=0)
    Entry_six=Entry(sci,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_six.grid(row=12,column=1)
    check6=Button(sci,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check6)
    check6.grid(row=12,column=2)
    Question_seven=Label(sci,text="7.What is the process by which plants convert light energy into food known as?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_seven.grid(row=13,columnspan=10,sticky=W)
    Answer_seven=Label(sci,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_seven.grid(row=14,column=0)
    Entry_seven=Entry(sci,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_seven.grid(row=14,column=1)
    check7=Button(sci,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check7)
    check7.grid(row=14,column=2)
    Question_eight=Label(sci,text="8.What scientific name is table salt known as?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_eight.grid(row=15,columnspan=10,sticky=W)
    Answer_eight=Label(sci,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_eight.grid(row=16,column=0)
    Entry_eight=Entry(sci,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_eight.grid(row=16,column=1)
    check8=Button(sci,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check8)
    check8.grid(row=16,column=2)
    Question_nine=Label(sci,text="9.What is the only metal that is liquid at room temperature?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_nine.grid(row=17,columnspan=10,sticky=W)
    Answer_nine=Label(sci,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_nine.grid(row=18,column=0)
    Entry_nine=Entry(sci,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_nine.grid(row=18,column=1)
    check9=Button(sci,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check9)
    check9.grid(row=18,column=2)
    Question_ten=Label(sci,text="10.Global warming is caused by too much of which type of gas?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_ten.grid(row=19,columnspan=10,sticky=W)
    Answer_ten=Label(sci,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_ten.grid(row=20,column=0)
    Entry_ten=Entry(sci,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_ten.grid(row=20,column=1)
    check10=Button(sci,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check10)
    check10.grid(row=20,column=2) 
       
#==Music==
#Frame
#Question
#Answer
k=[]
def musics2():
    m11=[]
    def check11():
        msg3=k
        v=100
        guess=Entry_eleven.get()
        user_guess=guess.title()
        Entry_eleven.delete(0 ,END)
        guesscount=m11
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Something Just Like This":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.eleven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 11 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.eleven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m12=[]
    def check12():
        msg3=k
        v=100
        guess=Entry_twelve.get()
        user_guess=guess.title()
        Entry_twelve.delete(0 ,END)
        guesscount=m12
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Canadian":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.twelve()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 12 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.twelve()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m13=[]
    def check13():
        msg3=k
        v=100
        guess=Entry_thirteen.get()
        user_guess=guess.title()
        Entry_thirteen.delete(0 ,END)
        guesscount=m13
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Thinking Out Loud":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.thirteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 13 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.thirteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m14=[]
    def check14():
        msg3=k
        v=100
        guess=Entry_fourteen.get()
        user_guess=guess.title()
        Entry_fourteen.delete(0 ,END)
        guesscount=m14
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Beyonce":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.fourteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 14 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.fourteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m15=[]
    def check15():
        msg3=k
        v=100
        guess=Entry_fifteen.get()
        user_guess=guess.title()
        Entry_fifteen.delete(0 ,END)
        guesscount=m15
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Symphony":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.fifteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 15 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.fifteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m16=[]
    def check16():
        msg3=k
        v=100
        guess=Entry_sixteen.get()
        user_guess=guess.title()
        Entry_sixteen.delete(0 ,END)
        guesscount=m16
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Can\'T Stop The Feeling":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.sixteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 16 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.sixteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m17=[] 
    def check17():
        msg3=k
        v=100
        guess=Entry_seventeen.get()
        user_guess=guess.title()
        Entry_seventeen.delete(0 ,END)
        guesscount=m17
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="New Kids On The Block":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.seventeen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 17 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.seventeen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m18=[] 
    def check18():
        msg3=k
        v=100
        guess=Entry_eighteen.get()
        user_guess=guess.title()
        Entry_eighteen.delete(0 ,END)
        guesscount=m18
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Adam Levine":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.eighteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 18 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.eighteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m19=[] 
    def check19():
        msg3=k
        v=100
        guess=Entry_nineteen.get()
        user_guess=guess.title()
        Entry_nineteen.delete(0 ,END)
        guesscount=m19
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="The Beatles":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.nineteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 19 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.nineteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m20=[] 
    def check20():
        msg3=k
        v=100
        guess=Entry_twenty.get()
        user_guess=guess.title()
        Entry_twenty.delete(0 ,END)
        guesscount=m20
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Grenade":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.twenty()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 20 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.twenty()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    mus=StringVar()
    clo_8=PhotoImage(file="close display.png")
    closeimage8=Label(root,image=clo_8,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    closeimage8.place(x=400,y=0)
    mu2=Frame(root,bg="#c6a66d",relief=SUNKEN)
    mu2.place(x=400,y=0)
    label_2=Label(mu2,text=" Music   :",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d")
    label_2.grid(row=0,column=0,sticky=W) 
    muscore=Label(root,text="Score",font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    muscore.place(x=0,y=500)
    backmu=Button(root,text="Back",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d",command=musics)
    backmu.place(x=1000,y=600)
    nummuscore=Label(root,textvariable=mus,font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    nummuscore.place(x=0,y=600)
    Question_eleven=Label(mu2,text="11.Coldplay teamed up with Chainsmokers on which 2017 track?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_eleven.grid(row=1,columnspan=10,sticky=W)
    Answer_eleven=Label(mu2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_eleven.grid(row=2,column=0)
    Entry_eleven=Entry(mu2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_eleven.grid(row=2,column=1)
    check11=Button(mu2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check11)
    check11.grid(row=2,column=2)
    Question_twelve=Label(mu2,text="12.What nationality is Shawn Mendes?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_twelve.grid(row=3,columnspan=10,sticky=W)
    Answer_twelve=Label(mu2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_twelve.grid(row=4,column=0)
    Entry_twelve=Entry(mu2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_twelve.grid(row=4,column=1)
    check12=Button(mu2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check12)
    check12.grid(row=4,column=2)
    Question_thirteen=Label(mu2,text="13.Which song earned Ed Sheeran the Grammy Award for Song of the Year in 2016?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_thirteen.grid(row=5,columnspan=10,sticky=W)
    Answer_thirteen=Label(mu2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_thirteen.grid(row=6,column=0)
    Entry_thirteen=Entry(mu2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_thirteen.grid(row=6,column=1)
    check13=Button(mu2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check13)
    check13.grid(row=6,column=2)
    Question_fourteen=Label(mu2,text="14.Which female artist sang the lyrics, ‘To the left, to the left, everything you own in the box to the left’?",font = ('Times',13,"bold"),fg="#B35900",bg="#c6a66d")
    Question_fourteen.grid(row=7,columnspan=10,sticky=W)
    Answer_fourteen=Label(mu2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_fourteen.grid(row=8,column=0)
    Entry_fourteen=Entry(mu2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_fourteen.grid(row=8,column=1)
    check14=Button(mu2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check14)
    check14.grid(row=8,column=2)
    Question_fifteen=Label(mu2,text="15.Zara Larsson featured on which 2017 hit song by Clean Bandit?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_fifteen.grid(row=9,columnspan=10,sticky=W)
    Answer_fifteen=Label(mu2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_fifteen.grid(row=10,column=0)
    Entry_fifteen=Entry(mu2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_fifteen.grid(row=10,column=1)
    check15=Button(mu2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check15)
    check15.grid(row=10,column=2)
    Question_sixteen=Label(mu2,text="16.Which song by Justin Timberlake was released in 2016 for the Trolls movie soundtrack?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_sixteen.grid(row=11,columnspan=10,sticky=W)
    Answer_sixteen=Label(mu2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_sixteen.grid(row=12,column=0)
    Entry_sixteen=Entry(mu2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_sixteen.grid(row=12,column=1)
    check16=Button(mu2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check16)
    check16.grid(row=12,column=2)
    Question_seventeen=Label(mu2,text="17.Which 1980’s boy band was known as NKOTB?'.",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_seventeen.grid(row=13,columnspan=10,sticky=W)
    Answer_seventeen=Label(mu2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_seventeen.grid(row=14,column=0)
    Entry_seventeen=Entry(mu2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_seventeen.grid(row=14,column=1)
    check17=Button(mu2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check17)
    check17.grid(row=14,column=2)
    Question_eighteen=Label(mu2,text="18.Who is the lead singer of Maroon Five?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_eighteen.grid(row=15,columnspan=10,sticky=W)
    Answer_eighteen=Label(mu2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_eighteen.grid(row=16,column=0)
    Entry_eighteen=Entry(mu2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_eighteen.grid(row=16,column=1)
    check18=Button(mu2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check18)
    check18.grid(row=16,column=2)
    Question_nineteen=Label(mu2,text="19.‘I Want To Hold Your Hand’ was a hit song in 1960s for which band.",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_nineteen.grid(row=17,columnspan=10,sticky=W)
    Answer_nineteen=Label(mu2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_nineteen.grid(row=18,column=0)
    Entry_nineteen=Entry(mu2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_nineteen.grid(row=18,column=1)
    check19=Button(mu2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check19)
    check19.grid(row=18,column=2)
    Question_twenty=Label(mu2,text="20.Which Bruno Mars’ song begins with the lyrics: ‘Easy come, easy go, that’s just how you live’?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_twenty.grid(row=19,columnspan=10,sticky=W)
    Answer_twenty=Label(mu2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_twenty.grid(row=20,column=0)
    Entry_twenty=Entry(mu2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_twenty.grid(row=20,column=1)
    check20=Button(mu2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check20)
    check20.grid(row=20,column=2)

k=[]
def musics():
    k.clear()
    print("Welome back to music categories")
    brek()
    m1=[]
    def check1():
        msg3=k
        v=100
        guess=Entry_one.get()
        user_guess=guess.title()
        Entry_one.delete(0 ,END)
        guesscount=m1
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Demi Lovato":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.one()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 1 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.one()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m2=[]
    def check2():
        msg3=k
        v=100
        guess=Entry_two.get()
        user_guess=guess.title()
        Entry_two.delete(0 ,END)
        guesscount=m2
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Owl City":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.two()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 2 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.two()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m3=[]
    def check3():
        msg3=k
        v=100
        guess=Entry_three.get()
        user_guess=guess.title()
        Entry_three.delete(0 ,END)
        guesscount=m3
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Katy Perry":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.three()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 3 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.three()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m4=[]
    def check4():
        msg3=k
        v=100
        guess=Entry_four.get()
        user_guess=guess.title()
        Entry_four.delete(0 ,END)
        guesscount=m4
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Justin Bieber":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.four()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 4 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.four()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m5=[]
    def check5():
        msg3=k
        v=100
        guess=Entry_five.get()
        user_guess=guess.title()
        Entry_five.delete(0 ,END)
        guesscount=m5
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Maroon 5":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.five()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 5 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.five()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m6=[]
    def check6():
        msg3=k
        v=100
        guess=Entry_six.get()
        user_guess=guess.title()
        Entry_six.delete(0 ,END)
        guesscount=m6
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="2013":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.six()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 6 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.six()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m7=[]
    def check7():
        msg3=k
        v=100
        guess=Entry_seven.get()
        user_guess=guess.title()
        Entry_seven.delete(0 ,END)
        guesscount=m7
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Halsey":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.seven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 7 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.seven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m8=[]
    def check8():
        msg3=k
        v=100
        guess=Entry_eight.get()
        user_guess=guess.title()
        Entry_eight.delete(0 ,END)
        guesscount=m8
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Umbrella":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.eight()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 8 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.eight()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m9=[]
    def check9():
        msg3=k
        v=100
        guess=Entry_nine.get()
        user_guess=guess.title()
        Entry_nine.delete(0 ,END)
        guesscount=m9
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Shape Of You":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.nine()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 9 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.nine()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m10=[]
    def check10():
        msg3=k
        v=100
        guess=Entry_ten.get()
        user_guess=guess.title()
        Entry_ten.delete(0 ,END)
        guesscount=m10
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Katy Perry":
                    msg3.append(v)
                    total=sum(msg3)
                    s=total
                    mus.set(s)
                    music.ten()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at music categories question 10 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    music.ten()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    mus=StringVar()
    mus.set("0")
    clo_6=PhotoImage(file="close display.png")
    closeimage6=Label(root,image=clo_6,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    closeimage6.place(x=400,y=0)
    main_3=PhotoImage(file="scorebackground.png")
    mainimage3=Label(root,image=main_3,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    mainimage3.place(x=0,y=500)
    mu=Frame(root,width=880,height=720,bg="#c6a66d",relief=SUNKEN)
    mu.place(x=400,y=0)
    label_3=Label(mu,text=" Music  :",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d")
    label_3.grid(row=0,column=0,sticky=W)
    muscore=Label(root,text="Score",font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    muscore.place(x=0,y=500)
    nextmu=Button(root,text="Next",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d",command=musics2)
    nextmu.place(x=1000,y=600)
    nummuscore=Label(root,textvariable=mus,font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    nummuscore.place(x=0,y=600)
    Question_one=Label(mu,text="1.With which American singer did Clean Bandit team on with on their single Solo?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_one.grid(row=1,columnspan=10,sticky=W)
    Answer_one=Label(mu,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_one.grid(row=2,column=0,)
    Entry_one=Entry(mu,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_one.grid(row=2,column=1)
    check1=Button(mu,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check1)
    check1.grid(row=2,column=2)
    Question_two=Label(mu,text="2.Which American group had a 2010 UK number one single with ‘Fireflies’?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_two.grid(row=3,columnspan=10,sticky=W)
    Answer_two=Label(mu,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_two.grid(row=4,column=0)
    Entry_two=Entry(mu,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_two.grid(row=4,column=1)
    check2=Button(mu,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check2)
    check2.grid(row=4,column=2)
    Question_three=Label(mu,text="3.Which American pop star has the birth name Kathryn?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_three.grid(row=5,columnspan=10,sticky=W)
    Answer_three=Label(mu,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_three.grid(row=6,column=0)
    Entry_three=Entry(mu,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_three.grid(row=6,column=1)
    check3=Button(mu,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check3)
    check3.grid(row=6,column=2)
    Question_four=Label(mu,text="4.Which Canadian singer had a 2015 hit with ‘What Do You Mean’?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_four.grid(row=7,columnspan=10,sticky=W)
    Answer_four=Label(mu,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_four.grid(row=8,column=0)
    Entry_four=Entry(mu,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_four.grid(row=8,column=1)
    check4=Button(mu,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check4)
    check4.grid(row=8,column=2)
    Question_five=Label(mu,text="5.Who was at a payphone, trying to phone home in 2012?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_five.grid(row=9,columnspan=10,sticky=W)
    Answer_five=Label(mu,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_five.grid(row=10,column=0)
    Entry_five=Entry(mu,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_five.grid(row=10,column=1)
    check5=Button(mu,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check5)
    check5.grid(row=10,column=2)
    Question_six=Label(mu,text="6.In what year did Christina Aguilere have a hit with 'Say Something'?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_six.grid(row=11,columnspan=10,sticky=W)
    Answer_six=Label(mu,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_six.grid(row=12,column=0)
    Entry_six=Entry(mu,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_six.grid(row=12,column=1)
    check6=Button(mu,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check6)
    check6.grid(row=12,column=2)
    Question_seven=Label(mu,text="7.Which American singer partner The Chainsmokers on the single Closer?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_seven.grid(row=13,columnspan=10,sticky=W)
    Answer_seven=Label(mu,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_seven.grid(row=14,column=0)
    Entry_seven=Entry(mu,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_seven.grid(row=14,column=1)
    check7=Button(mu,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check7)
    check7.grid(row=14,column=2)
    Question_eight=Label(mu,text="8.Which Rihanna song contains the lyrics: “When the sun shines, we’ll shine together. Told you I’d be here forever”?",font = ('Times',13,"bold"),fg="#B35900",bg="#c6a66d")
    Question_eight.grid(row=15,columnspan=10,sticky=W)
    Answer_eight=Label(mu,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_eight.grid(row=16,column=0)
    Entry_eight=Entry(mu,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_eight.grid(row=16,column=1)
    check8=Button(mu,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check8)
    check8.grid(row=16,column=2)
    Question_nine=Label(mu,text="9.Which Ed Sheeran hit begins with the lyrics: ‘The club isn’t the best place to find a lover’?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_nine.grid(row=17,columnspan=10,sticky=W)
    Answer_nine=Label(mu,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_nine.grid(row=18,column=0)
    Entry_nine=Entry(mu,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_nine.grid(row=18,column=1)
    check9=Button(mu,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check9)
    check9.grid(row=18,column=2)
    Question_ten=Label(mu,text="10.Who had a 2017 hit with ‘Chained to the Rhythm’ ?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_ten.grid(row=19,columnspan=10,sticky=W)
    Answer_ten=Label(mu,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_ten.grid(row=20,column=0)
    Entry_ten=Entry(mu,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_ten.grid(row=20,column=1)
    check10=Button(mu,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check10)
    check10.grid(row=20,column=2)
    
#==Movie==
#Frame
#Question
#Answer
y=[]
def movies2():
    m11=[]
    def check11():
        msg4=y
        v=100
        guess=Entry_eleven.get()
        user_guess=guess.title()
        Entry_eleven.delete(0 ,END)
        guesscount=m11
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Monster Inc":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.eleven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 11 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.eleven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return
            
    m12=[]
    def check12():
        msg4=y
        v=100
        guess=Entry_twelve.get()
        user_guess=guess.title()
        Entry_twelve.delete(0 ,END)
        guesscount=m12
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Fiona":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.twelve()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 12 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.twelve()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m13=[]
    def check13():
        msg4=y
        v=100
        guess=Entry_thirteen.get()
        user_guess=guess.title()
        Entry_thirteen.delete(0 ,END)
        guesscount=m13
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Roger Moore":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.thirteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 13 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.thirteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m14=[]
    def check14():
        msg4=y
        v=100
        guess=Entry_fourteen.get()
        user_guess=guess.title()
        Entry_fourteen.delete(0 ,END)
        guesscount=m14
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Toto":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.fourteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 14 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.fourteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m15=[]
    def check15():
        msg4=y
        v=100
        guess=Entry_fifteen.get()
        user_guess=guess.title()
        Entry_fifteen.delete(0 ,END)
        guesscount=m15
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Frodo Baggins":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.fifteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 15 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.fifteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m16=[]
    def check16():
        msg4=y
        v=100
        guess=Entry_sixteen.get()
        user_guess=guess.title()
        Entry_sixteen.delete(0 ,END)
        guesscount=m16
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Sixth Sense":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.sixteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 16 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.sixteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m17=[]
    def check17():
        msg4=y
        v=100
        guess=Entry_seventeen.get()
        user_guess=guess.title()
        Entry_seventeen.delete(0 ,END)
        guesscount=m17
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Toys Story":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.seventeen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 17 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.seventeen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m18=[]
    def check18():
        msg4=y
        v=100
        guess=Entry_eighteen.get()
        user_guess=guess.title()
        Entry_eighteen.delete(0 ,END)
        guesscount=m18
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Donkey":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.eighteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 18 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.eighteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m19=[]
    def check19():
        msg4=y
        v=100
        guess=Entry_nineteen.get()
        user_guess=guess.title()
        Entry_nineteen.delete(0 ,END)
        guesscount=m19
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Pixar":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.nineteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 19 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.nineteen()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m20=[]
    def check20():
        msg4=y
        v=100
        guess=Entry_twenty.get()
        user_guess=guess.title()
        Entry_twenty.delete(0 ,END)
        guesscount=m20
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Star Wars":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.twenty()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 20 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.twenty()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    mos=StringVar()
    clo_8=PhotoImage(file="close display.png")
    closeimage8=Label(root,image=clo_8,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    closeimage8.place(x=400,y=0)
    mo2=Frame(root,bg="#c6a66d",relief=SUNKEN)
    mo2.place(x=400,y=0)
    label_2=Label(mo2,text=" Movie   :",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d")
    label_2.grid(row=0,column=0,sticky=W) 
    moscore=Label(root,text="Score",font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    moscore.place(x=0,y=500)
    backmo=Button(root,text="Back",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d",command=movies)
    backmo.place(x=1000,y=600)
    nummoscore=Label(root,textvariable=mos,font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    nummoscore.place(x=0,y=600)
    Question_eleven=Label(mo2,text="11.From which movie do the characters Sully and Mike come from?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_eleven.grid(row=1,columnspan=10,sticky=W)
    Answer_eleven=Label(mo2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_eleven.grid(row=2,column=0)
    Entry_eleven=Entry(mo2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_eleven.grid(row=2,column=1)
    check11=Button(mo2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check11)
    check11.grid(row=2,column=2)
    Question_twelve=Label(mo2,text="12.In the film 'Shrek', what is the name of Shrek's wife?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_twelve.grid(row=3,columnspan=10,sticky=W)
    Answer_twelve=Label(mo2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_twelve.grid(row=4,column=0)
    Entry_twelve=Entry(mo2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_twelve.grid(row=4,column=1)
    check12=Button(mo2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check12)
    check12.grid(row=4,column=2)
    Question_thirteen=Label(mo2,text="13.Who played James Bond in 'Live and Let Die'?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_thirteen.grid(row=5,columnspan=10,sticky=W)
    Answer_thirteen=Label(mo2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_thirteen.grid(row=6,column=0)
    Entry_thirteen=Entry(mo2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_thirteen.grid(row=6,column=1)
    check13=Button(mo2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check13)
    check13.grid(row=6,column=2)
    Question_fourteen=Label(mo2,text="14.What was the name of Dorothy’s dog in the wizard of OZ?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_fourteen.grid(row=7,columnspan=10,sticky=W)
    Answer_fourteen=Label(mo2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_fourteen.grid(row=8,column=0)
    Entry_fourteen=Entry(mo2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_fourteen.grid(row=8,column=1)
    check14=Button(mo2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check14)
    check14.grid(row=8,column=2)
    Question_fifteen=Label(mo2,text="15.What is the name of the hobbit played by Elijah Wood in the Lord of the Rings movies?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_fifteen.grid(row=9,columnspan=10,sticky=W)
    Answer_fifteen=Label(mo2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_fifteen.grid(row=10,column=0)
    Entry_fifteen=Entry(mo2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_fifteen.grid(row=10,column=1)
    check15=Button(mo2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check15)
    check15.grid(row=10,column=2)
    Question_sixteen=Label(mo2,text="16.Guess this movie quote.'I see dead people'.",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_sixteen.grid(row=11,columnspan=10,sticky=W)
    Answer_sixteen=Label(mo2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_sixteen.grid(row=12,column=0)
    Entry_sixteen=Entry(mo2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_sixteen.grid(row=12,column=1)
    check16=Button(mo2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check16)
    check16.grid(row=12,column=2)
    Question_seventeen=Label(mo2,text="17.Guess this movie quote.'Reach for the sky!'.",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_seventeen.grid(row=13,columnspan=10,sticky=W)
    Answer_seventeen=Label(mo2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_seventeen.grid(row=14,column=0)
    Entry_seventeen=Entry(mo2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_seventeen.grid(row=14,column=1)
    check17=Button(mo2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check17)
    check17.grid(row=14,column=2)
    Question_eighteen=Label(mo2,text="18.Which character sings “I’m a Believer” in the 'Shrek' movie?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_eighteen.grid(row=15,columnspan=10,sticky=W)
    Answer_eighteen=Label(mo2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_eighteen.grid(row=16,column=0)
    Entry_eighteen=Entry(mo2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_eighteen.grid(row=16,column=1)
    check18=Button(mo2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check18)
    check18.grid(row=16,column=2)
    Question_nineteen=Label(mo2,text="19.Coco, Cars and Inside Out are all films produced by which US animated film company?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_nineteen.grid(row=17,columnspan=10,sticky=W)
    Answer_nineteen=Label(mo2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_nineteen.grid(row=18,column=0)
    Entry_nineteen=Entry(mo2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_nineteen.grid(row=18,column=1)
    check19=Button(mo2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check19)
    check19.grid(row=18,column=2)
    Question_twenty=Label(mo2,text="20.‘Solo’ is latest release from which famous movie franchise?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_twenty.grid(row=19,columnspan=10,sticky=W)
    Answer_twenty=Label(mo2,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_twenty.grid(row=20,column=0)
    Entry_twenty=Entry(mo2,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_twenty.grid(row=20,column=1)
    check20=Button(mo2,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check20)
    check20.grid(row=20,column=2)

y=[]
def movies():
    y.clear()
    print("Welome back to movie categories")
    brek()
    m1=[]
    def check1():
        msg4=y
        v=100
        guess=Entry_one.get()
        user_guess=guess.title()
        Entry_one.delete(0 ,END)
        guesscount=m1
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Mystique":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.one()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 1 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.one()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m2=[]
    def check2():
        msg4=y
        v=100
        guess=Entry_two.get()
        user_guess=guess.title()
        Entry_two.delete(0 ,END)
        guesscount=m2
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="It":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.two()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 2 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                else:
                    movie.two()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m3=[]
    def check3():
        msg4=y
        v=100
        guess=Entry_three.get()
        user_guess=guess.title()
        Entry_three.delete(0 ,END)
        guesscount=m3
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Oasis":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.three()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 3 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.three()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m4=[]
    def check4():
        msg4=y
        v=100
        guess=Entry_four.get()
        user_guess=guess.title()
        Entry_four.delete(0 ,END)
        guesscount=m4
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="San Andreas":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.four()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 4 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.four()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m5=[]
    def check5():
        msg4=y
        v=100
        guess=Entry_five.get()
        user_guess=guess.title()
        Entry_five.delete(0 ,END)
        guesscount=m5
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Suicide Squad":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.five()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 5 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.five()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m6=[]
    def check6():
        msg4=y
        v=100
        guess=Entry_six.get()
        user_guess=guess.title()
        Entry_six.delete(0 ,END)
        guesscount=m6
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Henry Cavill":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.six()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 6 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.six()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m7=[]
    def check7():
       msg4=y
       v=100
       guess=Entry_seven.get()
       user_guess=guess.title()
       Entry_seven.delete(0 ,END)
       guesscount=m7
       addcount=1
       guesslimit=3
       out_of_guesses=False
       while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Wade Wilson":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.seven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 7 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.seven()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m8=[]
    def check8():
        msg4=y
        v=100
        guess=Entry_eight.get()
        user_guess=guess.title()
        Entry_eight.delete(0 ,END)
        guesscount=m8
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Horror":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.eight()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 8 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.eight()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    m9=[]
    def check9():
        msg4=y
        v=100
        guess=Entry_nine.get()
        user_guess=guess.title()
        Entry_nine.delete(0 ,END)
        guesscount=m9
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Finding Nemo":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.nine()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 9 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.nine()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return
    m10=[]
    def check10():
        msg4=y
        v=100
        guess=Entry_ten.get()
        user_guess=guess.title()
        Entry_ten.delete(0 ,END)
        guesscount=m10
        addcount=1
        guesslimit=3
        out_of_guesses=False
        while out_of_guesses==False:
            if len(guesscount)<guesslimit:
                if user_guess=="Alice In Wonderland":
                    msg4.append(v)
                    total=sum(msg4)
                    s=total
                    mos.set(s)
                    movie.ten()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    correct()
                    return
                elif user_guess=="":
                    messagebox.showinfo("Error" , "You must answer the question given... Thank You")
                    print("You are at movie categories question 10 ")
                    print("Error! You must answer the question given... Thank You")
                    brek()
                    return
                else:
                    movie.ten()
                    guesscount.append(addcount)
                    print("You are not out of guess limit. Your attempt", len(guesscount), "now.")
                    wrong()
                    return
                return

            else:
                out_of_guesses=True
                print("You are out of guess limit.Try next question.")
                print("Your already attempt", len(guesscount), "before.")
                print("Each question have 3 chances to guess.")
                brek()
                return

    mos=StringVar()
    mos.set("0")
    clo_7=PhotoImage(file="close display.png")
    closeimage7=Label(root,image=clo_7,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    closeimage7.place(x=400,y=0)
    main_3=PhotoImage(file="scorebackground.png")
    mainimage3=Label(root,image=main_3,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    mainimage3.place(x=0,y=500)
    mo=Frame(root,width=880,height=720,bg="#c6a66d",relief=SUNKEN)
    mo.place(x=400,y=0)
    label_3=Label(mo,text=" Movie  :",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d")
    label_3.grid(row=0,column=0,sticky=W)
    moscore=Label(root,text="Score",font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    moscore.place(x=0,y=500)
    nextmo=Button(root,text="Next",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d",command=movies2)
    nextmo.place(x=1000,y=600)
    nummoscore=Label(root,textvariable=mos,font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d",bd=0,activebackground="#c6a66d")
    nummoscore.place(x=0,y=600)
    Question_one=Label(mo,text="1.I am blue, able to change into anyone including animals. What character am I?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_one.grid(row=1,columnspan=10,sticky=W)
    Answer_one=Label(mo,text="Answer :",font = ('Times',16,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_one.grid(row=2,column=0,)
    Entry_one=Entry(mo,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_one.grid(row=2,column=1)
    check1=Button(mo,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check1)
    check1.grid(row=2,column=2)
    Question_two=Label(mo,text="2.Which film is about a group of kids who band together to face a shapeshifting monster?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_two.grid(row=3,columnspan=10,sticky=W)
    Answer_two=Label(mo,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_two.grid(row=4,column=0)
    Entry_two=Entry(mo,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_two.grid(row=4,column=1)
    check2=Button(mo,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check2)
    check2.grid(row=4,column=2)
    Question_three=Label(mo,text="3.What is the name of the virtual reality world in Ready Player One?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_three.grid(row=5,columnspan=10,sticky=W)
    Answer_three=Label(mo,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_three.grid(row=6,column=0)
    Entry_three=Entry(mo,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_three.grid(row=6,column=1)
    check3=Button(mo,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check3)
    check3.grid(row=6,column=2)
    Question_four=Label(mo,text="4.Starring Dwayne Johnson this film has as its backdrop a massive earthquake in California.",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_four.grid(row=7,columnspan=10,sticky=W)
    Answer_four=Label(mo,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_four.grid(row=8,column=0)
    Entry_four=Entry(mo,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_four.grid(row=8,column=1)
    check4=Button(mo,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check4)
    check4.grid(row=8,column=2)
    Question_five=Label(mo,text="5.Deadshot, Griggs and Harley Quinn are characters from which 2016 action movie?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_five.grid(row=9,columnspan=10,sticky=W)
    Answer_five=Label(mo,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_five.grid(row=10,column=0)
    Entry_five=Entry(mo,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_five.grid(row=10,column=1)
    check5=Button(mo,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check5)
    check5.grid(row=10,column=2)
    Question_six=Label(mo,text="6.Who plays Superman in the action film Batman v Superman: Dawn of Justice?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_six.grid(row=11,columnspan=10,sticky=W)
    Answer_six=Label(mo,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_six.grid(row=12,column=0)
    Entry_six=Entry(mo,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_six.grid(row=12,column=1)
    check6=Button(mo,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check6)
    check6.grid(row=12,column=2)
    Question_seven=Label(mo,text="7.In the film Deadpool starring Ryan Reynolds, what is the name of Deadpool's alter ego?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_seven.grid(row=13,columnspan=10,sticky=W)
    Answer_seven=Label(mo,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_seven.grid(row=14,column=0)
    Entry_seven=Entry(mo,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_seven.grid(row=14,column=1)
    check7=Button(mo,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check7)
    check7.grid(row=14,column=2)
    Question_eight=Label(mo,text="8.The Babadook, It Follows and 31 are all films from which genre?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_eight.grid(row=15,columnspan=10,sticky=W)
    Answer_eight=Label(mo,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_eight.grid(row=16,column=0)
    Entry_eight=Entry(mo,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_eight.grid(row=16,column=1)
    check8=Button(mo,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check8)
    check8.grid(row=16,column=2)
    Question_nine=Label(mo,text="9.Marlin, Dory and Gill are characters from which 2003 animated movie?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_nine.grid(row=17,columnspan=10,sticky=W)
    Answer_nine=Label(mo,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_nine.grid(row=18,column=0)
    Entry_nine=Entry(mo,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_nine.grid(row=18,column=1)
    check9=Button(mo,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check9)
    check9.grid(row=18,column=2)
    Question_ten=Label(mo,text="10.Which Disney movie does the Cheshire Cat appear in?",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Question_ten.grid(row=19,columnspan=10,sticky=W)
    Answer_ten=Label(mo,text="Answer :",font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Answer_ten.grid(row=20,column=0)
    Entry_ten=Entry(mo,font = ('Times',15,"bold"),fg="#B35900",bg="#c6a66d")
    Entry_ten.grid(row=20,column=1)
    check10=Button(mo,text=" Check ",bg="#c6a66d",font = ('Times',10,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=check10)
    check10.grid(row=20,column=2)
    
#==============================================================About=============================================================================
#==About==
#==cover==
#Frame
def about():
    clo_1=PhotoImage(file="close categories.png")
    closeimage1=Label(root,image=clo_1,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    closeimage1.place(x=0,y=230)
    clo_2=PhotoImage(file="close display.png")
    closeimage2=Label(root,image=clo_2,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    closeimage2.place(x=400,y=0)
    main_3=PhotoImage(file="scorebackground.png")
    mainimage3=Label(root,image=main_3,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    mainimage3.place(x=0,y=500)
    ab=Frame(root,bg="#c6a66d",relief=SUNKEN)
    ab.place(x=400,y=0)
    label_4=Label(ab,text=" About  :",font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d")
    label_4.grid(row=0,column=0,sticky=W)
    detail=Label(ab,text=info,font = ('Times',13,"bold"),fg="#B35900",bg="#c6a66d")
    detail.grid(row=1,column=0, ipadx=40)
    logo=Label(ab,text=" T ",font = ('Times',50,"bold"),fg="#f7e171",bg="#e1671a")
    logo.grid(row=1, columnspan=1,sticky=NE)

#===========================================================Start============================================================================
#==Start==
#==Categories==
#Frame
def cate():
    cat=Frame(root,bg="#c6a66d",relief=SUNKEN)
    cat.place(x=0,y=230)
    clo_3=PhotoImage(file="close display.png")
    closeimage3=Label(root,image=clo_3,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    closeimage3.place(x=400,y=0)
    Welcome=Label(root,text="  Welcome  ",font = ('Times',120,"bold"),fg="#B35900",bg="#c6a66d")
    Welcome.place(x=450,y=320)
    Try=Label(root,text=" @ To Try My Riddle ! @ Created by Aynsley Aaron Chong (2018) & Ng Jing Ping (2018) ",font = ('Times',8,"bold"),fg="#B35900",bg="#c6a66d")
    Try.place(x=625,y=500)
    logo=Label(root,text=" T ",font = ('Times',100,"bold"),fg="#f7e171",bg="#e1671a")
    logo.place(x=750,y=180)
    main_3=PhotoImage(file="scorebackground.png")
    mainimage3=Label(root,image=main_3,bg="#c6a66d",bd=0,activebackground="#c6a66d")
    mainimage3.place(x=0,y=500)
    Categories=Label(cat,text="  Categories  ",font = ('Times',50,"bold"),fg="#B35900",bg="#c6a66d")
    Categories.grid(row=0,columnspan=5)
    logic=Button(cat,text="  Logic ",bg="#c6a66d",font = ('Times',30,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=logics)
    logic.grid(row=1,column=2)
    science=Button(cat,text="Science",bg="#c6a66d",font = ('Times',30,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=sciences)
    science.grid(row=1,column=3)
    music=Button(cat,text=" Music ",bg="#c6a66d",font = ('Times',30,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=musics)
    music.grid(row=2,column=2)
    movie=Button(cat,text=" Movie ",bg="#c6a66d",font = ('Times',30,"bold"),fg="#B35900",activebackground="#c6a66d",activeforeground="#B35900",command=movies)
    movie.grid(row=2,column=3)
    
#==========================================================Main====================================================================================
#Frame
main=Frame(root,bg="#c6a66d",relief=SUNKEN)
main.place(x=0,y=0)
Title=Label(main,text="Try My Riddle!",font = ('Times',42,"bold"),fg="#B35900",bg="#c6a66d")
Title.grid(row=0,column=0)
Time=Label(main,text=localtime,font = ('Times',20,"bold"),fg="#B35900",bg="#c6a66d")
def tick():
    s = time.strftime('%d %b %Y %I:%M:%S %p')
    if s != Time["text"]:
        Time["text"] = s
    Time.after(200, tick)

tick()
Time.grid(row=1,column=0)
photo1=PhotoImage(file="start.png")
start=Button(main,image=photo1,bg="#c6a66d",bd=0,activebackground="#c6a66d",command=cate)
start.grid(row=2,column=0)
photo2=PhotoImage(file="about.png")
about=Button(main,image=photo2,bg="#c6a66d",bd=0,activebackground="#c6a66d",command=about)
about.grid(row=3,column=0)
main_1=PhotoImage(file="close display.png")
mainimage1=Label(root,image=main_1,bg="#c6a66d",bd=0,activebackground="#c6a66d")
mainimage1.place(x=400,y=0)
main_2=PhotoImage(file="close categories.png")
mainimage2=Label(root,image=main_2,bg="#c6a66d",bd=0,activebackground="#c6a66d")
mainimage2.place(x=0,y=230)
main_3=PhotoImage(file="scorebackground.png")
mainimage3=Label(root,image=main_3,bg="#c6a66d",bd=0,activebackground="#c6a66d")
mainimage3.place(x=0,y=500)

#==========GUI Size (1280 pixels x 720 pixel)(NO RESIZABLE)==========================================================
root.maxsize(width=1280,height=720)
root.minsize(width=1280,height=720)
width_of_root=1280
height_of_root=720
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_root/2)
y_coordinate = (screen_height/2)-(height_of_root/2)
root.geometry("%dx%d+%d+%d" % (width_of_root,height_of_root,x_coordinate,y_coordinate))

if root.destroy:
    file=open("report.txt","a")
    file.write("\nThank you ! ")
    file.write(name)
    file.write("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    file.close()
    
root.mainloop()
root.destroy
