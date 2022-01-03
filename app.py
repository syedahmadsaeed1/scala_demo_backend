import json

from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS()
cors.init_app(app)

@app.route('/get_todo_list')
def get_to_list():
    try:
        f = open("todo_list.txt", "r")
        file = f.readlines()
        todo_list = []
        for i in file:
            if i != "\n":
                todo_list.append(json.loads(i))
        f.close()
        return jsonify(todo_list)
    except FileNotFoundError:
        return make_response(jsonify("No todo list found"), 404)


@app.route('/update_todo_item', methods=['POST'])
def update_todo_item():
    try:
        item = json.loads(request.data.decode())
        f = open("todo_list.txt", "r")
        data = f.readlines()
        f.close()
        f = open("todo_list.txt", "w")
        ind = item["index"]
        item = item["item"]
        data[ind] = json.dumps(item) + "\n"
        f.writelines(data)
        f.close()
        return make_response(jsonify("Todo item updated"), 200)
    except Exception as e:
        return make_response(jsonify("Todo item not updated"), 404)


@app.route('/delete_todo_item', methods=['POST'])
def delete_todo_item():
    try:
        item = json.loads(request.data.decode())
        f = open("todo_list.txt", "r")
        data = f.readlines()
        f.close()
        f = open("todo_list.txt", "w")
        ind = item["index"]
        item = item["item"]
        data.remove(data[ind])
        f.writelines(data)
        f.close()
        return make_response(jsonify("Todo item updated"), 200)
    except Exception as e:
        return make_response(jsonify("Todo item not updated"), 404)


@app.route('/add_todo_item', methods=['POST'])
def add_todo_item():
    try:
        item = request.data.decode()
        f = open("todo_list.txt", "a")
        f.write(item + "\n")
        f.close()
        return make_response(jsonify("Todo item added"), 200)
    except Exception as e:
        item = json.loads(request.data.decode())
        f = open("todo_list.txt", "w")
        f.write(item + "\n")
        f.close()

if __name__ == '__main__':
    app.run()
