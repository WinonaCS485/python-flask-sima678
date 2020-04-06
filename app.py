from flask import current_app as app
from collections import defaultdict
from re import *


import pymysql.cursors
import datetime


    
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('post.html')


@app.route('/post', methods = ['POST', 'GET'])
def post():
    if request.method =='POST':
        User = request.form['User']
        Pwd = request.form['Password']
        list ={'User':passwordInfo}
        
        ''' open datbase '''  
        connection = pymysql.connect(host='mrbartucz.com',
                             user='sx6525ir',
                             password='sx6525ir',
                             db='sx6525ir_University',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)      
        sql = "SELECT Username FROM PWD WHERE Username == User"
        cursor.execute(sql)
        data=cursor.fetchall()
        if(data ==' ')
            print("Enter username again")   
        salt='HoHoTuchBar'
        h = hash(pwd) '''key'''
        passwordInfo = salt+str(h)
        sql = "INSERT INTO PWD (Username, Password) VALUES(?, ?)", (User, passwordInfo)
        else if(data == user):
             print("Please enter username again") 
             sql = "UPDATE INTO PWD (Username, Password) VALUES(?, ?)", (User, passwordInfo)
        else
             print("Please enter username again") 
             cursor.execute(sql) 
             connection.commit()  
                
        for h, in list :
                   h = hash(pwd) '''key'''
                   passwordInfo = salt+str(h) 
                   info_dict[key].append(user)
           print(user)
           print(passwordInfo)
           data=cursor.fetchall()
        return redirect(url_for('database'))
        
           
      
@app.route('/database')        
def database():
      
    file = open( 'post.txt', 'r' )
    if file.mode == 'r':
        contents =file.read()
    file.close()
    
   
    return render_template('page.html', output_data = contents)  
    
        
    
if __name__ == '__main__':
    
     app.run(debug=True, port=27017)
