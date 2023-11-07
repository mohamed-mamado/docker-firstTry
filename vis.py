import matplotlib.pyplot as plt
import model

def visualizer(df):

    # Create a figure and increase the figure size
    fig = plt.figure(figsize=(12,8))

    # Create a scatter plot of duration versus year
    plt.scatter(df['release_year'],df['duration'])

    # Create a title
    plt.title('Movie Duration by Year of Release')

    # Show the plot
    plt.show()

    plt.savefig('vis.png')

    model.clustering(df)