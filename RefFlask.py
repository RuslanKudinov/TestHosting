from flask import Flask
app = Flask(__name__) #application#main

@app.route("/") # href - hyper reference
def hello_world():# h - header, ul - unordered list, li - list item
   return """
 <h1>Добро пожаловать на мой сайт!</h1>
 <ul>
     <li><a href="/about">Первая страница</a></li>
     <li><a href="/user">Вторая страница</a></li>
 </ul>
 """

@app.route("/about")
def about():
    return """
 <h1>Первая страница</h1>
 <ul>
     <li><a href="/">Домашняя страница</a></li>
 </ul>
 """
@app.route("/user")
def contact():
    return """
 <h1>Вторая страница</h1>
 <ul>
     <li><a href="/">Домашняя страница</a></li>
 </ul>
 """

app.run(debug=True)




