import matplotlib.pyplot as plt
import model

def visualizer(df):

    # Define an empty list
    colors = []

    # Iterate over rows of netflix_movies_col_subset
    for lab, row in df.iterrows():
        if row['genre'] == "Children":
            colors.append("red")
        elif row['genre'] == "Documentaries":
            colors.append("blue")
        elif row['genre'] == "Stand-Up":
            colors.append("green")
        else:
            colors.append("black")

    # Set the figure style and initalize a new figure
    plt.style.use('fivethirtyeight')
    fig = plt.figure(figsize=(12,8))

    # Create a scatter plot of duration versus release_year
    plt.scatter(df['release_year'],df['duration'],c=colors)

    # Create a title and axis labels
    plt.xlabel('Release year')
    plt.ylabel('Duration (min)')
    plt.title('Movie duration by year of release')  

    plt.savefig('vis.png')     

    model.clustering(df)