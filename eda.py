import vis

def insights(df):
    # Perform exploratory data analysis and generate insights
    insight1 = "Insight 1: ..."
    insight2 = "Insight 2: ..."
    insight3 = "Insight 3: ..."

    # Save insights as text files
    with open("/home/doc-bd-a1/eda-in-1.txt", "w") as f:
        f.write(insight1)

    with open("/home/doc-bd-a1/eda-in-2.txt", "w") as f:
        f.write(insight2)

    with open("/home/doc-bd-a1/eda-in-3.txt", "w") as f:
        f.write(insight3)

    vis.visualizer(df)