from flask import Flask

# Create app
app = Flask(__name__)

# Route for homepage
@app.route('/')
def hello():
    return "<h1>Hello from your Python Web App!</h1>"

# Run server
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
