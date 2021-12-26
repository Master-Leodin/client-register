
register = []


def list():
    for line in register: print(line)


def lista():
    name = str.title(input("What is your name?\n"))
    age = str(input("How old are you?\n"))
    phone = str(input("What is your phone number?\n"))
    register.append({"name": name, "age": age, "phone": phone})
    list()
    per()


def per():
    question = str.lower(input("Will you register one more person?\n"))
    while question != "yes" or question != "no":
        if question == "yes":
            lista()
            break
        elif question == "no":
            print("Thank you to use our services\n")
            break
        else:
            print('Answer "yes" or "no"\n')
            question = str.lower(input("Will you register one more person?\n"))

def final():

    per2 = str.lower(input("Do you want to see our registration list?\n"))
    while per2 != "yes" or per2 != "no":
        if per2 == "yes":
            list()
            break
        elif per2 == "no":
            print("End of the application.")
            break
        else:
            per2 = str.lower(input('Answer "yes" or "no"\n'))
