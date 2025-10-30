from flask import Flask
from routes.pricing import pricing_bp

app = Flask(__name__)
app.register_blueprint(pricing_bp)

if __name__ == '__main__':
    app.run(debug=True)
