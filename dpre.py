import pandas as pd
import eda


def trans(df):

    df = df[df['type'] == 'Movie']
    df = df[['title', 'country', 'genre', 'release_year', 'duration','date_added','genre']]

    df['date_added'] = pd.to_datetime(df['date_added']).dt.strftime('%m,%d,%Y')
    df = df.dropna()

    df['release_year'] = df['release_year'].astype(int)
    df['duration'] = df['duration'].astype(int)

    min_duration = df['duration'].min()
    max_duration = df['duration'].max()

    # Min-Max scaling
    df['duration_normalized'] = (df['duration'] - min_duration) / (max_duration - min_duration)

    df = pd.get_dummies(df, columns=['genre'], prefix='genre')
   

    df.to_csv('res_dpre.csv', index=False)
    eda.insights(df)