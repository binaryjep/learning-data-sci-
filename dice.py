import numpy as np 

np.random.seed(123)
step = 50 

dice = np.random.randint(1,7)

if dice <= 2: 
    
    step -= 1 

elif dice <=5 and dice > 2: 

    step += 1 

else: 

    step = step + np.random.randint(1,7)

print("You rolled " + str(dice))
print("You are at step " + str(step))