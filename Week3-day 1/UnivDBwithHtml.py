from flask import Flask, render_template
import pymysql.cursors


# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='CS485',
                             password='WinonaState',
                             db='CS485',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = "SELECT * from Students where Student ="
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        #connection.commit();
        

finally:
    connection.close()
    
app = Flask(__name__)

@app.route('/UnivDB')
def UnivDB():
    return render_template(result)
if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    #app.run(debug=True, host='50.116.3.147')
   app.run(debug=True, host='sx6525ir@localhost')