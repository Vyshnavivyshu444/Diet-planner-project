from flask import Flask, render_template, request, jsonify
from logic import generate_plan as logic_generate_plan

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-plan', methods=['POST'])
def generate_plan_api():
    try:
        data = request.get_json()

        age = data.get('age')
        gender = data.get('gender')
        height = data.get('height')
        weight = data.get('weight')
        goal = data.get('goal')
        diet = data.get('diet')

        plan = logic_generate_plan(age,gender, height, weight, goal, diet)

        return jsonify({"plan": plan})

    except Exception as e:
        print("❌ ERROR in /generate-plan:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
