print("""
      Mad Libs is a word game where players are prompted for one word at a time,
      and the words are eventually filled into the blanks of a word template to 
      make an entertaining story! """)

def main():
    #user say input lena
    adjective = input("Type adjective and press enter : ")
    noun = input("Type noun and press enter : ")
    verb = input("Type verb and press enter : ")
    place = input("Please type a place and press enter : ")

     # starter sentence set krna
    starter_sentence = "Once upon a time a "
    # final result print 
    print(f"{starter_sentence} {adjective} {noun} dicided to {verb} in the, {place} Its was a wild advanture !")

if __name__ == '__main__':
    main()