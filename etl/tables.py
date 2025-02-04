import pandas as pd
tables = pd.read_html('https://sites.google.com/view/cool-tools-for-schools/home/html-codes/tables')
print('Quantidade de tabelas: {len(tables)}')