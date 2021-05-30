from enum import unique
from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///userdb.sqlite3' # connect to DB default way
app.config['SQLALCHEMY_BINDS'] = {   # connect to multiple DB
    'usersDb':r'sqlite:///user.sqlite3',
    'usersDb1':r'sqlite:///user1.sqlite3'
}
app.config['SECRET_KEY'] = 'HiHelloBye'

db = SQLAlchemy(app)

class User(db.Model): # creating table
    __bind_key__ = 'usersDb' # table will create in this Db . Mandatory when using multiple DB
    id = db.Column('UserID',db.Integer,primary_key = True)
    name = db.Column(db.String(80),unique=True,nullable = False)
    city = db.Column(db.String(80),unique=False,nullable = False)
    addr = db.Column(db.String(80),unique=False,nullable = False)
    pin = db.Column(db.String,unique=False,nullable = False)

    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

@app.route('/',methods=['GET'])
def index():
    users = User.query.all()
    return render_template('show_all.html',users=users)

@app.route('/new',methods=['GET','POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['pin']:
            flash('Please enter all the fields', 'error') #use of Flash method
        else:
            check_user=User.query.filter_by(name=request.form['name']).first() # reterving details from the table
            if check_user:
                user = User.query.filter_by(name=request.form['name']).first()
                user.city = request.form['city'] # update the row of a table with a new value
                user.addr = request.form['addr']
                user.pin  = request.form['pin']
                db.session.commit()
                flash('user already exist.so updated the existing user')
                return redirect(url_for('index'))

            user = User(request.form['name'],request.form['city'],request.form['addr'],request.form['pin'])
            db.session.add(user) # insert operation on Db
            db.session.commit()
            flash('Record added sucessfully')
            return redirect(url_for('index'))
    return render_template('new.html')

@app.route('/get_user/<int:id>',methods=['GET'])
def get_user(id):
   user = User.query.get_or_404(id,description="not found") # reterive user via primary key
   if not user:
       flash('user not found')
   return render_template('user_get.html',user=user)

@app.route('/delete/<int:id>',methods=['GET'])
def delete(id):
    user = User.query.get_or_404(id,description="not found")
    db.session.delete(user) # Delete operation
    db.session.commit()
    return redirect(url_for('index'))




if __name__ == '__main__':
    #db.create_all() create the db
    db.create_all(bind='usersDb') # reterive the particular Db
    # db.drop_all() delete the db
    app.run(port=3000,debug=True)
          
        

