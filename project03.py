'''Assignment 3, Jordan Sinclair, BOGGLE!!!'''

import random

#Function to create a new 2D array for the boggle board and
#to initialize it with random letters. 
def new_board():
    #Array with the letters in the alphabet
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                'U', 'V', 'W', 'X', 'Y', 'Z']
    board = [] #Creates a list for the board. 
    for r in range(4): #We always want a 4 x 4 matrix 
        row = [] #List for the board's rows
        for c in range(4): #Loops through the columns
            #Gets a random number between 0 and 25 in order to choose
            #a random letter. Casts to an integer because random will
            #give a double (it will have decimal points). 
            num_letter = int(random.random() * 25)
            #The actual letter is the position in the alphabet list
            #that corresponds the random integer, num_letter. 
            letter = alphabet[num_letter]
            #appends the generated letter to the list of rows. 
            row.append(letter)
        #Appends the row list to the board (creating a 2D matrix)
        board.append(row) 
    return board #Returns the randomly generated, 4 x 4 board. 

#Prints the board in a formatted, string version. 
def board_to_string(board):
    s = "" #Creates an empty string to store the formatted board
    for i in range(len(board)): #Loops through the board's columns
        for j in range(len(board[i])): #Loops through the board's rows
            #The following statements determine the formatting for the
            #board. 
            #For the first three rows, the ending should be a 
            # bracket and an enter,
            #rather than a bracket and a space for the rest of the row. 
            if j == len(board[i]) - 1 and i <= 2:
                s = s + "[" + board[i][j] + "]\n"
            #Otherwise, if it is the last row, the ending should 
            # just be a bracket. 
            elif j == len(board[i]) - 1 and i == 3:
                s = s + "[" + board[i][j] + "]"
            #If the position is not at the end of a row, then the ending
            #should be a space with a bracket. 
            else:
                s = s + "[" + board[i][j] + "] "
    print(s) #Prints the board with the appropriate formatting
    return s #Returns the board string 

#Function to find the valid diagonal cells to the input position. 
def diagonals(current_cell):
    x, y = current_cell #Gets the x and y positions from the given tuple. 
    pos = [] #Creates an empty list to store the valid x,y positions. 
    if x+1 < 4 and y-1 >= 0: #If the downard right diagonal is within the board, 
        #Add that position to the list of possibilities.
        pos = pos + [(x+1, y-1)]  
    #If the downward left diagonal is within the board,
    if x-1 >= 0 and y-1 >= 0: 
        pos = pos + [(x-1, y-1)] #Add it to the list of possibilities. 
    if x+1 < 4 and y+1 < 4: #If the upward right position is within the board,
        pos = pos + [(x+1, y+1)] #add it to the list of options. 
    if x-1 >= 0 and y+1 < 4: #If the upward left position is within the board,
        #add that position to the list of possibilities. 
        pos = pos + [(x-1, y+1)] 
    return pos #Returns the list of valid diagonal positions

#Similar to the above function, this one defines the valid 
# horizontal/vertical cells given an input position
def sides(current_cell):
    x, y = current_cell #Gets the x and y coordinates from the given tuple. 
    pos = [] #Creates an empty list to store the valid x,y positions. 
    if x-1 >= 0: #If the left position is valid,
        pos = pos + [(x-1, y)] #add it to the list of possibilities
    if y+1 < 4: #if the top position is valid,
        pos = pos + [(x, y+1)] #add it to the list of options
    if x+1 < 4: #if the right position is valid,
        pos = pos + [(x+1, y)] #add it to the list of options
    if y-1 >= 0: #if the bottom position is valid,
        pos = pos + [(x, y-1)] #add it to the list of possibilities
    #Returns the list of valid vertical/horizontal positions
    return pos 

#Determines the full list of adjacent cells using the above two functions. 
def adjacent_cells(current_cell):
    #List to store the coordinates (as tuples) of the 
    # valid positions for the current cell. 
    coords = [] 
    #Adds the valid horizontal/vertical positions.
    coords = coords + sides(current_cell) 
    #Adds the valid diagonal positions.
    coords = coords + diagonals(current_cell)  
    return coords #Returns the list of tuples representing the usable cells. 

#This function determines all of the cells that contain a certain letter. 
def cells_with_letter(board, letter):
    #Empty list to store the coordinates where the letter can be found.
    coords = []  
    l = letter.upper() #Copies the input letter and sends it to uppercase. 
    for i in range(len(board)): #Loops through the board's rows
        for j in range(len(board[i])): #Loops through the board's columns
            if board[i][j] == l: #If the board contains the letter
                #adds the position of the cell to the coordinates list.
                coords.append((j,i))  
    #Returns the list of tuples representing the coordinates
    #  of each cell with the given letter
    return coords 

#This function establishes if the board contains a given word
#  using a recursive, depth first search, algorithm. 
def board_has_word(board, word, used_cells=None):
    word = word.upper() #Sends the word to uppercase to match the board. 
    if used_cells is None: #If there are no used cells 
        #The starting cells indicate all of the options for the first
        #  letter of the word. 
        starting_cells = cells_with_letter(board, word[0]) 
        #If there is one letter and that letter can be found on the board
        if len(word) == 1 and len(starting_cells) is not 0 :
            return True #Return true (there is only one letter)!
        #If there is not any case of the first letter on the board
        if not starting_cells: 
            return False #Return false because we can't go any further. 
        if len(word) > 1: #If the word is longer than one letter,
            for s in starting_cells: #Loops through the available starting cells
                #Recursively searches for the next letter in 
                # the word using the starting cells as the used letters. 
                # (Goes through the case in which used cells are given.)
                if board_has_word(board, word[1:], [s]):
                    #If the rest of the word was found using this
                    #  recursive method,
                    return True
            #Otherwise, the at least one of the letters in the worD
            # Must have not been found.
            return False  

    elif used_cells is not None: #If there are used cells,
        current_cell = used_cells[-1] #Starts with the last used cell
        #Finds the neighbors of the last used cell (the one we're on)
        neighbors = adjacent_cells(current_cell) 
        #Determines which of the neighbors haven't been used already. 
        neighbors = [c for c in neighbors if c not in used_cells ]
        #Removes the neighbors that don't have the letter we're searching for. 
        neighbors = [ c for c in neighbors if word[0] == board[c[1]][c[0]] ]

        #If the length of neighbors is 0, the word is not on the board.
        if not neighbors:  
            return False
        if len(word) == 1: #If the word has only one letter
            #Return true becuase we know that the letter is already a neighbor.
            return True 
        if len(word) > 1: #If the length of the word is greater than 1,
            for n in neighbors: #Loops through the available neighbors. 
                #Continues the recursive search with the next
                #  letter in the word. 
                return board_has_word(board, word[1:], used_cells + [n])
    return False

#Example game implementation:
b = new_board() #Creates a new board
board_to_string(b) #Converts the board to a string and prints it. 

search = input("Enter a word to search for: ") #Starts the search input. 
points = 0 #Variable to store the user's score in the game. 

while search != "end": #Keeps going until the user types end
    if board_has_word(b, search): #If the word is found
        print("You found a word!") #Prints "You found a word!"
        #Updates the points to add the length of the word found (simpler
        #  version of the actual point structure in Boggle)
        points = points + len(search) 
    else: #if the word was not found,
        print("That word wasn't found. ") 
    search = input("Enter another word to search for: ") #Restarts the search. 
#If the user types end, 
print("You ended the game. ") #Game ended
print("Your score was: ", points) #Prints the total score calculated above. 
