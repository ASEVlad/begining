import pandas as pd
my_series = pd.DataFrame(columns=['salary', 'address', 'requirements'])
for i in range(10):
    my_series.loc[i] = [i, i, i]
f = open('text.csv', 'w')
for row in range(10):
    f.write(f'{my_series}')
f.close()