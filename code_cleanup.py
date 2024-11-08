import random

def function_A(min, max):
    """
    Random integer.
    """
    return random.randint(min, int(max))  # Convert max to integer to avoid errors

def function_B():
    return random.choice(['+', '-', '*'])

def function_C(n1, n2, o):
    p = f"{n1} {o} {n2}"
    # Correct the logic to handle each operation properly
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3  # Set t_q to an integer value for the number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = function_A(1, 10)
        n2 = function_A(1, 5)  # Set max to an integer
        o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")

        try:
            useranswer = int(useranswer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
