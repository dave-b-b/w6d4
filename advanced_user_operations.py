import sqlite3
from functions import db_name, create_user_with_profile, retrieve_users_by_criteria, update_user_profile, delete_users_by_criteria



conn = sqlite3.connect(db_name)

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS user")

ddl = "CREATE TABLE user(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER, gender TEXT, address TEXT)"
cur.execute(ddl)
profile = ("dave", "brown", 37, "male", "12 Austin st. Mallager, Mass")
create_user_with_profile(cur, profile)

conn.commit()

criteria = {
    "age": 37
}
search_results = retrieve_users_by_criteria(cur=cur, criteria=criteria)

print(list(search_results))

update = {
    "age": 38
}

update_user_profile(cur, 1, update=update)
conn.commit()

criteria = {
    "id" : 1
}
search_results = retrieve_users_by_criteria(cur=cur, criteria=criteria)

print(list(search_results))

criteria = {
    "last_name": "brown"
}

delete_users_by_criteria(cur, criteria)

conn.commit()

criteria = {
    "id" : 1
}
search_results = retrieve_users_by_criteria(cur=cur, criteria=criteria)

print(list(search_results))