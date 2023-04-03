#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Define Vacuum Cleaner
class cleaner:                           #Here is created initialization method in my cleaner class
   def __init__(self, a, b):
       self.a = a                       #{self.a = attribute where a = parameter}
       self.b = b                       #{self.b = attribute where b = parameter}
  
   def move_left(self, environment):    #it is used to move the cleaner one unit left
       if self.b > 1:
           self.b -= 1
           self.clean(environment)      #there have two attributes "self.b" and "self.clean(), its takes argument "environment"
          
      
   def move_right(self, environment):   #it is used to move the cleaner one unit right
       if self.b < len(environment[0]):
           self.b += 1
           self.clean(environment)      #there have two attributes "self.b" and "self.clean(), its takes argument "environment"
           
      
   def move_up(self, environment):      #it is used to move the cleaner one unit up
       if self.a > 1:
           self.a -= 1
           self.clean(environment)      #there have two attributes "self.a" and "self.clean(), its takes argument "environment"
           
          
   def  move_down(self, environment):   #it is used to move the cleaner one unit down
       if self.a < len(environment[0]):
           self.a += 1
           self.clean(environment)      #there have two attributes "self.a" and "self.clean(), its takes argument "environment"
           
          
   def clean(self, environment):        #it is used to check the cell if it is dirty, it will clean the cell by updaing it dirty to "clean"
       if environment[self.a-1][self.b-1] == "dirty":
           environment[self.a-1][self.b-1] = "clean"
           
  
   def get_environment_with_cleaner(self, environment):        #it is used get the environment after cleaning process
       new_environment = [row.copy() for row in environment]
       new_environment[self.a-1][self.b-1] += "*"
       return new_environment
  
   def is_goal_state(environment):      #it is used check the environment clean or not clean
       for row in environment:
           if "dirty" in row:
               return False
       return True
           
      
#Define Manual Agent
class ManualAgent:                        #Here is created input function "get_action" then returns the string by the user
   def get_action(self):
       action = input("Enter action (left, right, up, down, clean): ")
       return action
  

#Define Auto Agent
class AutoAgent:                          #Here is created auto function, once get command from user cleaner will be moving in a zigzag pattern from left to right and down untill all the cells are cleand
   def get_action(self, environment, cleaner):
       if environment[cleaner.a-1][cleaner.b-1] == "dirty":
           return "clean"
       else:
           if cleaner.a % 2 == 1:
               if cleaner.b < len(environment[0]):
                   return "right"
               else:
                   return "down"
           else:
               if cleaner.b > 1:
                   return "left"
               else:
                   return "down"

def get_integer_input(prompt):             #its takes parameter prompt
   while True:                            #Here user need to put positive value otherwise it will show "Sorry, invalid value"
       try:
           value = int(input(prompt))
           if value > 0:
               return value
       except ValueError:
           print("Sorry, invalid value. Enter a positive integer.")
       

#Define the goal test function
def is_goal_state(environment):
   for row in environment:
       if "dirty" in row:
           return False
   return True

def get_coordinate_input(prompt):         #its takes parameter prompt
   while True:                           #Here user need to put positive coordinates in the format a,b otherwise it will show "Sorry, invalid value"
       try:
           value = input(prompt)
           if value == 's':
               return value
           a, b = map(int, value.split(","))
           if a > 0 and b > 0:
               return a, b
       except ValueError:
           print("Sorry, invalid value. Enter a positive coordinates in the format a,b.")

#Define environment as a 2D array        
def create_environment(n):
   environment = []
   for i in range(n):
       row = []
       for j in range(n):
           row.append("clean ")
       environment.append(row)
   return environment

def mark_dirt(environment, a, b):
   environment[a-1][b-1] = "dirty"

def display_environment(environment):
   n = len(environment)
   # Print the top border of the table
   print("+{}+".format("--" * (n * 3 + n + 1)))
   # Print each row of the table
   for row in environment:
       print("| {} |".format(" | ".join(row)))
   # Print the bottom border of the table
   print("+{}+".format("--" * (n * 3 + n + 1)))

n = get_integer_input("Enter the size of the  environment: ")
environment = create_environment(n)

while True:                         #Here user need to put the location of dirty as positive coordinates in the format a,b
   dirt_location = get_coordinate_input("Enter the location of the dirt (or type 's' to stop): ")
   if dirt_location == "s":
       break
   mark_dirt(environment, dirt_location[0], dirt_location[1])

display_environment(environment)    #Here user need to select "agent_type" manual either auto
agent_type = input("Enter agent type (manual or auto): ")
if agent_type == "manual":
   agent = ManualAgent()
elif agent_type == "auto":
   agent = AutoAgent()
else:
   print("Invalid input. Please enter 'manual' or 'auto'.")
   exit()

start_location = get_coordinate_input("Enter start location of the cleaner: ")        #Here user need to put the location of start
cleaner = cleaner(start_location[0], start_location[1])

#Repeat until the goal is achieved
while not is_goal_state(environment):
   display_environment(cleaner.get_environment_with_cleaner(environment))
   if isinstance(agent, ManualAgent):
       action = agent.get_action()
   elif isinstance(agent, AutoAgent):
       action = agent.get_action(environment, cleaner)
   else:
       print("Invalid agent type.")
       exit()
   if action == "left":
       cleaner.move_left(environment)
       print("Cleaner moved left.")
   elif action == "right":
       cleaner.move_right(environment)
       print("Cleaner moved right.")
   elif action == "up":
       cleaner.move_up(environment)
       print("Cleaner moved up.")
   elif action == "down":
       cleaner.move_down(environment)
       print("Cleaner moved down.")
       cleaner.move_left(environment)
   elif action == "clean":
       cleaner.clean(environment)
       print("clean")
      
   else:
       print("Invalid action. Try again.")


print("Whole environment is cleaned")

display_environment(environment)


# In[ ]:





