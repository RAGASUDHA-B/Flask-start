from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route (URL path) and its function
@app.route("/")
def home():
    return "Hello, Flask! 🎉"

# Run the app only if the script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
