from flask import Flask, render_template, request
app = Flask(__name__)


std_list = [
    {
        'id': 1,
        'name': 'soron',
        'gender': 'male',
        'phone': '031 37 20 005',
        'email': 'soronboyloy@gmail.com',
        'address': 'kampong cham',
    },
    {
        'id': 2,
        'name': 'soben',
        'gender': 'male',
        'phone': '070 37 20 005',
        'email': 'sobenhotboy@gmail.com',
        'address': 'kampot',
    },
    {
        'id': 3,
        'name': 'chengmeng',
        'gender': 'male',
        'phone': '010 99 20 005',
        'email': 'chengmengRSK@gmail.com',
        'address': 'Takeo',
    }
]


@app.route('/')
@app.route('/dashboard')
def dashboard():
    module = 'dashboard'
    return render_template('dashboard.html', module=module)


@app.route('/user')
def user():
    module = 'user'
    return render_template('user.html', module=module, data=std_list)


@app.route('/add_user')
def add_user():
    module = 'user'
    return render_template('add_user.html', module=module)


@app.route('/view_user')
def view_user():
    module = 'user'
    name = request.args.get('name', default='No Name', )
    gender = request.args.get('gender', default='Female', )
    # current_user = []
    # for item in std_list:
    #     if item['id'] == user_id:
    #         current_user = item

    # data = filter(lambda x: x['id'] == user_id, std_list)
    # current_user = list(data)
    return render_template('view_user.html', module=module, name=name, gender=gender)


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
