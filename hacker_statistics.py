import numpy as np 
import matplotlib.pyplot as plt 

np.random.seed(123)
all_random_walks = [] # empty list to store all the games of hacker statistic 

for x in range(500): 

    random_walk = [0] # will keep track of each step that you make after each roll of the dice. will start at 0. 

    for y in range(100): 

        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2: 

            step = max(0, step - 1)

        elif dice <= 5: 

            step = step + 1 

        else: 

            step = step + np.random.randint(1,7)
        
        if np.random.rand() <= 0.001: 

            step = 0 

        random_walk.append(step)
    
    all_random_walks.append(random_walk)


arwt = np.transpose(np.array(all_random_walks))

arwt_ends = arwt[-1, :]

plt.hist(arwt_ends)
plt.show()