# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays "
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
songplay_id serial primary key,
start_time date not null REFERENCES time(start_time),
user_id int not null references users (user_id),
level text,
song_id text references songs(song_id),
artist_id text references artists(artist_id),
session_id text,
location text,
user_agent text
)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
user_id int primary key,
first_name text not null ,
last_name text not null,
gender text,
level text
)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id text primary key,
title text not null,
artist_id text references artists(artist_id) ,
year int,
duration float not null
)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
artist_id text primary key ,
name text not null, location text,
latitude float,
longitude float
)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
start_time date primary key,
hour int,
day int,
week int,
month int ,
year int,
weekday text
)
""")

# INSERT RECORDS

songplay_table_insert = ("""  insert into songplays(
start_time, user_id, level, song_id, artist_id, session_id,location, user_agent)
    VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""INSERT INTO users
    (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;
""")

song_table_insert = ("""insert into songs
(song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists
    (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time
    (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = (""" select song_id ,artists.artist_id
        from songs join artists ON songs.artist_id = artists.artist_id
        where songs.title =%s
        AND artists.name =%s
        AND songs.duration =%s
""")

# QUERY LISTS

create_table_queries = [artist_table_create, user_table_create, song_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]