#this program is meant for creating quizes with random order and random wrong answers
#this is for making each exam completely differente from one another
import random
import json
import os
import time

def createquiz(quiznum):
    now = list(time.localtime()) #setting the current date
    foldername = 'quizes {}-{}-{}'.format(now[0],now[1],now[2]) #variable folder name based on date

    with open('capital.json') as f: #reading the json file for creating a local dict
        stateCapital = json.load(f) 

    if not os.path.exists(foldername): #create new dir based on the current date if does not exist
        os.makedirs(foldername)

    state = list(stateCapital.keys()) #states

    answers = {}#the answers file
    for i in range(quiznum):

        random.shuffle(state) #shuffeling states

        #creating the quizes files
        with open(foldername + '/' +'quizfile {}.txt'.format(i + 1),'w') as f:
            f.write('Name:\n\nDate:\n\nPeriod:\n\n')
            f.write((' ' * 20) + 'State capital quiz (form {})'.format(i + 1))
            f.write('\n\n')
            answers['file %s' %(quiznum)] = []
            for qnum in range(50): #create 50 random questions for each of the files with random options and one correct answer    
                correctAnswer = stateCapital[state[qnum]]
                wrongAnswer = list(stateCapital.values())
                del wrongAnswer[wrongAnswer.index(correctAnswer)]
                wrongAnswer = random.sample(wrongAnswer,3)
                answerOptions = [correctAnswer] + wrongAnswer
                random.shuffle(answerOptions)
                f.write('%s. What is the capital of %s? \n\n' %(qnum,state[qnum]))
                for i in range(4):
                    f.write('\n  %s) %s' %('ABCD'[i],answerOptions[i]))
                f.write('\n\n')
                answers['file %s' %(quiznum)].append(('Answer for question %s' %(qnum+1),'ABCD'[answerOptions.index(correctAnswer)]))

    with open(foldername + '/answers.json','w') as f: #writing the answers json file
        json.dump(answers,f)

try:
    createquiz(10)
except ValueError as v:
    print('error found!',v)

print('done!')
        
