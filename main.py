import random
import os

print("Welcome to Test Generator")

print("How many Tests to create for you?")
test_amount = int(input())

# Create list to insert the questions from the txt file
containerQes = []
with open("soccer_questions.txt", "r") as my_Container:
    for q in my_Container:
        containerQes.append(q)

# Add to each file 4 questions
for i in range(test_amount):
    with open(F"Test{i + 1}.txt", "a") as test_file:
        strQues = ''
        lines = random.sample(containerQes, 4)
        strQues = ''.join(lines)
        test_file.write(strQues)
        test_file.close()

i = 1
while os.path.exists(F"Test{i}.txt"):
    print(F"----Test {i}----\n")
    with open(F"Test{i}.txt", "r") as my_file:
        j = 1
        for line in my_file:
            print(F"{str(j)}. {line}")
            j += 1
    i = i + 1
