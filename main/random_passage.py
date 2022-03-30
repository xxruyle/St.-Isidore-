import random 
from readbible import data  

# all the books in the CPDV JSON
books = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1-Samuel', '2-Samuel', '1-Kings', '2-Kings', '1-Chronicles', '2-Chronicles', 'Ezra', 'Nehemiah', 'Tobit', 'Judith', 'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'Song2', 'Wisdom', 'Sirach', 'Isaiah', 'Jeremiah', 'Lamentations', 'Baruch', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', '1-Maccabees', '2-Maccabees', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1-Corinthians', '2-Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1-Thessalonians', 
'2-Thessalonians', '1-Timothy', '2-Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1-Peter', '2-Peter', '1-John', '2-John', '3-John', 'Jude', 'Revelation']


# Allows user to get random verse from a random book
def randompassage():
    book = books[random.randrange(len(books))]
    return randombook_passage(book)


# Allows user to get random verse from a specific book taken as an argument 
def randombook_passage(book):
    # The chapters of the book
    bookchapters = len(list(data[book].keys()))
    if len(list(data[book].keys())) == 0 or 1:  # If the length of the list of keys in a book is 1 or 0. We +1 so we don't call randrange(1,1)
        bookchapters = len(list(data[book].keys())) + 1
    chapter = random.randrange(1, bookchapters)

    # The verses of the chapter 
    bookverses = len(list(data[book][str(chapter)].keys()))
    if len(list(data[book][str(chapter)].keys())) == 0 or 1:  
        bookverses = len(list(data[book][str(chapter)].keys())) + 1
    verse = random.randrange(1, bookverses)

    passage = f'{book} {str(chapter)} {str(verse)}'  # formatting so getverse() and tokenize_passage() can read it properly              

    return passage


