@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request"}), 400