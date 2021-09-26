from CODE import CODE


def morze(word):
        morze_word = ""
        for i in word:
                if i == " ":
                        morze_word += " /"
                elif i == word[0]:
                        morze_word += CODE[f"{i.upper()}"]
                else:
                        morze_word = morze_word + " " + CODE[f"{i.upper()}"]

        print( morze_word)
        another = input("Do you want to translate another?Print 'yes' or 'no'")
        if another == "yes":
                word = input("type you word here")
                morze(word)
        else:
                print("Bye")







word = input("type you word here")
morze(word)



