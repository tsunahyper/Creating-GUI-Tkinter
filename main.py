#Using ttk instead of tk due to that the buttons and features from tk was developed in 1991, thus ttk is a more modern and updated version when using tkinter as GUI
import tkinter as tk
from tkinter import ttk

#Classes when being called, the "dunder" stands for "double underscore" will be automatically run
class App():
    def __init__(self):
        #Initialise the window, Tk() class creates a top level widget which is the main window of the application
        self.root =tk.Tk()
        
        #To specify the width ad size of the windows/application (eg: 350 width, 200 height), Can also add '500x500+4000+500' where adding 4000+500 will determine where the pop-up will be.
        self.root.geometry('500x500')

        #Adding title to the windows
        self.root.title('Test App')
       
        #Place all widgets inside of a frame, these would eases when designing a complex GUI like creating a new pages when all widegets are inside of one frame.
        self.mainframe = tk.Frame(self.root, background='teal')
      
        #This is where the widget will be placed within the frame, fill and expand where the frame fills the whole window
        self.mainframe.pack(fill='both', expand=True)
      
        #Adding title of the application, Label is Tkinter's way of getting text on the application
        self.text = ttk.Label(self.mainframe, text='Hello World', background='teal', font=("Times New Roman",30))
      
        #Where the title of the application will be placed inside the main frame
        self.text.grid(row=0, column=0)
      
        #Adding the widget for this case creating a textbox, the column 0 will populate and place under the same column as Adding title of the application.
        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky='NWES')
        
        #This allow text button to be keyed in and replace the title of the application, will call the set_text funtion to add functionalities.
        set_text_button = ttk.Button(self.mainframe, text ='Set Text', command=self.set_text)
        set_text_button.grid(row=1, column=1, pady=10)
      
        #This allow user to select from the color button to change the color of the application title. 'set_color' will call the funtion to allow the functionalities.
        color_options = ['red', 'black', 'blue', 'green']
        self.set_color_field = ttk.Combobox(self.mainframe, values=color_options)
        self.set_color_field.grid(row=2, column=0, pady=10, sticky='NWES')
        set_color_button = ttk.Button(self.mainframe, text ='Set Color', command=self.set_color)
        set_color_button.grid(row=2, column=1, pady=10)
        
        #Button to reverse the text. 'reverse' will call the funtion to allow the functionalities.
        self.reverse_text = ttk.Button(self.mainframe, text='Reverse Text', command=self.reverse)
        
        #Mainloop must be called to call the windows on the screen
        self.root.mainloop()
        return

    #Function to set text or replace the text of the Application Title
    def set_text(self):
        newtext = self.set_color_field.get()
        self.text.config(foreground=newtext)

    #Function to set text or replace the text of the Application Title
    def set_color(self):
        newcolor = self.set_text_field.get()
        self.text.config(text=newcolor)

    #Function to set text or replace the text of the Application Title
    def reverse(self):
        newtext = self.text.cget('text')
        reversed = newtext[::-1]
        self.text.config(text=reversed)
        
#Calling dunder App class   
if __name__ == '__main__':
    App()