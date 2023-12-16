import rasa

def main():
    print("Rasa NLU version:", rasa.__version__)
    print("Rasa Core version:", rasa.core.__version__)

if __name__ == "__main__":
    main()