import random
import os


def welcome(name1):
    print("Hello {}".format(name1))

def first():
    print("Welcome to Hangman")
    welcome(input("Enter name\n"))
def won():
    print("\nYou Won ")
    os.system("pause")
def lost():
    sarcasms = ['It’s okay if you didn’t get it. Not everyone has great mind.',
                'Unless your name is Google stop acting like you know everything.',
                'Everyone has the right to be stupid, but you are abusing the privilege.',
                'I clapped because it’s finished, not because I like it.',
                'Zombies eat brains. You’re safe.',
                'I’ll try being nicer, if you try being smarter.',
                'Keep rolling your eyes. Maybe you’ll find a brain back there.']
    print("You lost")
    print('{}\n'.format(random.choice(sarcasms)))
    os.system("pause")
def patt(guessn):
    if guessn == 6:
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guessn == 5:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guessn == 4:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|        |")
        print("|        |")
        print("|")
        print("|________")
    elif guessn == 3:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|       \|")
        print("|        |")
        print("|")
        print("|________")
    elif guessn == 2:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|       \|/")
        print("|        |")
        print("|")
        print("|________")
    elif guessn == 1:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|       \|/")
        print("|        |")
        print("        /")
        print("|________")
    elif guessn == 0:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|       \|/")
        print("|        |")
        print("        / | ")
        print("|________")


def wordguess():
    word=['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

    count=0
    r=0
                    #counting length of the words of the list to make total turns
    for w in word:
        for l in w:
            count+=1
        if count >r:
            r=count
        count = 0

    guessn=7
    print("You will get only 4 guesses")
    turn = r+4

    gword=random.choice(word)
    print("Guess the characters")


    print("Length of word is ",len(gword))
    gletter=''
    while turn > 0 and guessn >0:

        for letter in gword:
            if letter in gletter:
                comp = ['Nice one', 'Great', 'You are killing it']
                print('{} '.format(letter),end="")
            else:
                print("_ ",end="")
        if set(gletter) == set(gword):   # if the words match & converted to sets to remove repetition of the letters
            won()
            turn=0
            break
        else:
            gletterw = input("\nEnter a letter   ")[0]


        if gletterw in gword:
            comp = ['Nice one', 'Great', 'You are killing it']
            print("{}".format(random.choice(comp)))
            print("Correct {} guesses left".format(guessn))
            patt(guessn)
            gletter += gletterw
        else:
            guessn-=1
            print("Wrong {} guesses left".format(guessn))
            patt(guessn)

        turn-=1
    if guessn==0:
        lost()
if __name__ == '__main__':
    first()
    wordguess()




