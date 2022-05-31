# Import tkinter library
from tkinter import *
import os
class GUESSPLAY:
    def __init__(self, name1, name2):
        self.P1=name1
        self.P2=name2
    def myfunc(self):
        word = input(self.P1+" PLEASE ENTER A WORD FOR "+self.P2+" TO GUESS:")
        clear = lambda: os.system('cls')
        clear()
        firstChar=word[0]
        length=len(word)
        lastChar=word[length-1]
        secretWord=firstChar;
        for i in range(length-2):
            secretWord=secretWord+"*"
        secretWord=secretWord+lastChar;
        if length==1:
            secretWord="*"
        elif length==2:
            secretWord="**"
        print("THE ORIGINAL WORD IS SUCCESSFULLY HIDDEN.")
        print("THE SECRET WORD IS: "+secretWord)
        picPos=0
        guesses = ''
        guesses = ''
        turns = 8
        txtguess=""
        winText="CONRATULATIONS YOU WON!"
        while turns > 0:
            failed = 0
            for char in word:
                if char in guesses:
                    x=1  
                else:
                    failed += 1
            if failed == 0:
                print("You Win")
                isWin=1
                print("THE WORD IS: ", word)
                break
            
            print()
            guess = input("GUESS A CHARACTER: ")
            guesses += guess
            txtguess=txtguess+guess
            if guess not in word:
                picPos=picPos+120
                turns -= 1
                print("WRONG")
                print("YOU HAVE", + turns, 'MORE GUESSESS')
                if turns == 0:
                    print("YOU LOOSE..!");
                    winText="SAD FOR YOU! YOU LOOSE"
        txtUnguess="GUESS THE WORD: "+secretWord;            

        # Create an instance of tkinter frame or window
        root = Tk()
        root.title(  "WordGuessGame ")
        #root.geomatery("1255*944)

        # Create a Canvas
        canvas = Canvas(root, background="yellow", height=4000, width=5000)
        canvas.pack()
        canvas.create_text(220,30,font="Times 20 italic bold",fill="darkblue",text=txtUnguess)

        photo=PhotoImage(file=r"C:\Users\Latif\Desktop\Ambulance.png")

        #Image placing.....
        canvas.create_image(picPos,70,image=photo,anchor=NW)
        canvas.create_text(220,340,font="Times 20 italic bold",fill="darkblue",text="YOUR GUESS: "+txtguess)
        canvas.create_text(250,370,font="Times 20 italic bold",fill="RED",text=winText)
        
        root.mainloop()
        
p1 = GUESSPLAY("PLAYER1", "PLAYER2")
p1.myfunc()

p2 = GUESSPLAY("PLAYER2", "PLAYER1")
p2.myfunc()

