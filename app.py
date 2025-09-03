from flask import Flask, jsonify, request, abort
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'marian'
app.config['BASIC_AUTH_PASSWORD'] = 'matrix'

basic_auth = BasicAuth(app)

news = [{"id": 0, "title": "", "content": ""}]
next_id = 1

@app.route("/", methods=["GET"])
def index():
	pass

@app.route("/news", methods=["GET"])
def list_news():
	return jsonify({"count": len(news), "items": news})

@app.route("/news", methods=["POST"])
@basic_auth.required
def create_news():
	global next_id
	data = request.json
	data["id"] = next_id
	next_id += 1
	news.append(data)
	return jsonify(data), 201

@app.route("/news/<int:item_id>", methods=["PUT"])
@basic_auth.required
def update_news(item_id: int):
	item = news[item_id]
	data = request.json
	for key in ("title", "content"):
		if key in data:
			item[key] = data[key]
	return jsonify(item)

@app.route("/news/<int:item_id>", methods=["DELETE"])
@basic_auth.required
def delete_news(item_id: int):
	del news[item_id]
	return jsonify({"status": "deleted", "id": item_id})

if __name__ == "__main__":
	app.run(threaded=True, host='0.0.0.0', port=3000)

