def file_print(file_create_not, wordlist):
    if file_create_not == 'y':
        filename = f"{first_name}.txt"
        with open(filename, 'w') as file_object:
            for word in wordlist:
                file_object.write(word+"\n")
    else:
        for word in wordlist:
            print(word)


def input_taking():
    first_name = input("first name: ")
    last_name = input("last name: ")
    date_of_birth = input("Year of birth: ")
    file_create_not = input("Do you want to write the wordlist in a file (y/n): ")

    return first_name, last_name, date_of_birth, file_create_not


def create_wordlist(first_name, last_name, date_of_birth):

    wordlist = []

    wordlist.append(first_name.lower())
    wordlist.append(first_name.lower() + last_name.lower())
    wordlist.append(first_name.title() + last_name.title())
    wordlist.append(first_name.title() + last_name.lower())
    wordlist.append(first_name.lower() + last_name.title())
    wordlist.append(last_name.lower())
    wordlist.append(last_name.title())
    wordlist.append(first_name.title())
    wordlist.append(last_name.lower() + first_name.lower())
    wordlist.append(last_name.title() + first_name.lower())
    wordlist.append(last_name.title() + first_name.title())
    wordlist.append(last_name.lower() + first_name.title())

    num = (len(wordlist))

    for i in range(num):
        wordlist.append(f"{wordlist[i]}123")
    for i in range(num):
        wordlist.append(f"{wordlist[i]}@123")
    for i in range(num):
        wordlist.append(f"{wordlist[i]}{date_of_birth}")

    return wordlist


first_name, last_name, date_of_birth, file_create_not = input_taking() 

wordlist = create_wordlist(first_name, last_name, date_of_birth) 

file_print(file_create_not, wordlist)
