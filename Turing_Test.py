def turing_test():

    print("Turing Test Simulation")

    questions = [
        "How are you?",
        "What is your favorite color?",
        "What is 2 + 2?"
    ]

    answers = [
        "I am fine",
        "Blue",
        "4"
    ]

    for i in range(len(questions)):

        print("Judge:", questions[i])
        response = input("Machine: ")

        if response.lower() == answers[i].lower():
            print("Response seems human-like")
        else:
            print("Response seems machine-like")


turing_test()
