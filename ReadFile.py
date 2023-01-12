from tkinter import filedialog
from tkinter import *
    
def ReadInputFile(lines = 0):
    root = Tk()
    root.withdraw()
    root.filename =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))

    with open(root.filename) as f:
        content = f.readlines()
    
    if lines > 0:
        content = content[:lines]

    return content

def StripNewLines(lines):
    for row in range(len(lines)):
        lines[row] = lines[row].strip()
    return lines

def SplitToList(lines):
    for row in range(len(lines)):
        lines[row] = list(lines[row])
    return lines