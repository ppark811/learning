import tkinter, random, sys, pandas as pd

class FlashCardApp:
    def __init__(self):
        
        self.LANG_TEXT = ("Arial", 40, "italic")
        self.WORD_TEXT = ("Arial", 60, "bold")
        self.BACKGROUND_COLOR = "#B1DDC6"
        self.rand_kor_word = ""
        self.kor_word = ""
        
        self.openFile()
        self.uiSetup()
        
    
    # generates a file with the unknown words when it closes
    def onClosing(self):
        if tkinter.messagebox.askyesno(title="Quit", message="Do you want to quit?"):
            self.dont_know_words.to_csv("./data/korean_top5k_dont_know_common_words.csv", index=False)
            self.window.destroy()
        
        
    # opens data file, or pre-existing data file from prior run
    def openFile(self):
        try:                                                                            # Try opening the "dont know words file"
            words = pd.read_csv("./data/korean_top5k_dont_know_common_words.csv")   
        except FileNotFoundError:                                                       # If it doesn't exist, make it as a DataFrame
            try:                                                                        # Try opening the data file, if it doesnt exist, exit the script 
                words = pd.read_csv("./data/korean_top5k_common_words.csv")             
            except FileNotFoundError:
                tkinter.messagebox.showinfo(title="Missing Data", message="There is no data file to read")
                sys.exit()
        finally:
            self.dont_know_words = words.copy()
            #self.dont_know_words.to_csv("./data/korean_top5k_dont_know_common_words.csv")
            self.know_words = pd.DataFrame()
    
    
    #flips card between english and korean
    def flipCard(self):   
        current_lang = self.canvas.itemcget(self.language_text, "text")
        if current_lang == "Korean":
            self.engCard()
        if current_lang == "English":
            self.korCard()


    # pulls a random word from the data file
    def randKorWord(self): # only happens on button presses
        self.rand_kor_word = random.choice(self.dont_know_words["korean"])
        self.korCard()


    # shows the korean word card
    def korCard(self):
        self.kor_word = self.rand_kor_word #this is a string variable, not the function
    
        self.canvas.itemconfig(self.card, image=self.card_front)
        self.canvas.itemconfig(self.word_text, text=self.kor_word, fill="black")
        self.canvas.itemconfig(self.language_text, text="Korean", fill="black")
        
    
    # shows the english word card
    def engCard(self):
        eng_word = self.dont_know_words.loc[self.dont_know_words["korean"] == self.kor_word, "english"].values[0]
        
        self.canvas.itemconfig(self.card, image=self.card_back)
        self.canvas.itemconfig(self.word_text, text=eng_word, fill="white")
        self.canvas.itemconfig(self.language_text, text="English", fill="white")
        
    
    # removes word from dataframe of words that the doce pulls from
    def removeWord(self):
        word_index = self.dont_know_words[self.dont_know_words["korean"] == self.kor_word].index[0]
        self.dont_know_words = self.dont_know_words.drop(word_index)


    # When the "know" button is clicked(green button), it runs these two functions
    def knowWord(self):
        self.removeWord()
        self.randKorWord()
    
    # sets up user interface
    def uiSetup(self):
        # --- UI setup --- #
        
        # Window
        self.window = tkinter.Tk()
        self.window.title("Korean Practicer")
        self.window.config(padx=50, pady=50, bg=self.BACKGROUND_COLOR)
        
        # Card
        self.canvas = tkinter.Canvas(width=800, height=526, bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.card_front = tkinter.PhotoImage(file="./images/card_front.png")
        self.card_back = tkinter.PhotoImage(file="./images/card_back.png")
        self.card = self.canvas.create_image(400,263, image=self.card_front)
        
        self.language_text = self.canvas.create_text(400, 150, font=self.LANG_TEXT)
        self.word_text = self.canvas.create_text(400, 263, font=self.WORD_TEXT)
        self.canvas.grid(column=0, row=0, columnspan=3)
        
        # Making a button so you can flip it over and over again
        self.flip_button = tkinter.Button(text="Flip Card", bg=self.BACKGROUND_COLOR, highlightthickness=0, command=self.flipCard)
        self.flip_button.grid(column=1, row=1)
        
        # DontKnow Button
        self.dont_know_button_image = tkinter.PhotoImage(file="./images/dont_know.png")
        self.dont_know_button = tkinter.Button(image=self.dont_know_button_image, highlightthickness=0, command=self.randKorWord)
        self.dont_know_button.grid(column=0, row=1)
        
        # Know Button
        self.know_button_image = tkinter.PhotoImage(file="./images/know.png")
        self.know_button = tkinter.Button(image=self.know_button_image, highlightthickness=0, command=self.knowWord)
        self.know_button.grid(column=2, row=1)
        
        self.randKorWord() # need this call so it can start without any button presses
        
        self.window.protocol("WM_DELETE_WINDOW", self.onClosing) # when the close button is pressed, do this
        self.window.mainloop()
        
        
flash_card_app = FlashCardApp() # run the program
