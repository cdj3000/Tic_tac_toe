


import numpy as np
import random
class TicTacToe:
    def __init__(self,size=5):
        self.size=size
        self.board=np.zeros([self.size,self.size])
        self.score=np.zeros([self.size, self.size])

    def move(self,a, player):
        # a is a tuple(row, col ), player=
        row, col= a
        player_temp=np.array(['x','o'])

        if player=='x':
            mark=1
        elif player=='o':
            mark=-1
        self.board[row,col]=mark
        if player =='o':
            return 'x'
        if player =='x':
            return 'o'

        
    def clean_board(self):
        self.board=np.zeros([self.size,self.size])
    def clean_score(self):
        self.score=np.zeros([self.size, self.size])
        
        
    
    def visualize(self):
        print('\n')
        print(self.board)

    def get_board(self):
        return self.board

        
    def get_score(self):
        print('\n')
        print(self.score)

    def check_v2(self):
        score_list=[]

        for i in range(self.size):
            score_list.append(np.sum(self.board[i,:]))
            score_list.append(np.sum(self.board[:,i]))

        score_list.append(np.sum(np.diagonal(self.board)))
        score_list.append(np.sum(np.diagonal(np.fliplr(self.board))))

        if self.size in score_list:
            return 'x'

        elif -self.size in score_list:
            return 'o'

        elif np.sum(self.board!=0) == self.size*self.size:
            return 'tie'

        else:
            return 'none'

    def best_move(self, player,num_iter=1000,alpha=1, belta=1 ):
        player_list=np.array(['o','x'])
        self.clean_score()
        board_copy= np.copy(self.board)
        

        for i in range(num_iter):
            current_player=player
            self.board=np.copy(board_copy)
            p_move_list=[]
            op_move_list=[]

            while self.check_v2()=='none':

                random_x,random_y= np.where( self.board==0)

                random_index= random.randint(0,len(random_x)-1)

                random_move=(random_x[random_index], random_y[random_index])
                #print('current_player ',current_player,'\n','take ', random_move)

                if current_player ==player:
                    p_move_list.append(random_move)
                else:
                    op_move_list.append(random_move)

                current_player=self.move(random_move,current_player)
           
            #print('final board:')
            #self.visualize()

            if self.check_v2()== player:
                #print('input player win')
                p_count=-1
                op_count=-1
                for move in p_move_list:
                    p_count+=1
                    self.score[move]+= 1*(alpha**(p_count))

                for move in op_move_list:
                    op_count+=1
                    self.score[move]+= -1*(belta**(op_count))

                #self.get_score()
            elif self.check_v2()== player_list[player_list!=player][0]:
                #print('opp player win')
                p_count=-1
                op_count=-1

                for move in p_move_list:
                    p_count+=1
                    self.score[move]+= -1*(belta**(p_count))
                for move in op_move_list:
                    op_count+=1
                    self.score[move]+= 1*(alpha**(op_count))
                #self.get_score()

        self.board=np.copy(board_copy)
        return np.unravel_index(np.argmax(self.score, axis=None), self.score.shape)

            

# a=TicTacToe(size=5)
# a.move([1,1],'o')

# a.move([1,0],'o')
# a.move([1,2],'o')
# a.move([1,3],'o')
# a.move([2,0],'x')
# a.move([2,1],'x')
# a.move([2,2],'x')
# a.move([2,4],'x')
# a.best_move('x',num_iter=2000)
a=TicTacToe(size=3)
# a.move([0,0],'x')
# a.move([0,1],'x')
# a.move([1,0],'o')
# a.move([1,1],'o')
a.move([0,0],'x')
a.move([0,2],'x')
a.move([1,1],'o')
a.move([1,2],'o')
c=a.best_move('x', num_iter=5000)
print(c)
# a.move([1,1],'x')

# a.move([1,0],'x')
# a.move([1,2],'x')
# a.move([1,3],'x')
# a.move([2,0],'o')
# a.move([2,1],'o')
# a.move([2,2],'o')
# a.move([2,4],'o')
# # a.best_move('x',num_iter=5000)
# a.get_score()
# # for i in range(50):
# #     m=a.mc_trial('x',[2,4],num_iter=1,alpha=1,belta=1)

# # m=a.mc_trial('o',[2,4],num_iter=5000,alpha=1,belta=1)  

# # a.get_score()
# # #a.move([2,3],'x')
# # print(m)
# # a.move([2,3],'x')
# # a.move([3,1],'x')
# # a.move([3,2],'o')
# # a.move([4,0],'o')
# # print(a.check([2,3]))
# a.visualize()

# # a.move([3,2],'x')
# # a.move([0,0], 'o')
# # a.move([1,0],'o')
# a.move([2,0],'o')
# a.move([3,0],'x')
# a.move([4,0],'o')
# a.move([3,1],'x')
# a.move([3,4],'x')
# m=a.mc_trial('o',[3,4],num_iter=1500,alpha=0.99)

# a.move([1,1], 'x')
# a.move([0,0], 'o')
# a.move([0,1],'x')
# a.mc_trial('o', [0,1], num_iter=10000,alpha=1)


# a.visualize()
# a.check([0,0])
# a.mc_trial('x',[0,0],num_iter=500)
# a.score
#a.board
#a.visualize()
#a.ai_player([0,0], 'x',num_iter=500)
# m=a.mc_trial('x',[0,0],num_iter=5000)
#a.get_score()

#print(m)