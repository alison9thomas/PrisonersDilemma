#Common base class for all Player0
class Player3:
    
   #This is the constructor for the class. It helps to allocate, instantiate,
   #each child in memory, and initializes the data members of the child object,
   #in this example, data members are model, color and passengerseats, mpg
   def __init__(self):
       pass
       
       
    
   #Defining functions for each child(instance) of class Car
   def strategy(self,history, opponent_history, score, opponent_score, getting_team_name):
        if getting_team_name:
            return 'loyal vengeful'
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            if len(opponent_history)==0: # betray is they were severly punished last time 
                return 'b'
            elif len(opponent_history)==1:
                if history[-1]=='c' and opponent_history[-1]=='b':
                    return 'b' # betray is they were severely punished last time
                    
            elif len(opponent_history)>=2:
                if history[-1]=='c' and opponent_history[-2]=='b':
                    return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude
