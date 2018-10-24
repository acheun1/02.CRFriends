#Assignment: C + R Friends
#2018 10 08
#Cheung Anthony

# Create a Flask application that displays data from a MySQL database
# Take user input and add it to the database
# Practice redirecting after going to a POST route

# Create a simple registration page with the following fields:

# Have the main page show all users and their data as part of a table. On the same page, allow users to enter data and submit that data to the database in order to add a new friend. How many routes do you need? What should each do? Think back to routing from the previous section, and remember never to render from a post route (once you're done building the features you need).

from flask import Flask, render_template, redirect, request, session,flash

from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key='as43df46asd3f4as4'

@app.route('/')
def index():
    mysql = connectToMySQL('cr')
    all_friends = mysql.query_db("SELECT * FROM user")
    print("all the users", all_friends)
    cnt=len(all_friends)
    return render_template('index.html',friends=all_friends,loopcnt=cnt)

@app.route('/update_records', methods=['POST'])
def update():
    mysql = connectToMySQL('cr')
    insert_query="INSERT INTO user (name_first, name_last, occupation, created_at, updated_at) VALUES (%(name_first)s, %(name_last)s, %(occupation)s, NOW(), NOW());"
    record = {
                'name_first':request.form['q1'],
                'name_last':request.form['q2'],
                'occupation':request.form['q3'],
            }
    new_record_id=mysql.query_db(insert_query, record)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
