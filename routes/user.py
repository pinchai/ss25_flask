from app import app, render_template, request
from sqlalchemy import create_engine, text
try:
    engine = create_engine("mysql+mysqlconnector://root:mysql@127.0.0.1/ss25_db")
    # Test the connection
    connection = engine.connect()
except Exception as e:
    print(e)


@app.route('/user')
def user():
    module = 'user'
    return render_template('user.html', module=module)


@app.get('/getUser')
def getUser():
    result = connection.execute(text("SELECT * FROM `user` order by id desc"))
    connection.commit()
    data = result.fetchall()
    user_list = []
    for item in data:
        user_list.append(
            {
                'id': item[0],
                'name': item[1],
                'gender': item[2],
                'phone': item[3],
                'email': item[4],
                'address': item[5],
            }
        )
    return user_list


@app.post('/editUser')
def editUser():
    data = request.get_json()
    user_id = data.get('id')
    name = data.get('name')
    gender = data.get('gender')
    phone = data.get('phone')
    email = data.get('email')
    address = data.get('address')

    result = connection.execute(text(f"UPDATE `user` set `name` = '{name}',"
                                     f" `gender` = '{gender}', "
                                     f"`phone` = '{phone}', "
                                     f"`email` = '{email}', "
                                     f"`address` = '{address}' "
                                     f"WHERE id = '{user_id}'"))
    connection.commit()
    return "update success"


@app.post('/deleteUser')
def deleteUser():
    data = request.get_json()
    user_id = data.get('id')
    result = connection.execute(text(f"DELETE FROM `user`"
                                     f" WHERE id = {user_id}"))
    connection.commit()
    return f"{result}"


@app.post('/createUser')
def createUser():
    form = request.get_json()
    name = form.get('name')
    gender = form.get('gender')
    phone = form.get('phone')
    email = form.get('email')
    address = form.get('address')
    password = '123456'

    result = connection.execute(
        text(f"INSERT INTO `user` VALUES(null, '{name}', '{gender}', '{phone}', '{email}', '{address}', '{password}')"))
    connection.commit()
    current_id = result.lastrowid
    return f"Last User ID: {current_id}"
