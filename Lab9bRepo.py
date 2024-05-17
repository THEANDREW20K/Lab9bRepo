# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:04:50 2024

@author: ganne
"""
#Agent class must know if it's happy, know how to move, and be able to locate
#neighbors 

#World class has to know a lot of things, I think it's essentially just 
#tracking the dictionary that we use to create coordinates? And also creating
#Agents, and also determining some of the Agent's behavior

#have a paramater thing with objects the class uses:
    #dict:
        
        
thing = {"world_size":(20, 20)}  #I think this is just a dictionary that 
#contains a key that says "world_size" and a value that is just a tuple       

params = {1:(1, 2, 3), 2:(1, 2, 3), 3:(1, 2, 3)}
 
#maybe I could cycle through the tuples to produce unique output? 

#examining some of the professor's code:
    
    def locate_neighbors(self, loc):
       """given a location, return a list of all the patches that count as neighbors"""
       include_corners = True # a keyword argument

       x, y = loc  #how does the loc thing work?
       cardinal_four = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
       #I think this is meant to allow for variation in the coordinates? 
       if include_corners:
           corner_four = [(x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]
           neighbors = cardinal_four + corner_four
      #testing out adding these objects
       else:
           neighbors = cardinal_four

#the test
cardinal_four = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

corner_four = [(x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]
neighbors = cardinal_four + corner_four
#perhaps these can only be added as local variables


class Agent():
    def _init_(self):
       pass
   
    def move(self):
       if params != 1: 
        return("move")
       pass
   
    def locate_empty_path(self):
        pass
    
    
class World():
    def _init_(self):
        pass
    
    def build_grid(self):
        
        pass
    
    def init_world(self):
        pass
    
    def build_agents(self):
        pass
    
    def find_vacant(self):
        pass
    
    def run(self):
        pass