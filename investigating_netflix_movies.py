import pandas as pd 
import matplotlib.pyplot as plt 

netflix_df = pd.read_csv("datasets\netflix_data.csv", index_col=0) # import csv file as dataframe using pandas
netflix_subset = netflix_df[netflix_df["type"] == "Movie"] #subset the dataframe to only include those whose type is a movie
netflix_movies = netflix_subset.loc[:, ["title", "country", "release_year", "duration", "genre"]] #only include columns for title, country, release year and duration
short_movies = netflix_movies[netflix_movies["duration"] < 60] #examine the movies whose duration is shorter than 60 minutes

colors = [] #empty list to assign colors 

for label, movie in netflix_movies.iterrows(): # iterate through the netflix movies dataframe

    if movie["genre"] == "Children": # if the movie row's genre is "Children", assign or append a color of red 

        colors.append("red")

    elif movie["genre"] == "Documentaries": # if the movie row's genre is "Documentation", assign or append a color of green 

        colors.append("green")

    elif movie["genre"] == "Stand-Up": # if the movie row's genre is "Stand-up, assign or append a color of blue 

        colors.append("blue")

    else: #any other genre receives gray color

        colors.append("gray")
    
plt.figure(figsize= (10,10), dpi = 100, tight_layout = True )
plt.scatter(netflix_movies["release_year"], netflix_movies["duration"], color = colors)
plt.xlabel("Release Year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")
plt.show()

answer = "no"
