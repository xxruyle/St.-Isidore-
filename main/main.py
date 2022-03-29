from readbible import data  # The bible in json format
from tokenize_passage import parse 
from random_passage import randompassage
    #: = parsed_passage[2]
    #init_verse = parsed_passage[3]
    #- = parsed_passage[4]


def getverse(passage):
    parsed_passage = parse(passage)  
    book = parsed_passage[0]
    chapter = parsed_passage[1]
    obt_passage = []  # list for storing passages that have multiple lines 
    # if parse length is 2 (EX: Genesis 1)
    try:
        if len(parsed_passage) == 2:
            multiverse = data[book][chapter]  # getting the parse
            for verse in multiverse:  
                obt_passage.append(verse + ' ' + multiverse[verse])  # getting proper format and adding the lines to the list
            return readlist(obt_passage)  # returning the passage list      
        # if parse length is 4 (EX: Genesis 1:2)
        elif len(parsed_passage) == 3:
            init_verse = parsed_passage[2]  # the number after the colon 
            verse = data[book][chapter][init_verse]
            singleverse = parsed_passage[2] + ' ' + verse  # Getting proper format 
            obt_passage.append(singleverse)
            return readlist(obt_passage)
        # if parse length is 6 (EX: Genesis 1:2-3)
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
        return "That passage does not exist"  # If there is no passage that exists


def getrandomverse():
    passage = randompassage()
    return f'{passage}:\n{getverse(passage)}'

def readlist(list):
    string = ' \n \n'.join(list)
    return string
        

