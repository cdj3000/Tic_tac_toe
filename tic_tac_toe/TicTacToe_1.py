import numpy as np
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
        #print(player_temp!=player)
        #print(self.board)
        return player_temp[player_temp!=player][0]
        
    def clean_board(self):
        self.board=np.zeros([self.size,self.size])
    def clean_score(self):
        self.score=np.zeros([self.size, self.size])
        
        
    
    def check(self, recent):
        recnet_x, recnet_y= recent
        if (np.sum(self.board[:,recnet_y])==self.size) or ( np.sum(self.board[recnet_x,:])==self.size) or (np.sum(np.diagonal(self.board))== self.size) or (np.sum(np.diagonal(np.fliplr(self.board)))== self.size ):
            return 'x'
        if (np.sum(self.board[:,recnet_y])== -self.size) or (np.sum(self.board[recnet_x,:])== -self.size) or (np.sum(np.diagonal(self.board))== -self.size) or (np.sum(np.diagonal(np.fliplr(self.board)))== -self.size ):
            return 'o'
        if np.sum(self.board!=0) == self.size*self.size:
            return 'tie'
        
        return 'none'
    
    def visualize(self):
        print('\n')
        print(self.board)
    def update_score(self,pos, num):
        row,col=pos
        self.score[row,col]+=num
        return
    def get_board(self):
        return self.board
    
    def ai_player(self,player,last_move, num_iter=500, alpha=0.99):
        temp_last_move=last_move
        
        
        #print(self.check(temp_last_move))
        
        while self.check(temp_last_move)=='none':
            
            #self.visualize()
            temp_last_move=self.mc_trial(player, temp_last_move, num_iter,alpha)
            #print(temp_last_move)
            #self.visualize()
            
            player= self.move(temp_last_move, player)
            #print(1)
            self.visualize()
            #print('next')
            
        print(self.check(temp_last_move))

        
    def get_score(self):
        print('\n')
        print(self.score)

    def mc_trial(self,player,last_move,num_iter=30,alpha=0.9, belta=0.9):
        # given board, player return best move
        """
        last_player == recent
        player = next move
        """
        player_option=['x','o']
        board_copy =self.board.copy()
        self.clean_score()

        for i in range(num_iter):
            self.board=board_copy.copy()
            player_temp=player
            temp_last_move=last_move
            
            player_history=[]
            opp_history=[]
            
            while self.check(temp_last_move)=='none':
                # random_Walk
                x,y=np.where(self.board ==0 )
                random_select= np.random.choice(len(x))
                player_temp = self.move((x[random_select],y[random_select]), player_temp)
                temp_last_move=(x[random_select], y[random_select])
                # print(player_temp,' move ',(x[random_select], y[random_select]), 'then', self.check(temp_last_move))
                # self.visualize()
                if player_temp != player:
                    player_history.append((x[random_select], y[random_select]))
                else:
                    opp_history.append((x[random_select], y[random_select]))
            
#             print(player_history)
#             print(opp_history)
            
            if self.check(temp_last_move)== player:
#                 self.score[player_history[0]]+= +1
#                 self.score[opp_history[0]]+=-1
#                 print(self.check(temp_last_move))
                #print(player,' win')
                count_p_move=-1
                count_op_move=-1
                for move in player_history:
                    count_p_move+= 1
                    self.score[move]+= 1*((alpha)**count_p_move)
                for move in opp_history:
                    count_op_move+=1
                    self.score[move]+= -1*((belta)**count_op_move)
   
            elif self.check(temp_last_move) == player_option[player_option!=player][0]:
#                 self.score[player_history[0]]+= -1
#                 self.score[opp_history[0]]+=1
                #print(self.check(temp_last_move))
                #print(player_option[player_option!=player][0], ' win')
                count_p_move=-1
                count_op_move=-1
            
                for move in player_history:
                    count_p_move+=1
                    self.score[move]+= -1*((belta)**count_p_move)

                for move in opp_history:
                    count_op_move+=1
                    self.score[move]+= 1*((alpha)**count_op_move)
                
            
            elif self.check(temp_last_move)=='tie':
                pass
        self.board=board_copy.copy()
        return  np.unravel_index(np.argmax(self.score, axis=None), self.score.shape)
        
            

a=TicTacToe(size=3)
a.move([0,0],'o')
a.move([0,1],'o')
a.move([1,0],'x')
a.move([1,1],'x')
a.visualize()
# a.move([1,1],'o')
# # a.ai_player('o',[1,1],num_iter=50000)
# a.move([1,0],'o')
# a.move([1,2],'o')
# a.move([1,3],'o')
# a.move([2,0],'x')
# a.move([2,1],'x')
# a.move([2,2],'x')
# a.move([2,4],'x')

# # for i in range(50):
# #     m=a.mc_trial('x',[2,4],num_iter=1,alpha=1,belta=1)

# m=a.mc_trial('o',[1,1],num_iter=5000,alpha=1,belta=1)  

# a.get_score()
# #a.move([2,3],'x')
# print(m)
# # a.move([2,3],'x')
# # a.move([3,1],'x')
# # a.move([3,2],'o')
# # a.move([4,0],'o')
# # print(a.check([2,3]))
# a.visualize()

# # a.move([3,2],'x')
# # a.move([0,0], 'o')
# # a.move([1,0],'o')
# # a.move([2,0],'o')
# # a.move([3,0],'x')
# # a.move([4,0],'o')
# # a.move([3,1],'x')
# # a.move([3,4],'x')
# # m=a.mc_trial('o',[3,4],num_iter=1500,alpha=0.99)

# # a.move([1,1], 'x')
# # a.move([0,0], 'o')
# # a.move([0,1],'x')
# # a.mc_trial('o', [0,1], num_iter=10000,alpha=1)


# # a.visualize()
# # a.check([0,0])
# # a.mc_trial('x',[0,0],num_iter=500)
# # a.score
# #a.board
# #a.visualize()
# #a.ai_player([0,0], 'x',num_iter=500)
# # m=a.mc_trial('x',[0,0],num_iter=5000)
# #a.get_score()

# #print(m)


