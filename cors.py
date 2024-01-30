# pip install -U flask-cors

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/api/v1/users")
# @app.route("/")
def hello():
    return "Hello! CORS gets enabled!"


@app.route("/app/4/o")
def getw():
    return "Hello!!"


if __name__ == "__main__":
    app.run(debug=True)

#
# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
