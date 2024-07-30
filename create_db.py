import pandas as pd

subject_df = pd.read_csv('./data/subject', sep=',')
colors_df = pd.read_csv('./data/colors', sep=',')
dates_df = pd.read_csv('./data/dates', sep=',', names=['title', 'date', 'other'])



subject_df = subject_df.drop(['EPISODE', 'TITLE', 'GUEST', 'DIANE_ANDRE', 'STEVE_ROSS'], axis=1)
subject_df.drop(list(subject_df.filter(regex = 'FRAME')), axis = 1, inplace = True)

cols = subject_df.columns.tolist()[1:]
for col in cols:
	if (subject_df[col].mean() == 0):
		subject_df = subject_df.drop(col, axis=1)

subject_df.columns = subject_df.columns.str.lower()

def get_subjects(row):
	cols = []
	for col in row.index:
		if row[col] == 1:
			cols.append(col)
	return cols

subject_df['subject_list'] = subject_df.apply(lambda row: get_subjects(row), axis=1)

subject_df['subject_list'] = subject_df['subject_list'].apply(lambda x: ', '.join(x))

subject_df = subject_df.drop(subject_df.columns.difference(['subject_list']), axis=1)

subject_df['id'] = range(0, len(subject_df))


colors_df.drop(['Unnamed: 0', 'painting_index', 'season', 'episode', 'color_hex', 'colors', 'painting_title', 'youtube_src'], axis=1, inplace=True)

cols = colors_df.columns.tolist()[3:]
colors_df['verify_colors'] = colors_df[cols].sum(axis=1)
colors_df.loc[~(colors_df['verify_colors'] == colors_df['num_colors'])]

colors_df.drop(['verify_colors', 'num_colors'], axis=1, inplace=True)

colors_df.columns = colors_df.columns.str.lower()

def get_colors(row):
	cols = []
	for col in row.index:
		if row[col] == 1:
			cols.append(col)
	return cols

colors_df['color_list'] = colors_df.apply(lambda row: get_colors(row), axis=1)

colors_df['color_list'] = colors_df['color_list'].apply(lambda x: ', '.join(x))

colors_df = colors_df.drop(colors_df.columns.difference(['color_list']), axis=1)

colors_df['id'] = range(0, len(colors_df))


dates_df.drop(['other'], axis=1, inplace=True)
dates_df['id'] = range(0, len(dates_df))

dates_df = dates_df[['id', 'title', 'date']]


two_df = pd.merge(dates_df, colors_df)
three_df = pd.merge(two_df, subject_df)

three_df.columns = three_df.columns.str.lower()



import sqlite3

col_list = ['id INTEGER NOT NULL PRIMARY KEY', 'title VARCHAR(50) NOT NULL UNIQUE', 'date VARCHAR(20) NOT NULL UNIQUE', 'color_list BLOB NOT NULL', 'subject_list BLOB NOT NULL']
col_list = ','.join(col_list)

conn = sqlite3.connect('./joy_of_painting.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS episodes(col_str)')


import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///./joy_of_painting.db')

three_df = three_df.applymap(str)

three_df.to_sql('episodes', engine, if_exists='replace', index=False)