from flask import Flask, jsonify, request, abort

app = Flask(__name__)

news = [{"id": 0, "title": "", "content": ""}]
next_id = 1

@app.route("/", methods=["GET"])
def index():
	pass

@app.route("/news", methods=["GET"])
def list_news():
	return jsonify({"count": len(news), "items": news})

@app.route("/news", methods=["POST"])
def create_news():
	pass

@app.route("/news/<int:item_id>", methods=["POST"])
def update_news():
	pass

@app.route("/news/<int:item_id>", methods=["DELETE"])
def delete_news():
	pass

if __name__ == "__main__":
	app.run(threaded=True, host='0.0.0.0', port=3000)

