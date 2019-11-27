from flask import Flask

app = Flask(__name__)

# Launch app if this file was directly executed
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)