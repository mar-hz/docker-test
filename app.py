from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
	return jsonify({"message": "yippie yippie yippie yippie"})

if __name__ == "__main__":
	app.run(threaded=True, host='0.0.0.0', port=3000)

