from app import app, render_template, request
from sqlalchemy import create_engine, text
try:
    engine = create_engine("mysql+mysqlconnector://root:mysql@127.0.0.1/ss25_db")
    # Test the connection
    connection = engine.connect()
except Exception as e:
    print(e)


@app.route('/category')
def category():
    module = 'category'
    return render_template('category.html', module=module)


@app.get('/getCategory')
def getCategory():
    result = connection.execute(text("SELECT * FROM `category` order by id desc"))
    connection.commit()
    data = result.fetchall()
    category_list = []
    for item in data:
        category_list.append(
            {
                'id': item[0],
                'name': item[1],
                'description': item[2],
            }
        )
    return category_list


@app.post('/editCategory')
def editCategory():
    data = request.get_json()
    category_id = data.get('id')
    name = data.get('name')
    description = data.get('description')

    result = connection.execute(text(f"UPDATE `category` set `name` = '{name}',"
                                     f" `description` = '{description}'"
                                     f"WHERE id = '{category_id}'"))
    connection.commit()
    return "update success"


@app.post('/deleteCategory')
def deleteCategory():
    data = request.get_json()
    category_id = data.get('id')
    result = connection.execute(text(f"DELETE FROM `category`"
                                     f" WHERE id = {category_id}"))
    connection.commit()
    return f"{result}"


@app.post('/createCategory')
def createCategory():
    form = request.get_json()
    name = form.get('name')
    description = form.get('description')

    result = connection.execute(
        text(f"INSERT INTO `category` VALUES(null, '{name}', '{description}')"))
    connection.commit()
    return f"Last Category: {result}"
