import sqlite3 as sql

# create a connection
conn = sql.connect('factbook.db')
curs = conn.cursor()

# return sum of area_land
query = 'select sum(area_land) from facts where area_land != 0 and area_land != "";'
curs.execute(query)
sum_area_land = curs.fetchone()[0]

# return sum of area_water
query = 'select sum(area_water) from facts where area_water != 0 and area_water != "";'
curs.execute(query)
sum_area_water = curs.fetchone()[0]

# calc ration & print
land_water_ratio = sum_area_land / sum_area_water
print(land_water_ratio)

# close connection
conn.close()