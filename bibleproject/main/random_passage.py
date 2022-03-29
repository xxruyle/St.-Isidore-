import random 
from readbible import data  

books = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1-Samuel', '2-Samuel', '1-Kings', '2-Kings', '1-Chronicles', '2-Chronicles', 'Ezra', 'Nehemiah', 'Tobit', 'Judith', 'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'Song2', 'Wisdom', 'Sirach', 'Isaiah', 'Jeremiah', 'Lamentations', 'Baruch', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', '1-Maccabees', '2-Maccabees', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1-Corinthians', '2-Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1-Thessalonians', 
'2-Thessalonians', '1-Timothy', '2-Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1-Peter', '2-Peter', '1-John', '2-John', '3-John', 'Jude', 'Revelation']


def randompassage():
    book = books[random.randrange(len(books))]
    chapter = random.randrange(1, len(list(data[book].keys())))
    verse = random.randrange(1, len(list(data[book][str(chapter)].keys())))
    passage = f'{book} {str(chapter)} {str(verse)}'             

    return passage

