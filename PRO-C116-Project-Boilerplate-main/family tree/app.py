# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "vijay" # write your name
    age = "12" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage


@app.route('/father/')
def home():
    name = "sakthivelu" # write your name
    age = "50" # write your age
    return render_template('father.html', name = name , age = age)



# define the route to mother webpage
@app.route('/mother/')
def home():
    name = "dhanya" # write your name
    age = "40" # write your age
    return render_template('mother.html', name = name , age = age)

# define the route to friends webpage
@app.route('/friends/')
def home():
    name = "monish,dhivvesh,etc.." # write your name
    age = "13" # write your age
    return render_template('friends.html', name = name , age = age)


# add other routes, if you want
@app.route('/sister/')
def home():
    name = "ahalya" # write your name
    age = "17" # write your age
    return render_template('sister.html', name = name , age = age)




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
