# Assignment 2: Are You an Introvert?

# Name: Jinyao DeSandies, Mon Sep 8 Assignment 2
print("Answer the following questions with 'yes' or 'no':")

# TODO: Prompt the user to answer the following 4 yes/no questions:
# 1. Do you prefer spending time alone?
# 2. Do you find large gatherings draining?
# 3. Do you enjoy deep one-on-one conversations over small talk?
# 4. Do you often reflect before speaking or acting?
# Rather than using the print function, we can combine
# prompting the user and reading their input using the following syntax
# answer = input("your prompt goes here")
# You should have four different variables to store the
# four different responses corresponding to the four different prompts
q1 = input("Do you prefer spending time alone?")
q2 = input("Do you find large gatherings draining??")
q3 = input("Do you enjoy deep one-on-one conversations over small talk?")
q4 = input("Do you often reflect before speaking or acting?")
answers = [q1, q2, q3, q4]
i = 0
# TODO Create four different bool variables, A-D, that will be True if the answer was "yes" and False otherwise.
for each in answers:
#for an extra UX twist I added the option for multiple versions of y to prevent capitalization errors
    if each == "Yes" or each == "yes" or each =="Y" or each =="y" or each =="1":
        answers[i] = True
        #changes the value of the list to the desired BOOL variables
    else:
        answers[i] = False
    i+=1
print(answers)
A,B,C,D = answers
# TODO: Replace this with the simplified Boolean expression that you derived using the K-map
# original boolean function: ($\lnot B \land \lnot C$) $\lor$ ($\lnot A \land \lnot B \land \lnot D$) $\lor$ ($\lnot A \land \lnot C$)
#After testing I realized that my map was opposite of the right answer, and although I could have reversed engineered it I did it the right way :)
#($C \land D$) $\lor$ ($ A \land B$) $\lor$ ($A\land C$) $\lor (B \land C)$
introvert = (C and D)or(A and B)or(A and C)or(B and C)  # ← your Boolean logic here


if introvert:
    print("You are likely an introvert")
else:
    print("You are likely an extrovert")
