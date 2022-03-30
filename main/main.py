from readbible import data  # The bible in json format
from tokenize_passage import parse 
from random_passage import randompassage
from random_passage import randombook_passage
from random_passage import books 

def getverse(passage):
    parsed_passage = parse(passage)  
    book = parsed_passage[0]
    chapter = parsed_passage[1]
    obt_passage = []  # list for storing passages that have multiple lines 
    
    try:
        # if parse length is 2 (EX: Genesis 1)
        if len(parsed_passage) == 2:
            multiverse = data[book][chapter]  # getting the parse
            for verse in multiverse:  
                obt_passage.append(verse + ' ' + multiverse[verse])  # getting proper format and adding the lines to the list
            return readlist(obt_passage)  # returning the passage list      
        # if parse length is 3 (EX: Genesis 1:2)
        elif len(parsed_passage) == 3:
            init_verse = parsed_passage[2]  # the number after the colon 
            verse = data[book][chapter][init_verse]
            singleverse = parsed_passage[2] + ' ' + verse  # Getting proper format 
            obt_passage.append(singleverse)
            return readlist(obt_passage)
        # if parse length is 4 (EX: Genesis 1:2-3)
        elif len(parsed_passage) == 4:
            # defining variables
            end_verse = parsed_passage[3]
            init_verse = parsed_passage[2]
            multiverse = data[book][chapter]
            for verse in multiverse:  
                obt_passage.append(verse + ' ' + multiverse[verse])  # getting proper format and adding the lines to the list
            indexed_verses = obt_passage[int(init_verse)-1:int(end_verse)]  # Getting the verses between init_verse and end_verse
            return readlist(indexed_verses)
        # else, parse is not correct format  (EX: Genesis)
        elif parsed_passage == 0:
            return "Not proper format (Book Chapter:list or Book Chapter)"
    except KeyError:
        return "Not proper format (Book Chapter:list or Book Chapter)"  # If there is no passage that exists

# Allows user to get random verse from any book
def getrandomverse():
    passage = randompassage()
    return f'{passage}:\n{getverse(passage)}'

# Allows user to get random verse from a specific book 
def randompassage_withbook(book):
    passage = randombook_passage(book)
    return f'{passage}:\n{getverse(passage)}'

def readlist(list):
    string = ' \n \n'.join(list)
    return string
        
def booklist():
    old_testament = '\n'.join(books[0:46])
    new_testament = ' \n'.join(books[46:])
    return f"Old Testament:\n\n{old_testament}\n\nNew Testament:\n\n{new_testament}"



