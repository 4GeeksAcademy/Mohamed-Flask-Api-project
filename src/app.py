from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "First task", "done": False } 
]

# Return all Todos
@app.route('/todos', methods=['GET'])
def hello_world():
    return todos

# Add a new todo
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    # print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos) 

# remove a todo
@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_new_todo(index):
    deleted_item = todos.pop(index)
    print('this position was deleted',deleted_item)
    jsonify(todos) 



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)