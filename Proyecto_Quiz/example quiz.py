#Archivo prueba (bajado de internet) para el formato aleatorio
import random

questions = ["Es el valor de Pi", "Autor de la pintura La ultima cena", "¿Qué animal es la drosophila?"]
originals = [["Es el valor de Pi", "c"], ["Autor de la pintura La ultima cena", "a"], ["Qué animal es la drosophila?", "b"]]
answers = [["a.3.1014"], ["b.3.1410"], ["c. 3.1416"]], [["a. Leonardo da vinci"], ["b. Pablo Picasso"], ["c. Vincent"]], [["a. cabra"], ["b. mosca"], ["c. rata"]]        #List of answers for each question
selected_answers = [] #Contains selected answers
random.shuffle(questions)
random.shuffle(answers[0])
random.shuffle(answers[1])
random.shuffle(answers[2])
question = 0
while question < 4:
    if questions[0] == "Es el valor de Pi":
        print ("Question 1")
        print (answers[0][0], answers[0][1], answers[0][2])
        chosen = input("Enter 1 for the first answer, 2 for the second answer and 3 for the third one.")
        selected_answers.append(chosen)
        del questions[0]
        question += 1
        
    elif questions[0] == "Question 2":
        print ("Question 2")
        print (answers[1][0], answers[1][1], answers[1][2])
        chosen = input("Enter 1 for the first answer, 2 for the second answer and 3 for the third one.")
        selected_answers.append(chosen)
        del questions[0]
        question += 1
            
    elif questions[0] == "Question 3":
        print ("Question 3")
        print (answers[2][0], answers[2][1], answers[2][2])
        chosen = input("Enter 1 for the first answer, 2 for the second answer and 3 for the third one.")
        selected_answers.append(chosen)
        del questions[0]
        question += 1
