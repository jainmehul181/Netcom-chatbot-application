from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

# 🗣️ API endpoint for chatbot messages
@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message", "").lower().strip()

    # Check if user_message matches friendly replies
    if user_message in friendly_replies:
        return jsonify({"reply": friendly_replies[user_message]})

    # Default fallback reply
    return jsonify({
        "reply": "🤖 I'm still learning! You can ask me about NETCOM courses, fees, placements, internships, or contact info."
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
