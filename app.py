from flask import Flask, request, jsonify, render_template_string
from recommender import recommend_assessments

app = Flask(__name__)

# 🏠 Home Page (UI)
@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Job Role Recommender</title>
            <style>
                body {
                    background-color: #f0f8ff;
                    font-family: Arial, sans-serif;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                }
                textarea {
                    padding: 10px;
                    font-size: 16px;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                    width: 300px;
                }
                input[type="submit"] {
                    padding: 10px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <h2>Job Role Recommender</h2>
            <form method="POST" action="/recommend">
                <textarea name="query" rows="5" placeholder="Type your job description here..."></textarea><br><br>
                <input type="submit" value="Get Recommendations">
            </form>
        </body>
        </html>
    ''')

# 🔍 Form-based recommendation
@app.route('/recommend', methods=['POST'])
def recommend():
    query = request.form.get('query', '').strip()

    # ✅ Input validation
    if not query:
        return jsonify({"error": "Please enter a job description"})

    try:
        results = recommend_assessments(query)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)})

# 🔗 API endpoint (GET)
@app.route('/api/recommend', methods=['GET'])
def api():
    query = request.args.get("query", "").strip()

    if not query:
        return jsonify({"error": "Query parameter is required"})

    try:
        results = recommend_assessments(query)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)})

# 🚀 Run app
if __name__ == '__main__':
    app.run(debug=True)