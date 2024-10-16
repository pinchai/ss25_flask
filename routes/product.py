from app import app, render_template, request
from sqlalchemy import create_engine, text

try:
    engine = create_engine("mysql+mysqlconnector://root:mysql@127.0.0.1/ss25_db")
    # Test the connection
    connection = engine.connect()
except Exception as e:
    print(e)


@app.route('/product')
def product():
    module = 'product'
    return render_template('product.html', module=module)


@app.get('/getProduct')
def getProduct():
    # products
    result = connection.execute(text("SELECT * FROM `product` order by id desc"))
    connection.commit()
    data = result.fetchall()

    # category
    category_result = connection.execute(text("SELECT * FROM `category` order by id desc"))
    connection.commit()
    category_data = category_result.fetchall()

    product_list = []
    for item in data:
        product_list.append(
            {
                'id': item[0],
                'name': item[1],
                'category': item[2],
                'cost': item[3],
                'price': item[4],
                'stock': item[5],
            }
        )

    category_list = []
    for item in category_data:
        category_list.append(
            {
                'id': item[0],
                'name': item[1],
                'description': item[2],
            }
        )
    return {
        'category_list': category_list,
        'product_list': product_list
    }


@app.post('/editProduct')
def editProduct():
    data = request.get_json()
    product_id = data.get('id')
    name = data.get('name')
    description = data.get('description')

    result = connection.execute(text(f"UPDATE `product` set `name` = '{name}',"
                                     f" `description` = '{description}'"
                                     f"WHERE id = '{product_id}'"))
    connection.commit()
    return "update success"


@app.post('/deleteProduct')
def deleteProduct():
    data = request.get_json()
    product_id = data.get('id')
    result = connection.execute(text(f"DELETE FROM `product`"
                                     f" WHERE id = {product_id}"))
    connection.commit()
    return f"{result}"


@app.post('/createProduct')
def createProduct():
    form = request.get_json()
    name = form.get('name')
    description = form.get('description')

    result = connection.execute(
        text(f"INSERT INTO `product` VALUES(null, '{name}', '{description}')"))
    connection.commit()
    return f"Last Product: {result}"
