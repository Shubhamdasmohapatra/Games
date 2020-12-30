import random
def game_rps():
    
    while True:

        lst = ['Rock','Paper','Scissor']
        input1 = input('Rock/Paper/Scissor ?')
        print(f'The user has chosen :{input1}')
        input2 = random.choice(lst)
        print(f'The Computer has chosen :{input2}')

        if input1 == input2:
            print('It is a draw')
        elif ((input1 =='Rock' and input2 == 'Scissor') or (input1 == 'Paper' and input2 == 'Rock') or (input1 == 'Scissor' and input2 == 'Paper')):
            print('User wins')
        else:
            print('Computer wins')
    
game_rps()