print("welcome To my small Quiz")
play = input("Do u wanna play my quiz? ")
if play.lower() != "yes":
    quit()
print("Let's go then! :)")
print("there's only one rule: Don't use Google.")
score = 0
Q1 = input("Which continent does France belong to ?  ")
if Q1.lower() == "europe":
    print("U are right!")
    score = score + 1
else:
    print("oops! That's wrong.")
Q2 = input("Which continent does the UK belong to? ")
if Q2.lower() == "europe":
    print("U are right!")
    score = score + 1
else:
    print("oops! That's wrong.")

Q3 = input("what is the country that hosts the Mississippi River? ")
if Q3.lower() == "usa":
    print("U are right!")
    score = score + 1
elif Q3.lower() == "the usa":
    print("U are right!")
    score = score + 1
else:
    print("oops! That's wrong.")

    Q4 = input("Which continent does Austria belong to ?  ")
    if Q4.lower() == "europe":
        print("U are right!")
        score = score + 1
print("That's all for today.")
print("your Score is " + str(score) + "!")
if score <= 2:
    print("study harder!")
prc= input("Do u wanna know your percentage? ")
if prc.lower()=="yes":
    print("you got "+str((score / 4))*100)
else:
    quit()




