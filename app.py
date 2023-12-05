from flask import Flask


# Create a Flask app instance
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)
