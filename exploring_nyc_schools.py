import pandas as pd 

# Read schools file 

df = pd.read_csv('datasets\schools.csv')

# Filter schools with average math score >= 640
best_math_schools = df[df['average_math'] >= 640][['school_name', 'average_math']]

# Sort the best math schools in descending order 
best_math_schools = best_math_schools.sort_values('average_math', ascending=False)

# Display results
print(best_math_schools)

# Create new column for total_SAT combining all scores
df['total_SAT'] = df['average_reading'] + df['average_writing'] + df['average_math']

# Filter top 10 schools with highest SAT scores 
top_10_schools = df.sort_values('total_SAT', ascending=False)[['school_name', 'total_SAT']].head(10)

# Display results
print(top_10_schools)

# Group the schools by borough and calculate the number of schools, mean of SAT, and std of SAT per borough
boroughs = df.groupby('borough')['total_SAT'].agg(['count', 'mean', 'std' ]).round(2)

# Create a dataframe containing the borough with the largest std_SAT
largest_std_dev = boroughs[boroughs['std'] == boroughs['std'].max()]

# Rename the columns for clarity 
largest_std_dev= largest_std_dev.rename(columns={'count': 'num_schools', 'mean': 'average_SAT', 'std': 'std_SAT'})

# Display results 
print(largest_std_dev)

