# CREATE TABLES

songplay_table_create = ("""
  CREATE TABLE IF NOT EXISTS songplays
  (songplay_id serial PRIMARY KEY, 
  start_time timestamp REFERENCES time(start_time), 
  user_id int REFERENCES users(user_id), 
  level varchar, 
  song_id varchar REFERENCES songs(song_id), 
  artist_id varchar REFERENCES artists(artist_id), 
  session_id int, 
  location varchar, 
  user_agent varchar)
  """)

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users
(user_id int PRIMARY KEY, 
first_name varchar, 
last_name varchar, 
gender varchar, 
level varchar)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
(song_id varchar PRIMARY KEY, 
title varchar, 
artist_id varchar, 
year int, 
duration float)
""")
                     
song_table_insert = ("""
    INSERT INTO songs
    (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
(artist_id varchar PRIMARY KEY, 
name varchar, 
location varchar, 
latitude float, 
longitude float)
""")
                       
artist_table_insert = ("""
    INSERT INTO artists
    (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
(start_time timestamp PRIMARY KEY, 
hour int, 
day int, 
week int, 
month int, 
year int, 
weekday varchar)
""")
                     
time_table_insert = ("""
    INSERT INTO time
    (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
""")

#DROP TABLES
songplay_table_drop = ("DROP TABLE IF EXISTS songplays CASCADE")
user_table_drop = ("DROP TABLE IF EXISTS users CASCADE")
song_table_drop = ("DROP TABLE IF EXISTS songs CASCADE")
artist_table_drop = ("DROP TABLE IF EXISTS artists CASCADE")
time_table_drop = ("DROP TABLE IF EXISTS time CASCADE")

#QUERIES LIST
create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, artist_table_drop, song_table_drop, time_table_drop, songplay_table_drop]

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays
    (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users
    (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO NOTHING;
""")


# FIND SONGS

song_select = ("""
    SELECT song_id, artists.artist_id
    FROM songs JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s
""")