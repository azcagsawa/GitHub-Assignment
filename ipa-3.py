#!/usr/bin/env python
# coding: utf-8

# In[146]:


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # we want to know the relationship of two users
    
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "friends"
        
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    
    else: 
        return "no relationship"
        
social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
} 


# In[147]:


relationship_status("@chums", "@joaquin", social_graph)


# In[102]:


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may be 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    # for 3x3
    
    size = len(board)
    
    if size in [3,4,5,6]:
        
        # row checker 
        
        for row in board:
            x_row_checker = 0
            o_row_checker = 0
            for each in row:
                if each == "X":
                    x_row_checker += 1
                    if x_row_checker == size:
                        return "X"
        
                elif each == "O":
                    o_row_checker += 1
                    if o_row_checker == size:
                        return "O"
             
                        
        # column checker
    
        for col in range(size): # 0 1 2 
            x_col_counter = 0
            o_col_counter = 0 
        
            for each in range(size): # 0 1 2 
                if board[each][col] == "X":
                    x_col_counter += 1
                    if x_col_counter == size:
                        return "X"
                elif board[each][col] == "O":
                    o_col_counter += 1
                    if o_col_counter == size:
                        return "O"
                
                        
        # diagonal checker
        
        x_diag_counter = 0 
        o_diag_counter = 0
            
        for diag1 in range(size): # main diagonal
            if board[diag1][diag1] == "X":
                x_diag_counter += 1
                if x_diag_counter == size: 
                    return "X"
            elif board[diag1][diag1] == "O":
                o_diag_counter += 1 
                if o_diag_counter == size:
                    return "O"

        x_diag_counter = 0 
        o_diag_counter = 0   
        
        for diag2 in range(size): # reverse diagonal
            if board[diag2][size - diag2 - 1] == "X":
                x_diag_counter += 1
                if x_diag_counter == size:
                    return "X"
            elif board[diag2][size - diag2 - 1] == "O":
                o_diag_counter += 1
                if o_diag_counter == size:
                    return "O"
                
    return "NO WINNER"
        
    
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','',''],
]
    
board8 = [
['X','O','O'],
['X','O','O'],
['O','','X'],
]



# In[103]:


tic_tac_toe(board7)


# In[246]:


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    for each in route_map:
        if first_stop == each[0] and second_stop == each[1]:
            current_mins = route_map[first_stop,second_stop]
            return "it will take " + str(current_mins[ "travel_time_mins"]) + " mins to travel from " + first_stop + " to " + second_stop
        else:
            continue
    return "no known travel time"
    
legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}


# In[247]:


eta("dlsu","upd",legs)


# In[ ]:




