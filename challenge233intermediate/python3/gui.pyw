"""GUI for TextLife

TODO
 - Clean up code
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

#Outermost frame
frame_main = Frame(root)
frame_main.pack(fill=BOTH, expand=YES)
#first row and coulmn expands with window.
frame_main.grid_columnconfigure(0, weight=1)
frame_main.grid_rowconfigure(1, weight=1)

#Toolbar with Start/Stop button.
toolbar = Frame(frame_main, bd=3)
toolbar.grid(row=0, column=0, sticky=N+E+W+S)
btn_play = Button(toolbar, text='Start/Stop', bd=2, relief=GROOVE, command=lambda: toggle_frame(txt))
btn_play.pack(side=LEFT)

#Text-area frame.
frame_txt = Frame(frame_main, bd=2, relief=SUNKEN)
#fill and expand with window
frame_txt.grid_columnconfigure(0, weight=1)
frame_txt.grid_rowconfigure(0, weight=1)
frame_txt.grid(row=1, column=0, sticky=N+E+W+S)

#Scrollbars.
xbar = Scrollbar(frame_txt, orient=HORIZONTAL)
xbar.grid(row=1, column=0, sticky=E+W)
ybar = Scrollbar(frame_txt)
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

