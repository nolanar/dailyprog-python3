"""GUI for TextLife

TODO
 - Clean up code
     - Add classes
     - Function to add new toolbar button
 - Preferences menu:
     - Set tab width
     - Game run speed
"""

from tkinter import *
import tkinter.font as tkfont

def toggle_frame(frame):
    state = frame.cget('state')
    if state == 'normal':
        frame.config(state=DISABLED)
        # Indicate when disabled with background color.
        frame.config(bg='grey94')
    elif state == 'disabled':
        frame.config(state=NORMAL)
        frame.config(bg='white')
        
root = Tk()
root.geometry('800x600')
root.title('TextLife')

#Menu bar.
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_command(label='Save')

settingsmenu = Menu(menubar, tearoff=0)
settingsmenu.add_command(label='Preferences')

menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Settings', menu=settingsmenu)
# display the menu
root.config(menu=menubar)

#Outermost frame.
frame_main = Frame(root)
frame_main.pack(fill=BOTH, expand=YES)
#first row and coulmn expands with window.
frame_main.grid_columnconfigure(0, weight=1)
frame_main.grid_rowconfigure(1, weight=1)

#Toolbar.
toolbar = Frame(frame_main)
toolbar.grid(row=0, column=0, sticky=N+E+W+S)
#Button to run game.
btn_play = Button(toolbar, text='Start/Stop', padx=5, relief=FLAT, command=lambda: toggle_frame(txt))
btn_play.grid(row=0, column=0, sticky=W, padx=5)
#Button to export to file.
btn_save = Button(toolbar, text='Step', relief=FLAT)
btn_save.grid(row=0, column=1, sticky=W, padx=5)
#Preferences menu button.
btn_pref = Button(toolbar, text='?', relief=FLAT)
btn_pref.grid(row=0, column=2, sticky=W, padx=5)

#Text-area frame.
frame_txt = Frame(frame_main, bd=2, relief=SUNKEN)
#fill and expand with window
frame_txt.grid_columnconfigure(0, weight=1)
frame_txt.grid_rowconfigure(0, weight=1)
frame_txt.grid(row=1, column=0, sticky=N+E+W+S)

#Scrollbars.
xbar = Scrollbar(frame_txt, relief=FLAT, orient=HORIZONTAL)
xbar.grid(row=1, column=0, sticky=E+W)
ybar = Scrollbar(frame_txt, relief=FLAT)
ybar.grid(row=0, column=1, sticky=N+S)

#Textfield.
txt = Text(frame_txt, wrap=NONE, xscrollcommand=xbar.set, yscrollcommand=ybar.set)
txt.grid(row=0, column=0, sticky=N+S+E+W)
#Set tab to 4 space width.
txt.config(tabstyle=('wordprocessor'))
font = tkfont.Font(font=txt['font'])
tab_width = font.measure(' ' * 4)
txt.config(tabs=(tab_width))

#Allow cursor-drag scrollbars.
xbar.config(command=txt.xview)
ybar.config(command=txt.yview)

root.mainloop()

