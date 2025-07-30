from flask import Flask, request, jsonify
from predictor import predict_risk

app = Flask(__name__)

@app.route("/flood-risk", methods=["GET"])
def risk():
    precip = float(request.args.get("precip", 0))
    water_level = float(request.args.get("water_level", 0))
    risk = predict_risk(precip, water_level)
    return jsonify({"flood_risk": risk})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
