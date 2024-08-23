def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        # print(file_contents)
        num_words, words = getNumOfWords(file_contents)
        Dict = getNumofChars(words)
        print('--- Begin report of books/frankenstein.txt ---')
        print(f'{num_words} words found in the document')
        print('\n')
        new_list = listify(Dict)
        new_list.sort(reverse=True, key=sort_on)
        for each in new_list:
            if each['char'].isalpha():
                print(f"The {each['char']} character was found {each['num']} times")



            
def listify(dict):
    unsorted_list = []
    for item in dict:
        new_dict = {}
        new_dict['char'] = item
        new_dict['num'] = dict[item]
        unsorted_list.append(new_dict)
    return unsorted_list

def sort_on(dict):
    return dict["num"]

        

def getNumOfWords(text:str):
    words = text.split()
    return len(words), words

def getNumofChars(words:str):
    Dict = {}
    for word in words:
        for char in word.lower():
            try:
                Dict[char] += 1
            except:
                Dict[char] = 1
    return Dict


main()

