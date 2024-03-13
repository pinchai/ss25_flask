from flask import Flask, render_template
app = Flask(__name__)


std_list = [
    {
        'id': 1,
        'name': 'soron123',
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
    }
]

@app.route('/')
def home():
    module = 'master'
    return render_template('master.html', module=module)


@app.route('/dashboard')
def dashboard():
    module = 'dashboard'
    return render_template('dashboard.html', module=module)


@app.route('/user')
def user():
    module = 'user'
    return render_template('user.html', module=module, data=std_list)


@app.route('/edit_user/<int:user_id>')
def edit_user(user_id):
    module = 'user'
    current_user = []
    for item in std_list:
        if item['id'] == user_id:
            current_user = item

    return render_template('edit_user.html', module=module, data=current_user)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')


if __name__ == '__main__':
    app.run()
