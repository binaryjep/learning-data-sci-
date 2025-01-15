import numpy as np 

x = np.array([0,4,4])

for j in x: 

    print(str(j) +' km')

apples = [[9,25,33],
          [16,19,16],
          [25,37,15]]

for x in apples:
    print(x[2])

stocks = {'Apple': 'AAPL', 'Amazon': 'AMZN'}

for p, q in stocks.items(): 
    print(str(q) + ' is ' + str(p))

