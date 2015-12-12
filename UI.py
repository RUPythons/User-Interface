from tkinter import *
from tkinter import ttk

def find(*args):                                                # Gets called when find button is clicked
    try:
        value = path.get()                                      # Will get the path from the input box
        result1.set(1)                                          # Needs to be  modified to give out image URL results by doing the lookup
        result2.set(2)
        result3.set(3)
        result4.set(4)
        result5.set(5)
        result6.set(6)
        result7.set(7)
    except ValueError:
        pass
    
root = Tk()
root.title("Pattern Recognizier")                               # Title of the window

mainframe = ttk.Frame(root, padding="3 3 12 12")                # Making of a Frame
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=10)
mainframe.rowconfigure(0, weight=10)

path = StringVar()                                              # Variables holding path and results 
result1 = StringVar()
result2 = StringVar()
result3 = StringVar()
result4 = StringVar()
result5 = StringVar()
result6 = StringVar()
result7 = StringVar()

path_entry = ttk.Entry(mainframe, width=20, textvariable=path)  
path_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=result1).grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=result2).grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, textvariable=result3).grid(column=2, row=5, sticky=(W, E))
ttk.Label(mainframe, textvariable=result4).grid(column=2, row=6, sticky=(W, E))
ttk.Label(mainframe, textvariable=result5).grid(column=2, row=7, sticky=(W, E))
ttk.Label(mainframe, textvariable=result6).grid(column=2, row=8, sticky=(W, E))
ttk.Label(mainframe, textvariable=result7).grid(column=2, row=9, sticky=(W, E))
ttk.Button(mainframe, text="find", command=find).grid(column=3, row=10, sticky=W)

ttk.Label(mainframe, text="Enter path to your image").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Following are the results found:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="First").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="Second").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, text="Third").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="Fourth").grid(column=1, row=6, sticky=E)
ttk.Label(mainframe, text="Fifth").grid(column=1, row=7, sticky=E)
ttk.Label(mainframe, text="Sixth").grid(column=1, row=8, sticky=E)
ttk.Label(mainframe, text="Seventh").grid(column=1, row=9, sticky=E)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

path_entry.focus()
root.bind('<Return>', find)

root.mainloop()
