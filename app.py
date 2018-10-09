# End 2 End API Application

from flask import Flask
from flask import Request
from flask import Response
import requests

app = Flask(__name__)

@app.route("/return/<int:some_id>", methods=['GET', 'POST', 'OPTIONS'])
def return_something(some_id):
    response = Response(
        response=str("<h1>Hey!!<br/>Is this your parameter? - %s <h1>" %(str(some_id))),
        status=200,
        mimetype="text/html"
    )
    return response

@app.route("/owround/<int:some_id>", methods=['GET', 'POST', 'OPTIONS'])
def other_way_round(some_id):
    URL = "http://0.0.0.0:9000/return/%s" %(str(some_id))
    response = requests.get(URL)
    return Response(
        response=response.content,
        status=response.status_code,
        mimetype="text/html"
    )

if __name__ == "__main__":
    app.run(host ='0.0.0.0',port=9000)
