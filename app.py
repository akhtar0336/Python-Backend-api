from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Soheb", "course": "Data Analyst"},
    {"id": 2, "name": "Aman", "course": "Python Developer"}
]

@app.route('/')
def home():
    return "Backend API is Running!"

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify({"message": "Student Added", "data": new_student})

if __name__ == '__main__':
    app.run(debug=True)
