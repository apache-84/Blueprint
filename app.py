from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

items = [
    {"id": 1, "title": "Apple iPhone 15", "category": "Smartphones"},
    {"id": 2, "title": "Samsung Galaxy S23", "category": "Smartphones"},
    {"id": 3, "title": "Sony WH-1000XM4 Headphones", "category": "Headphones"},
    {"id": 4, "title": "MacBook Pro 16-inch", "category": "Laptops"},
    {"id": 5, "title": "Dell XPS 15", "category": "Laptops"},
    {"id": 6, "title": "Google Pixel 7", "category": "Smartphones"},
]

@app.route('/search', methods=["GET"])
def search():
    query = request.args.get("q", "").strip().lower()

    if not query:
        return jsonify({"error": "No search query provided"}), 400
    
    results = [item for item in items if query in item["title"].lower()]

    return jsonify(results)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)