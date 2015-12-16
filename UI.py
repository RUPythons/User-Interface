#!/usr/bin/python


from tkinter import *
from tkinter import ttk
from imagesearch import imageSearch
from PIL import Image

def find():          # Gets called when find button is clicked
    try:
        value1 = dataset.get()              # Will get the path from the input box
        value2 = shlv.get()
        value3 = query.get()
        files = imageSearch(value1, value2, value3)
        for i in files:
            image = Image.open(value1 + "/" + str(i))
            image.show()
    except ValueError:
        pass
    
root = Tk()
root.title("Fabric Finder")                # Title of the window

mainframe = ttk.Frame(root, padding="3 3 12 12")                # Making of a Frame
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=10)
mainframe.rowconfigure(0, weight=10)

dataset = StringVar()
shlv = StringVar()                                            # Variables holding path and results 
query = StringVar()


path_entry = ttk.Entry(mainframe, width=20, textvariable=dataset)  
path_entry.grid(column=2, row=1, sticky=(W, E))

path_entry = ttk.Entry(mainframe, width=20, textvariable=shlv)  
path_entry.grid(column=2, row=2, sticky=(W, E))

path_entry = ttk.Entry(mainframe, width=20, textvariable=query)  
path_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="find", command=find).grid(column=3, row=11, sticky=W)

ttk.Label(mainframe, text="Enter directory name of image files").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Enter database filename").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Enter name of the sample image file").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="Following are the results found:").grid(column=1, row=4, sticky=E)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

path_entry.focus()
root.bind('<Return>', find)

root.mainloop()
