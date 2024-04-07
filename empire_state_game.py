import numpy as np
import matplotlib.pyplot as plt 

np.random.seed(123)
all_random_walks = [] # initialize an empty list that will store all the random walks (500)

for i in range(500): # we will perform the game for the random walk 500 times to make sure we have enough data

    random_walk = [0] # set random walk to 0 as that's the first step we'll be starting at 

    for j in range(100): # the random walk will come from 100 dice rolls

        step = random_walk[-1] # initialize our current step to the final value of the random walk
        dice = np.random.randint(1,7) # roll the dice with value from 1-6 

        if dice <= 2: # if dice is 1 or 2, the step will decrement. however, if the value of step is between 0 and a negative number, we'll choose 0 
            #as we can't have a negative step value 

            step = max(0, step - 1)

        elif dice <= 5: # if dice is equals to 3-5 then we increment our step

            step = step + 1 

        else: # if dice is equals to 6, then we'll increment it by whatever a new dice roll will give us

            step = step + np.random.randint(1,7)
        
        if np.random.rand() <= 0.001: # if we somehow fall on a step with a 0.1% chance, we must reset to step 0. 

            step = 0 

        random_walk.append(step) # append the step to the random walk 
    
    all_random_walks.append(random_walk) #append the finished random walk to all random walks 

arwt = np.transpose(np.array(all_random_walks)) #swap the rows and columns of all_random_walks which is now an np array also

arwt_ends = arwt[-1, :] #access the endpoint or last step of the 500 random walks.

plt.hist(arwt_ends) #plot all the end step to a histogram 
plt.show() #show the histogram 

 


