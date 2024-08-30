from src.GreptileProcessor import Greptile
from src.LLM import LLM

greptile = Greptile('gauravreddy08/test1', branch='gh-pages')
llm = LLM(greptile=greptile)

userInput = input("What changes do you want to make?: ")

while True:
    print(f">Assistant: {llm.call(userInput)}")

    userInput = input("> User: ")
    if userInput=='q': break

