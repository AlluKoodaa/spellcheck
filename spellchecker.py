###---AlluKoodaa---###

def check(text, words):
    checked = []
    for word in text:
        if word.casefold() not in words:
            word = f"*{word}*"
        checked.append(word)
    return " ".join(checked)

def main():
    wordlist = []
    with open("wordlist.txt") as tdst:
        for rivi in tdst:
            wordlist.append(rivi.strip())

    text = input("Write text: ").split()
    print(check(text, wordlist))

main()

###---eof---###