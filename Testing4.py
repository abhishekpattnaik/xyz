import pandas as pd
dx = pd.read_csv('http://bit.ly/imdbratings')
print(dx[dx.star_rating>9])
dx.to_excel('AMN.xlsx',sheet_name='IMDB')
print('Successfully created')