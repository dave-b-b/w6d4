db_name = "user_database.sqlite"

def create_user_with_profile (cur, profile):

    sql = f"INSERT INTO user (first_name, last_name, age, gender, address) VALUES (?, ?, ?, ?, ?)"
    cur.execute(sql, profile)

    
    
def retrieve_users_by_criteria(cur, criteria):

    sql = f"SELECT * FROM user WHERE "

    for key, value in criteria.items():
        ws = ""
        if key in ['id', 'first_name', 'last_name', 'age', 'gender', 'address']:
            ws = f'{key} = {value}'
            key_list = list(criteria.keys())
            if key_list.index(key) != len(key_list) - 1:
                ws = f'{ws}, '
        sql = f'{sql}{ws}'         
    result = cur.execute(sql)
    return list(result)



def update_user_profile(cur, id, update):
    sql = "UPDATE user SET "
    for key, value in update.items():
        us = ""
        if key in ['id', 'first_name', 'last_name', 'age', 'gender', 'address']:
            us = f'{key} = {value}'
            key_list = list(update.keys())
            if key_list.index(key) != len(key_list) - 1:
                us = f'{us}, '
        sql = f'{sql}{us}'     
    
    sql = f'{sql} WHERE id = {id}'
    return cur.execute(sql)

def delete_users_by_criteria(cur, criteria):
    sql = "DELETE FROM user WHERE "
    for key, value in criteria.items():
        ds = ""
        if key in ['id', 'first_name', 'last_name', 'age', 'gender', 'address']:
            ds = f"{key} = '{value}'"
            key_list = list(criteria.keys())
            if key_list.index(key) != len(key_list) - 1:
                ds = f'{ds}, '
        sql = f'{sql}{ds}'     
    
    return cur.execute(sql)