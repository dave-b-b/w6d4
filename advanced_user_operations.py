import sqlite3

class AdvancedUserOperations():

    db_name = "user_database.sqlite"
    
    def __init__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("DROP TABLE IF EXISTS user")
        ddl = "CREATE TABLE user(id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, age INTEGER, gender TEXT, address TEXT)"
        self.cur.execute(ddl)

    def create_user_with_profile(self, name, email, password, age=None, gender=None, address=None):
        args = (name, email, password, age, gender, address)
        sql = f"INSERT INTO user (name, email, password, age, gender, address) VALUES (?, ?, ?, ?, ?, ?)"
        try:
            self.cur.execute(sql, args)
            self.conn.commit()

            return self._get_user_by_id(self.cur.lastrowid)

        except Exception as e:
            print("Error creating user:", e)
            return None

        
    def retrieve_users_by_criteria(self, min_age=None, max_age=None, gender=None):

        params = {
            "min_age": min_age,
            "max_age": max_age,
            "gender": gender,
        }

        sql = f"SELECT * FROM user WHERE "
        if min_age:
            sql = f'{sql}age >= {min_age}'
        if max_age:
            sql = f'{sql} AND age <= {max_age}'
        if gender:
            sql = f"{sql} AND gender = '{gender}'"

        result = self.cur.execute(sql)
        return list(result)

    def update_user_profile(self, email, age=None, gender=None, address=None):
        string = f"UPDATE user SET email = '{email}' WHERE "

        update = {
            "age": age,
            "gender": gender,
            "address": address,
        }

        sql = self._get_string(string=string, params=update)

        self.cur.execute(sql)
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM user WHERE email = '{email}'")
        return self.cur.fetchone()

    def delete_users_by_criteria(self, gender=None):
        sql = "DELETE FROM user WHERE "

        criteria = {
            "gender": gender
        }

        sql = self._get_string(sql, criteria)   
        
        self.cur.execute(sql)
    
    def _get_string(self, string, params):
        result = string
        
        for key, value in params.items():
            additional_param = ""
            if value is not None:
                exact_value = f"'{value}'" if type(value) == str else value
                additional_param = f"{key} = {exact_value}"
                key_list = list(params.keys())
                if key_list.index(key) != len(key_list) - 1:
                    additional_param = f'{additional_param} AND '
            result = f'{result}{additional_param}'     
        
        return result
    
    def _get_user_by_id(self, user_id):
        sql = f"SELECT * FROM user WHERE id = {user_id}"
        result = self.cur.execute(sql)
        return result.fetchone()
    
    def __del__(self):
        self.conn.close()