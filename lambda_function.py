import pandas as pd

def lambda_handler(even, context):
    df = pd.DataFrame({'col1':[2,7],
                        'col2':[10, 11]})
    print(df)
    print('Done x1.1')
