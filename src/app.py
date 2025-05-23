from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "First task", "done": False }
    
]
@app.route('/todos', methods=['GET'])
def hello_world():
    return todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json.todos
    print("Incoming request with the following body", request_body)
    return todos

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)