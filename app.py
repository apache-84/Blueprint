from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

classes = [
    {"id": 1, "class": "CSCI265", "name": "Software Engineering", "link": "/csci265"},
    {"id": 2, "class": "CSCI260", "name": "Data Structures and Algorithms", "link": "/csci260"},
    {"id": 3, "class": "CSCI159", "name": "Computer Science I", "link": "/csci159"},
    {"id": 4, "class": "CSCI161", "name": "Computer Science II", "link": "/csci161"},
    {"id": 5, "class": "CSCI375", "name": "Systems and Analysis", "link": "/csci375"},
    {"id": 6, "class": "CSCI261", "name": "Assembly", "link": "/csci261"},
]

@app.route('/search', methods=["GET"])
def search():
    query = request.args.get("q", "").strip().lower()

    if not query:
        return jsonify({"error": "No search query provided"}), 400
    
    results = [item for item in classes if query in item["class"].lower()]

    return jsonify(results)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/CSCI159')
def csci159():
    return render_template("course.html", classes=classes)

if __name__ == '__main__':
    app.run(debug=True)