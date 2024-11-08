from flask import Flask,render_template,Response
from CustomerDAO import CustomerDAO
from dataclasses import asdict
import json

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World fred!</p>"


# @app.route("/")
# def index():
#     dao = CustomerDAO(r'..\customers_db.db')
#     customers = dao.find_all()
#     html = ""
#     for customer in customers:
#         html+=f"<li>{customer.first_name} {customer.last_name}</li>"
#     return f"<ul>{html}</ul>"

@app.route("/")
def index():
    dao = CustomerDAO(r'..\customers_db.db')
    customers = dao.find_all()
    return render_template("customers.html",customers=customers)

@app.route("/api")
def api():
    dao = CustomerDAO(r'..\customers_db.db')
    # from dataclasses import asdict
    # import dataclasses as dc
    # dc.asdict()

    customers = [asdict(c) for c in dao.find_all()]
    data = json.dumps(customers,indent=4)
    return Response(data,200,mimetype="application/json")
    
