from flask import Flask, render_template, request, redirect, url_for
from database import Database
from waitress import serve

app = Flask(__name__, static_url_path='')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/validateRegister', methods=['GET', 'POST'])
def validateRegister():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    db = Database()
    db.creeateUser(name, email, password)
    return render_template('login.html')


@app.route('/validateLogin', methods=['GET', 'POST'])
def validateLogin():
    email = request.form['email']
    password = request.form['password']
    db = Database()
    if email=='admin' and password==db.loginAdmin(email)[0]:
        return redirect(url_for('admin'))
    else:
        if password == db.loginUser(email)[0]:
            return redirect(url_for('customercare'))
        else:
            return "Invalid Credentials"


@app.route('/customercare')
def customercare():
    return render_template('customercare.html')

@app.route('/admin')
def admin():
    db = Database()
    agents = db.getAgents()
    print(agents)
    return render_template('admin.html', agt=agents)

@app.route('/agentAssign')
def agentAssign():
    db = Database()
    complaints = db.getComplaints()
    print(complaints)
    return render_template('agentAssign.html',comp=complaints)
    

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    complaint = request.form['complaint']
    db = Database()
    db.registerComplaint(name, email, complaint)
    return redirect(url_for('customercare'))
    

if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=8080)
    app.run()