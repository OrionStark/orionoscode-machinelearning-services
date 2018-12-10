from flask import Flask
from .blueprints.IrisBlueprint import IrisBlueprint
from .blueprints.ErrorHandlerBlueprint import ErrorHandlerBlueprint

app = Flask(__name__)

@app.route('/')
def index():
	return 'Machine Learning Service in Progress!'

app.register_blueprint(IrisBlueprint)
app.register_blueprint(ErrorHandlerBlueprint)

if __name__ == '__main__':
	app.run(debug=True)
