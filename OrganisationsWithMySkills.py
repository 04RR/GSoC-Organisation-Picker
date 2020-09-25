import pandas as pd

df = pd.read_excel('GSoC.xlsx')
df1 = pd.DataFrame()
cols = []
skills = ['YOUR SKILLS']
for col in df.columns:
    col_list = []
    col_list = df[col].tolist()
    for skill in skills:
        if skill in col_list:
        print(col)
        cols.append(col))

df1 = df[cols]

df1.to_excel(r'IDK.xlsx', index=False, index_label=False)

