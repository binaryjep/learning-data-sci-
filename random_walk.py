import numpy as np
import matplotlib.pyplot as plt 

np.random.seed(123) # provide a random seed 

random_walk = [0] # initialize random walk to 0 

for x in range(100): # perform the roll of dice and step/walk update for each iteration (100 times)

    step = random_walk[-1] # initialize step to the last item in the random walk list 

    dice = np.random.randint(1,7) # roll the dice between 1 and 6 

    if dice <= 2: # if dice is 1 or 2, decrease the step by 1 or choose 0 if it comes to a negative value 

        step = max(0, step - 1)

    elif dice <= 5: # if dice is less than or equal to 5, increment the step by 1 

        step += 1 

    else: # if the dice is equals to 6, roll the dice again and increment the number to the current value of step

        step = step + np.random.randint(1,7)

    random_walk.append(step) #append the new step to the random walk 

plt.plot(random_walk) #plot the random walk 

plt.show() # show the plot of random walk 