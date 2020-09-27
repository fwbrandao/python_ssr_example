from flask import Flask, render_template, request, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder="./client/build/static", template_folder="./client/build")

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/",methods=['GET', 'POST'])
def index():
  return render_template('index.html')

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)
