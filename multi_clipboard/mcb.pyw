# --MULTI CLIPBOARD PROGRAM--
#to load the program 
#this program saves and loads text to the clipboard using shortcuts
#the shortcuts are assigned to program on the shell while running it

import shelve,pyperclip,sys
def mcb():
    mcbShelf = shelve.open('mcb')

    if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 2:
        #list keywords and load content
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])
    mcbShelf.close()
    
mcb()