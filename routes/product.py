import os
import time

from app import app, render_template, request, IMAGE_DIR
from sqlalchemy import create_engine, text
from helpers import file_upload

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
    result = connection.execute(text("""
        SELECT
        product.id,
        product.name,
        category.`name` as category,
        product.cost,
        product.price,
        product.stock,
        category.`id` as category_id,
        product.`image` as image
    FROM
        `product`
        INNER JOIN category ON product.category_id = category.id 
    ORDER BY
        product.id DESC
	"""))
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
                'category_id': item[6],
                'image': item[7],
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
    category_id = data.get('category_id')
    cost = data.get('cost')
    price = data.get('price')
    stock = data.get('stock')

    result = connection.execute(text(f"UPDATE `product` set `name` = '{name}',"
                                     f" `category_id` = '{category_id}',"
                                     f" `cost` = '{cost}',"
                                     f" `price` = '{price}',"
                                     f" `stock` = '{stock}'"
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
    category_id = form.get('category_id')
    cost = form.get('cost')
    price = form.get('price')
    stock = form.get('stock')
    # return str(form), 500
    base64_string = request.json['image']

    image_name = None
    if base64_string:
        image_path = os.path.join(IMAGE_DIR)
        image_name = f"{time.time()}.png"
        file = file_upload.upload(base64_string, image_path, image_name)

    result = connection.execute(
        text(f"INSERT INTO `product` VALUES(null, '{name}', '{category_id}', '{cost}', '{price}', '{stock}', '{image_name}')"))
    connection.commit()
    return f"Last Product: {result}"
