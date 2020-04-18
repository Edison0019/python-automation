#this is a python project design for text scrapping
#this is design for stracting phone numbers and email addresses from the clipboard
import re, pyperclip

phone = re.compile(r'''
    \d{10}| #ten numbers
    \d{3}-?\d{3}-\d{4}| #ten numbers with hyphen
    \d{3}\.\d{3}\.\d{4}| #separated by points
    \d{3}-\d{4}|
    \(\d{3}\)?\d{3}-\d{4}| #numbers with parenthesis
    \d{3}\s?\d{3}\s\d{4}| #numbers with spaces
    \d{7}
    ''',re.VERBOSE) # VERBOSE for writing multiline regular expressions

#This is the email regular expression 
email = re.compile(r'[a-zA-Z0-9-_*%-+]+@[a-zA-Z0-9-]+\.[a-zA-Z]+')

#this is to copy the text in the clipboard
text = str(pyperclip.paste())
def findr(text):
    matches = []
    for i in phone.findall(text):
        matches.append(i)

    for i in email.findall(text):
        matches.append(i)
    return matches

def copyr():
    result = findr(text)
    x = open('contact.txt','w')
    if len(result) > 0:
        x.write('\n'.join(result))
        print('information added to file')
        x.close()
    else:
        print('no matches found')

copyr()