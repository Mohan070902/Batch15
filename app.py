from flask import Flask, request, render_template, redirect, url_for, session,make_response
import jwt

app = Flask(__name__) 

SECRET_KEY = "my-secret-key" 


@app.route("/") 
def home():
    return render_template("home.html")
print("Python")

 
 
@app.route("/login", methods=["POST"]) 
def login(): 
 
    username = request.form["username"] 
    password = request.form["password"] 
 
    if username == "admin" and password == "1234": 
 
        token = jwt.encode({"user_id": 1, "name" : "Mohan", "password":1234}, SECRET_KEY, algorithm="HS256") 
 
        return { 
            "message": "Login Successful", 
            "token": token 
        } 
 
    return { 
        "message": "Invalid Login" 
    }, 401 


if __name__ == "__main__": 
    app.run(debug=True) 

