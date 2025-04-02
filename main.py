from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# جایگزین کردن کلید OpenAI API (از کشور مجاز بگیر)
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_message}]
    }
    
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
