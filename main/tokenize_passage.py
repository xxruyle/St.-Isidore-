# Tokenizing the string so that (EX: Genesis 1:1) turns into (['Genesis' , '1' , '1'])
def parse(string):
    # split the string 
    token = string.split()
    nocolon = token[-1].split(':')
    nohyphen = nocolon[-1].split('-')
    #If it is only the chapter with no initial verse line 
    if ':' in token[-1] and '-' not in token[-1]:
        return combinelist(nocolon, token[0])
        
    #If it is the chapter with the individual verse
    if token[-1].isdigit(): # if the last token of the list is a digit (a chapter)
        return token

    #If it is the chapter with init verse and end verse (EX: Genesis 1:2-3)    
    if ':' in token[-1] and '-' in token[-1]:
        first = combinelist(nocolon, token[0])
        first.pop()
        first.extend(nohyphen)
        return first 
    else:
        return 0 

def combinelist(first, second):
    first.insert(0, second)
    return first 




