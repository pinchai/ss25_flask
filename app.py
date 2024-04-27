from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

cnn = sqlite3.connect('db.sqlite3')
cur = cnn.cursor()
student = cur.execute("""SELECT * FROM student""")
cnn.commit()
std_list = []
for row in student:
    std_list.append(
        {
            'id': row[0],
            'name': row[1],
            'gender': row[2],
            'phone': '031 37 20 005',
            'email': 'soronboyloy@gmail.com',
            'address': row[3],
        }
    )


@app.route('/')
@app.route('/dashboard')
def dashboard():
    module = 'dashboard'
    return render_template('dashboard.html', module=module)


@app.route('/user')
def user():
    module = 'user'
    return render_template('user.html', module=module, data=std_list)


@app.get('/add_user')
def add_user():
    module = 'user'
    return render_template('add_user.html', module=module)


@app.post('/create_user')
def create_user():
    module = 'user'
    name = request.form.get('name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')

    form = {
        'name': name,
        'gender': gender,
        'phone': phone,
        'email': email,
        'address': address,
    }

    return form


@app.route('/view_user')
def view_user():
    module = 'user'
    name = request.args.get('name', default='No Name', )
    current_user = filter(lambda x: x['name'] == name, std_list)
    user_list = list(current_user)

    return render_template('view_user.html', module=module, data=user_list[0])


@app.route('/confirm_delete_user')
def confirm_delete_user():
    module = 'user'
    name = request.args.get('name', default='No Name', )
    current_user = filter(lambda x: x['name'] == name, std_list)
    user_list = list(current_user)

    return render_template('confirm_delete_user.html', module=module, data=user_list[0])


@app.route('/edit_user/<int:user_id>')
def edit_user(user_id):
    module = 'user'
    # current_user = []
    # for item in std_list:
    #     if item['id'] == user_id:
    #         current_user = item

    data = filter(lambda x: x['id'] == user_id, std_list)
    current_user = list(data)
    return render_template('edit_user.html', module=module, data=current_user[0])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')


if __name__ == '__main__':
    app.run()
