#!/usr/bin/env python
# coding: utf-8

# ## Tic Tac Toe Game
# Choose the character and place it on the board.
# 
# 3 same characters in the row wins the game.
# 
# Position on the game board corresponds with the numpad on the computer keyboard

# In[1]:


def display_board(board):
    board = [board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9]]    
   
    print(board[7],' | ',board[8],' | ',board[9])
    print('-------------')
    print(board[4],' | ',board[5],' | ',board[6])
    print('-------------')
    print(board[1],' | ',board[2],' | ',board[3])
    


# In[50]:


def player_input():
    while True:
        player1 = input("Please pick a marker 'X' or 'O'")
        print(player1)
        if player1 ==('X'):
            break
        elif player1=='O':
            break
        else:
            continue
    return player1


# In[51]:


def place_marker(board, marker, position):
    while True:
        if position == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            break
        else:
            continue
    board[position] = marker


# In[52]:


def clear(board):
    board[0], board[1], board[2], board[3] ,board[4] ,board[5] ,board[6] ,board[7] ,board[8], board[9] = ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ' 


# In[53]:


def win_check(board, mark):
    if ((board[1],board[2],board[3])==('X', 'X', 'X')) or ((board[4],board[5],board[6])==('X', 'X', 'X')) or ((board[7],board[8],board[9])==('X', 'X', 'X')) or ((board[1],board[5],board[9])==('X', 'X', 'X')) or ((board[3],board[5],board[7])==('X', 'X', 'X')) or ((board[7],board[4],board[1])==('X', 'X', 'X')) or ((board[8],board[5],board[2])==('X', 'X', 'X')) or ((board[9],board[6],board[3])==('X', 'X', 'X')):
        print('X WON!')
        return True
    elif ((board[1],board[2],board[3])==('O', 'O', 'O')) or ((board[4],board[5],board[6])==('O', 'O', 'O')) or ((board[7],board[8],board[9])==('O', 'O', 'O')) or ((board[1],board[5],board[9])==('O', 'O', 'O')) or ((board[3],board[5],board[7])==('O', 'O', 'O')) or ((board[7],board[4],board[1])==('O', 'O', 'O')) or ((board[8],board[5],board[2])==('O', 'O', 'O')) or ((board[9],board[6],board[3])==('O', 'O', 'O')):
        print('O WON!')
        return True
        


# In[54]:


def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False


# In[55]:


def full_board_check(board):
    if ((board[1]!=' ') and (board[2]!=' ') and (board[3]!=' ') and (board[4]!=' ') and (board[5]!=' ') and (board[6]!=' ') and (board[7]!=' ') and (board[8]!=' ') and (board[9]!=' ')):
        print('nobody won the game')
        return True
    else:
        return False


# In[56]:


def input_check():
    import string
    
    while True:
        position = input('Please enter a number 1-9')
        if position in string.ascii_lowercase:
            print('Enter a NUMBER!')
            continue
        elif position in string.ascii_uppercase:
            print('Enter a NUMBER!')
            continue
        else:
            if int(position) in range(1,10):
                position = int(position)
                print('\n')
                return position
            else:
                print('Wrong position number, choose from 1-9 range')
                continue
    


# In[57]:


def player_choice(board):
    import string
    
    position = input_check()
  
    while space_check(board, position) == False:
        print('This position is not avaiable')
        position =  input_check()
    return position 
    
    


# In[60]:


print('Welcome to Tic Tac Toe!')
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 

while True:
    clear(board)
    
    while True:
        display_board(board)
        
        if win_check(board, marker) == True:
            break
        if full_board_check(board) == True:
            break
        
        marker = player_input()
        position = player_choice(board)
        place_marker(board,marker,position)
    
    
    if not replay():
        break
    


# In[ ]:




