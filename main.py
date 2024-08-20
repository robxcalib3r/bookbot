def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        # print(file_contents)
        getNumOfWords(file_contents)

def getNumOfWords(text:str):
    words = text.split()
    print(len(words))

def getNumofChars(words:str):
    pass

main()

