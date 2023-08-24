from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'survey_data'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def survey_form():
    if request.method == 'POST':
        fname = request.form['Fname']
        lname = request.form['Lname']
        email = request.form['Email']
        age = request.form['Age']
        gender = request.form['gender']
        role = request.form['role']
        favorite_feature = request.form['favorite_feature']
        recommendation = request.form['recommendation']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO survey_data (fname, lname, email, age, gender, role, favorite_feature, recommendation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (fname, lname, email, age, gender, role, favorite_feature, recommendation))
        mysql.connection.commit()
        cur.close()
        
        return "Form submitted successfully!"

    return render_template('survey_form.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
