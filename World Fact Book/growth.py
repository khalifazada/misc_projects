import sqlite3 as sql
import pandas as pd
import math

conn = sql.connect('factbook.db')
query = 'select * from facts where (area_land != "" or area_land != 0);'

df = pd.read_sql_query(query, conn)
df = df.dropna()

def final_population(row):
    pop_2050 = (row['population'] * math.e ** ((row['population_growth'] / 100) * 35))
    return pop_2050

population_2050 = df.apply(final_population,axis=1)
population_2050 = population_2050.sort_values(ascending=False)

print(population_2050.head(10))

query_land = 'select sum(area_land)'

conn.close()