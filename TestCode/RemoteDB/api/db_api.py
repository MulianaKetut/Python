import flask
from flask import request, jsonify
import sqlite3
from sqlite3 import Error
import pymysql.cursors

app = flask.Flask(__name__)
app.config["DEBUG"] = True

database = r"api/test.db"

# Simple Functions


def create_connection():
    c = None
    try:
        c = sqlite3.connect(database)
        print(sqlite3.version)
        return c
    except Error as e:
        print(e)


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    finally:
        if c:
            c.close()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def execute(sql, isSelect=True):
    # LOCAL DATABASE
    # conn = sqlite3.connect(database)
    # conn.row_factory=dict_factory
    # cur = conn.cursor()
    # if isSelect:
    #     return cur.execute(sql).fetchall()
    # else:
    #     result = cur.execute(sql)
    #     conn.commit()
    #     return result
    
    # REMOTE DATABASE
    conn = pymysql.connect(host='remotemysql.com',
                            port=3306,
                            user='N26gN8uvOh',
                            password='xN5x9P4LGQ',
                            db='N26gN8uvOh',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    result = None
    try:
        with conn.cursor() as cursor:
            if isSelect:
                cursor.execute(sql)
                result = cursor.fetchall()
                print(f"result = {result}")
            else:
                cursor.execute(sql)
                result = conn.insert_id()
                conn.commit()
    finally:
        conn.close()
    return result


# def start_db():

#     # create a database connection
#     conn = create_connection()

#     # create tables
#     if conn is not None:
#         user_table_sql = """ CREATE TABLE IF NOT EXISTS user (
#                             id integer PRIMARY KEY AUTOINCREMENT,
#                             age integer NOT NULL,
#                             name text NOT NULL
#                         ); """
#         create_table(conn, user_table_sql)
#     else:
#         print("Error! cannot create the database connection.")

# HTTP functions

# Add new user
@app.route('/user', methods=['POST'])
def post_users():
    user = request.get_json()
    # print("====== req user ", user)
    _age = user['age']
    _name = user['name']

    try:
        sql = f"INSERT INTO tbl_user (age, name) VALUES ({_age}, '{_name}');"

        user['id'] = execute(sql, False)
    except:
        return jsonify({"message":"Created user failed!"})

    return jsonify({"message":"Created user successfully!"})

# Update user
@app.route('/user', methods=['PUT'])
def put_users():
    user = request.get_json()
    _id = user['id']
    _age = user['age']
    _name = user['name']

    try:
        sql = f"UPDATE tbl_user SET age = {_age}, name = '{_name}' WHERE id = {_id};"
        execute(sql, False)
    except:
        return jsonify({"message":"Updated user failed!"})

    return jsonify({"message":"Updated user successfully!"})

# List all users
@app.route('/users', methods=['GET'])
def get_users():

    _id = request.args['id'] if 'id' in request.args else 0
    _age = request.args['age'] if 'age' in request.args else 0
    _name = request.args['name'] if 'name' in request.args else ''

    sql = f"""SELECT * FROM tbl_user WHERE 
            ({_id} = 0 OR id = {_id}) 
            AND ({_age} = 0 OR age = {_age}) 
            AND ('{_name}' = '' OR UPPER(name) = UPPER('{_name}'));"""

    users = execute(sql)
    return jsonify(users)

# Get user by id
@app.route('/user/<_id>', methods=['GET'])
def get_user_by_id(_id):
    sql = f"SELECT * FROM tbl_user WHERE id = {int(_id)};"
    user = execute(sql)
    return jsonify(user)

# Delete user by id
@app.route('/user/<_id>', methods=['DELETE'])
def delete_users(_id):
    try:
        sql = f"DELETE FROM tbl_user WHERE id = {int(_id)};"
        execute(sql, False)
    except:
        return jsonify({"message":"Deleted user failed!"})

    return jsonify({"message":"Deleted user successfully!"})

# LOCAL DATABASE
# start_db()

app.run()