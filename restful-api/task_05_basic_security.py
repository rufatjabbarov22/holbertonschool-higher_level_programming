# task_05_basic_security.py

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Sample users dictionary
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("adminpass"), "role": "admin"}
}

# Setup JWT secret key
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a strong secret key
jwt = JWTManager(app)

# Basic authentication routes
@app.route('/basic-protected')
@auth.login_required
def basic_protected_route():
    return "Basic Auth: Access Granted"

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

# JWT authentication routes
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected_route():
    return "JWT Auth: Access Granted"

# Role-based access control
@app.route('/admin-only')
@jwt_required()
def admin_only_route():
    current_user = get_jwt_identity()
    if users[current_user]['role'] == 'admin':
        return "Admin Access: Granted"
    else:
        return "Unauthorized Access", 403

# Error handling
@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": "Unauthorized access"}), 401

if __name__ == '__main__':
    app.run(debug=True)
