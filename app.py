from flask import Flask, request, jsonify

app = Flask(__name__)

# Pamięć na wiadomości (prosta w ramach testów)
messages = []

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "Nieprawidłowe dane"}), 400
    messages.append(data['message'])
    return jsonify({"status": "Wiadomość zapisana"}), 200

@app.route('/receive', methods=['GET'])
def receive_messages():
    if not messages:
        return jsonify({"messages": []}), 200
    return jsonify({"messages": messages}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
