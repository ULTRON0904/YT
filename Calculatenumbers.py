import wolframalpha
import pyttsx3
import speech_recognition

class Calculator:
    def addition(number1: int, number2:int) -> int:
        return number1 + number2
        
    def subtraction(number1: int, number2:int) -> int:
        return number1 - number2
    
    def multiplay(number1: int, number2:int)  -> int:
        return number1 * number2
    
    def divide(number1: int, number2:int)  -> int:
        return number1 / number2
    

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = "YRG2KW-EG88TEWAP6"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    # calculator: Calculator = Calculator()
    # result = 0

    # match Term:
    #      case '+':
    #         result = calculator.addition()


    Final = str(Term)
    # Final = ""
    try:
        result = WolfRamAlpha(Final)
        print(str(result))
        speak(result)

    except:
        speak("The value is not answerable")