
register = []


def menu():
    print("Choose a option.\nUse the numbers to choose.\n")
    check = str(input("1) Register\n2) See the registrtion list\n3) Exit\n"))
    while check != "1" or check != "2" or check != "3":
        if check == "1":
            lista()
            break
        elif check == "2":
            print("Do not have persons registered on the system\n")
            print("End of the application.\n")
            break
        elif check == "3":
            print("End of the application.\n")
            break
        else:
            print("Choose only numbers 1, 2 or 3\n")
            check = str(input("1) Register\n2) See the registrtion list\n3) Exit\n"))
            
            
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
            final()
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
            print("End of the application.\b")
            break
        else:
            per2 = str.lower(input('Answer "yes" or "no"\n'))
