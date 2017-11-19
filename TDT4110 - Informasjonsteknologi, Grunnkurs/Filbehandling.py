#Må spesifisere hvordan filen skal brukes med parameter i open metoden.
#r for lesing av filen(default)
#w for skriving til filen
#a for å legge til data(append)



def main():

    def write_to_file(filename): #W is typically used fo Write but as it overrides earlier text append(a) is better used here.
        f = open("testfile.txt", "a")
        f.write(w_answer + ". ")
        f.close()

    def read_from_file(filename):
        f = open(filename, "r")
        innhold = f.read()
        print(innhold)


    answer = input("Type W to write, R to read or Done to end")
    while answer != "Done" and answer != "done":

        if answer == "R" or answer == "r":
            print("Current content: ")
            read_from_file("testfile.txt")

        elif answer == "W" or answer == "w":
            w_answer = input ("What would you like to write?")
            write_to_file(w_answer)

        answer = input("Type W to write, R to read or Done to end")

    print("Goodbye")
main()

