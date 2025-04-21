# match الأدوات الشرطية باستخدام 

name = input("What programming language are you learning: ")

match name.lower():
    case "python":
        print("You can use Python for AI")
    case "flutter":
        print("You can use Flutter for Mobile Applications")
    case _:
        print(f"You are learning {name}")