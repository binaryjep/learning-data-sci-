import pandas as pd 

session = {
    'MONTH':['JAN','FEB'],
    'day': ['7','8'],
    'year': ['2015','2015'],
    'session_id':[17357, 10011]
}

session_df = pd.DataFrame(session, index=['a','b'])
for j,q in session_df.iterrows():
    session_df.loc[j, 'month'] = q['MONTH'].lower()

print(session_df)