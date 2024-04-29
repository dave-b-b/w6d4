import unittest
from functions import retrieve_users_by_criteria, \
    db_name, update_user_profile, delete_users_by_criteria, \
    create_user_with_profile
import sqlite3

class Test_AdvancedUser_Operations(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("DROP TABLE IF EXISTS user")
        ddl = "CREATE TABLE user(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER, gender TEXT, address TEXT)"
        self.cur.execute(ddl)
        self.conn.commit()           
        self.cur.execute("INSERT INTO user (first_name, last_name, age, gender, address) VALUES ('dave', 'brown', 37, 'male', '12 Austin st. Mallager, Mass')")
        self.conn.commit()

    def test_retrieve_users_by_criteria(self):
        criteria = {'id': 1}
        expected_result = [(1, 'dave', 'brown', 37, 'male', '12 Austin st. Mallager, Mass')]
        result = retrieve_users_by_criteria(self.cur, criteria)
        self.assertEqual(result, expected_result)

    def test_update_user_profile(self):
        update = {'age': 38}
        update_user_profile(self.cur, 1, update)
        self.conn.commit()
        criteria = {'id': 1}
        expected_result = [(1, 'dave', 'brown', 38, 'male', '12 Austin st. Mallager, Mass')]
        result = retrieve_users_by_criteria(self.cur, criteria)
        self.assertEqual(result, expected_result)

    def test_delete_users_by_criteria(self):
        criteria = {'last_name': 'brown'}
        delete_users_by_criteria(self.cur, criteria)
        self.conn.commit()
        criteria = {'id': 1}
        expected_result = []
        result = retrieve_users_by_criteria(self.cur, criteria)
        self.assertEqual(result, expected_result)
    
    def test_create_user_with_profile(self):
        profile = ('jane', 'doe', 25, 'female', '12 Austin st. Mallager, Mass')
        create_user_with_profile(self.cur, profile)
        self.conn.commit()
        criteria = {'id': 2}
        expected_result = [(2, 'jane', 'doe', 25, 'female', '12 Austin st. Mallager, Mass')]
        result = retrieve_users_by_criteria(self.cur, criteria)
        self.assertEqual(result, expected_result)

    

if __name__ == '__main__':
    unittest.main()