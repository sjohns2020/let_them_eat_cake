from flask import Flask, render_template
from controllers.cakes_controller import cakes_blueprint
from controllers.bakers_controller import bakers_blueprint


app = Flask(__name__)

app.register_blueprint(cakes_blueprint)
app.register_blueprint(bakers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)