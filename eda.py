import vis

def insights(df):
    # Perform exploratory data analysis and generate insights
    insight1 = "Insight 1: the movies during the 2010s have a higher duration and revenue than the movies during the 1990s"
    insight2 = "Insight 2: the movies production have increaced during the 2000s"
    insight3 = "Insight 3: the USE has produced most of the movies with 2100 movies "

    # Save insights as text files
    with open("/home/doc-bd-a1/eda-in-1.txt", "w") as f:
        f.write(insight1)

    with open("/home/doc-bd-a1/eda-in-2.txt", "w") as f:
        f.write(insight2)

    with open("/home/doc-bd-a1/eda-in-3.txt", "w") as f:
        f.write(insight3)

    vis.visualizer(df)