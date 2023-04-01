# from itertools import tee
# from re import L
from tkinter import *
# from random import choice,choices
import time
import enchant

from backend2 import *

class App():
    def __init__(self, main,board):
        self.main = main
        self.main.resizable(0,0)
        self.bg=PhotoImage(file='FINAL BACKGROUND.png')
        self.bg1=Label(image=self.bg)
        self.bg1.place(x=0, y=0)
        self.board=board

        # self.instruction=Text(main,bg='#d1c49d',font='Times 14 bold',wrap=WORD,height=10,width=22)
        # self.instruction.place(x=50,y=100)
        # self.play_button=Button(main,text='Play',width=10,height=2,command=self.Function(self.board))
        # self.play_button.place(x=300,y=600)

        self.TopFrame = Frame(main)
        self.BottomFrame = Frame(main)
        self.MFrame=Frame(main,height=400,width=400)
        self.TopFrame.grid(row=0)
        self.BottomFrame.grid(row=4)
        self.word=''
        self.dictionary=enchant.Dict("en_US")
        self.lastclickedI=-1
        self.lastclickedJ=-1
        self.row = [-1, -1, -1, 0, 1, 0, 1, 1]
        self.col = [-1, 1, 0, -1, -1, 1, 0, 1]
        self.entry=Entry(main,width=17,bg='#e0d5dc',fg='black',font='sans 16 bold')
        self.entry.place(x=340,y=535,height=35)
        self.words_box=Text(main,bg='#e0d5dc',font='Times 14 bold',wrap=WORD,height=10,width=22)
        self.words_box.place(x=35,y=210)
        # self.words_box.insert(END,'               Words                     ')
        # self.words_box.insert(END,'\n')
        self.done=Button(main,text='Submit',width=10,height=2,fg='white',bg='black',command=self.done_click)
        self.done.place(x=350,y=600)
        self.giveup=Button(main,text='Finish Game',width=10,height=2,fg='white',bg='black',command=self.score_screen)
        self.giveup.place(x=450,y=600)
        self.word_lst={1:''}
        self.processed = []

        #timer
        self.mins= StringVar()
        Entry(main,bg='black',fg='white', textvariable = self.mins,justify=CENTER, width =3,font = 'sans 16 bold').place(x=650, y=310)
        self.mins.set('03')
        self.sec = StringVar()
        Entry(main,bg='black',fg='white', textvariable=self.sec, justify=CENTER,width = 3,font = 'sans 16 bold').place(x=690, y=310)
        self.sec.set('00')

    def instructions(self):
        instructions='HurdleGRAM is a word game which has a 3x3 grid. The user is required to make as many valid words as possible within 3 minutes. The user can traverse in eight possible direction. Minimum length of acceptable words is 3. The program creats a list of all possible words in the same grid in the backend, and the score is decided by comparing the words made user and the program.'
        self.instruction.insert(END,str(instructions))
        pass

    def Function(self,board):
        self.grid = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(Button(self.MFrame,text=board[i][j],font='sans 16 bold',width=7,height=4,fg='black',background='#ba8179',command=lambda i=i, j=j: self.getClick(i, j)))
                row[-1].grid(row=i,column=j)
            self.grid.append(row)
        self.MFrame.place(x=300,y=150)
        self.bg1.grid()

    def isSafe(self, i, j):
        for k in range(len(self.row)):
            if i==self.lastclickedI + self.row[k] and j==self.lastclickedJ + self.col[k]:
                status=True
                return status
        
        # return (0 <= x < len(processed)) and (0 <= y < len(processed[0]))\
        #     and not processed[x][y]

    def getClick(self, i, j):
        self.status=False
        if self.lastclickedI==-1 and self.lastclickedJ==-1:
            self.status=True
        else:
            self.status=self.isSafe(i,j)
        orig_color = self.grid[i][j].cget('bg')
        if orig_color=='#ba8179' and self.status==True:
            self.grid[i][j]["bg"]='#b8deb8'
            text=self.grid[i][j].cget('text')
            self.entry.insert(END,str(text))
            self.word+=str(text)
            self.lastclickedI = i
            self.lastclickedJ = j
        # self.word_lst[]
        # self.word_lst.append(str(text))        #get the words entered in text box
        # return self.word

    def done_click(self):
        # word=self.entry.cget()
        # print(word)
        if len(self.word)>=3:
            self.words_box.insert(END,str(self.word)+',')
            self.word=''
            self.entry.delete(0,'end')
            for i in range(3):
                for j in range(3):
                    orig_color = self.grid[i][j].cget('bg')
                    if orig_color=='#b8deb8':
                        self.grid[i][j]["bg"]='#ba8179'
            self.lastclickedI=-1
            self.lastclickedJ=-1
            # self.words_box.insert(END,str(self.word_lst[-1]))
            # print(self.word_lst[-1])
            # pass

    def countdowntimer(self):
        times = int(self.mins.get())*60 + int(self.sec.get())
        while times > -1:
            minute,second = (times // 60 , times % 60)
            self.sec.set(second)
            self.mins.set(minute)
            self.main.update()
            time.sleep(1)
            if(times == 0):
                self.sec.set('00')
                self.mins.set('00')
                time.sleep(1)
                self.score_screen
            times-=1
    
    def score_screen(self):
        # score=Tk()
        # score.geometry('850x1000')
        self.bg=PhotoImage(file='FINAL BACKGROUND.png')
        self.bg1=Label(image=self.bg)
        self.bg1.place(x=0, y=0)
        self.valid_words=Text(self.main,bg='#b8deb8',font='Times 14 bold',wrap=WORD,height=20,width=28)
        self.valid_words.place(x=80,y=120)
        valid_words_lst=searchInBoggle(self.board,self.dictionary)
        input=self.words_box.get('1.0',END)
        self.word_lst=input.split(',')
        print(self.word_lst)
        score=0

        self.valid_words.insert(END,'              Made by user ')
        self.valid_words.insert(END,'\n')
        for i in range(len(self.word_lst)-1):
            print(str(self.word_lst[i]))
            self.valid_words.insert(END,str(self.word_lst[i])+', ')

        self.valid_words.insert(END,'\n')
        self.valid_words.insert(END,' \n             Valid words')
        self.valid_words.insert(END,'\n')
        for i in valid_words_lst:
            self.valid_words.insert(END,str(i)+', ')
        print(valid_words_lst)
        
        for i in range(len(self.word_lst)-1):
            if self.word_lst[i] not in self.processed:
                if len(self.word_lst[i])==3 and self.word_lst[i] in valid_words_lst:
                    score+=5
                elif len(self.word_lst[i])==4 and self.word_lst[i] in valid_words_lst:
                    score+=10
                elif len(self.word_lst[i])>=5 and self.word_lst[i] in valid_words_lst:
                    score+=15
            self.processed.append(self.word_lst[i])

        self.score=Text(self.main,bg='#b8deb8',font='Times 14 bold',wrap=WORD,height=2,width=12)
        self.score.place(x=600,y=280)
        self.score.insert(END,'Your score is: ')
        self.score1=Text(self.main,bg='#b8deb8',font='Times 17 bold',wrap=WORD,height=2,width=10)
        self.score1.place(x=600,y=300)
        self.score.insert(END,'\n')
        self.score1.insert(END,'       '+str(score))
        print(self.score)

def play(main):
    board=generate_board()
    app = App(main,board)
    app.Function(board)
    app.countdowntimer()

def main2(main,bg2):
    bg3=Label(image=bg2)
    bg3.place(x=0, y=0)
    instruction=Text(main,bg='#e0d5dc',font='Times 14 bold',wrap=WORD,height=18,width=38)
    instruction.place(x=270,y=120)

    instruction.insert(END,'                            Instructions')
    instruction.insert(END,'\n \n')
    instruction.insert(END,' HurdleGRAM is a word game which has a 3x3 grid.\n') 
    instruction.insert(END,'The user is required to make as many valid   words as possible within 3 minutes.\n')
    instruction.insert(END,' The user can traverse in eight possible direction.\n')
    instruction.insert(END,' Minimum length of acceptable words is 3.\n')
    instruction.insert(END,'The program creats a list of all possible words in the same grid.\n')
    instruction.insert(END,'Score is decided by comparing the words made user and the program.\n')
    instruction.insert(END,'Three letter words has a score of 5.\n')
    instruction.insert(END,'Four letter words has a score of 10.\n')
    instruction.insert(END,'Five letter words has a score of 15.\n')

    play_button=Button(main,text='Play',width=10,height=1,bg='#b8deb8',font='Times 14 bold',command=lambda: play(main))
    play_button.place(x=385,y=560)

def main3():
    main=Tk()
    main.geometry('850x1000')
    main.resizable(0,0)
    main.configure(bg='white')
    bg=PhotoImage(file='Untitled (1).png')
    bg1=Label(image=bg)
    bg1.place(x=-40, y=40)

    bg2=PhotoImage(file='FINAL BACKGROUND.png')
    start_button=Button(main,text='Start',width=10,height=1,bg='#79d279',font='Times 14 bold',command=lambda: main2(main,bg2))
    start_button.place(x=350,y=600)
    main.mainloop()

main3()

