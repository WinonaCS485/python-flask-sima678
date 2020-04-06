from flask import Flask, render_template, redirect, url_for, request
from flask import current_app as app
import sys , keyword


import pymysql.cursors
import datetime
    
app = Flask(__name__)
def formula():
    salt = "HoHoTuchBar"
    num1=9
    num2=44444
    salt = str(num1)+salt+str(num2)
    return salt

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('post.html')
#    return render_template('enterPosthtmlagain.html')
@app.route('/post', methods = ['POST', 'GET'])
def post():
    if request.method =='POST':  
            ''' open datbase '''
       connection = pymysql.connect(host='mongodb0.example.com', user='Team8', password='TeamSMP',db='sx6525ir_Geo', arset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)      
        sql ="SELECT * From places"
        cursor.execute(sql)
        data=cursor.fetchall()
    return render_template('page.html', output_data =data)

@app.route('/database')        
def database():
    #if request.method =='GET':
       connection = pymysql.connect(host='mongodb0.example.com',
                             user='Team8',
                             password='TeamSMP',
                             db='sx6525ir_Geo',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
        sql ="SELECT * From places"
        cursor.execute(sql)
        data=cursor.fetchall()
     return render_template('page.html', output_data =data)

        
    
if __name__ == '__main__':
    
     app.run(debug=True, port=27016)






