from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from pymysql import NULL, MySQLError, connect

BOOKS = []

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

result_ok = json.dumps({'result': 'ok'})
result_fail = json.dumps({'result': 'fail'})
result_session_error = json.dumps({'result': 'session_error'})
result_pw_invalid = json.dumps({'result': 'Invalid Password'})
result_id_invalid = json.dumps({'result': 'Invalid ID'})

"""
========================================================================================================================
MariaDB SQL : mysqlconn, sqlExe, sqlSelect
========================================================================================================================
"""


# MariaDB CONNECT
def mysqlconn():
    return connect(host="127.0.0.1", port=3306, user='root', password='airlab@3293', db='books', charset='utf8')
    

# Sql Insert, Delete
def sqlExe(sql, data):
    conn = mysqlconn()
    curs = conn.cursor()
    try:
        curs.execute(sql, (*data,))
        tmp = conn.commit()
        response = result_ok
    except MySQLError as e:
        print(e)
        response = result_fail
    conn.close()
    return response


# Sql Select
def sqlSelect(sql, data):
    conn = mysqlconn()
    curs = conn.cursor()
    datalist = []
    try:
        curs.execute(sql, (*data,))
        datas = curs.fetchall()
        for data in datas:
            datalist.append(data)
    except MySQLError as e:
        print(e)
    conn.close()
    return datalist


"""
========================================================================================================================
            APP Route
========================================================================================================================
"""
# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        data =[post_data.get('title'), post_data.get('author'), post_data.get('read')]
        sql = "INSERT INTO book_list_tbl (TITLE, AUTHOR, ISREAD) VALUES (%s, %s, %s)"
        result = sqlExe(sql, data)
        if result_fail == result:
            response_object['message'] = 'Fail!'
        else:
            response_object['message'] = 'Book added!'
    # 조회
    BOOKS.clear();
    sql = 'select * from book_list_tbl'
    sqlResult = sqlSelect(sql, [])
    for i in sqlResult:
        idx, title, author, read = (i)
        BOOKS.append({
            'id': idx,
            'title': title,
            'author': author,
            'read': True if read == 1 else False
        })
    response_object['books'] = BOOKS
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        sql = 'update book_list_tbl set TITLE=%s, AUTHOR=%s, ISREAD=%s where BOOK_ID=%s'
        result = sqlExe(sql, [post_data.get('title'), post_data.get('author'), post_data.get('read'), book_id])
        if result == result_ok:
            response_object['message'] = 'Book updated!'
        else:
            response_object['message'] = 'Fail!'
    if request.method == 'DELETE':
        sql = 'delete from book_list_tbl where BOOK_ID=%s'
        response = sqlExe(sql, [book_id])
        if response == result_ok:
            response_object['message'] = 'Book removed!'
        else:
            response_object['message'] = 'Fail!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(host='0.0.0.0')