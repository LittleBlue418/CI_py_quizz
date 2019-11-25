def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")

    option = input("Enter option: ")
    return option

def ask_questions():
    # Defining our empty variables
    questions = []
    answers = []

    # Opening our text file and reading the split lines
    # Into a variable 'lines'
    # The with statement here will automatically close the file after
    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()

    # Enumerating (itterating) through the lines variable
    # Taking the questions and answers text and appending them to the questions and answers variables
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)

    # Zipping together the questions and answers to form
    # Effectively two columns of text
    # The questions and answers will be in pairs e can easilly access
    for question, answer in zip(questions, answers):
        guess = input(question + "> ")



def add_question():
    print("")
    question = input("Enter a question\n>")

    print("")
    print("Sounds good, tell me the answer")

    answer = input("{0}\n>".format(question))

    file = open("questions.txt","a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()


def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            ask_questions()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid option, please enter '1', '2' or '3'")
        print("")

game_loop()