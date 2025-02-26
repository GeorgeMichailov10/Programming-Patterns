from flask_pymongo import PyMongo
from flask import Flask
from flask import request, jsonify
import uuid

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/users"
mongo = PyMongo(app)
#mongo.db.create_collection('users')

# What attributes does a user need have?

# Email
# Username
# Password

# Route for creating users
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json

    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({"error": f"Arguments not provided\n{username} {password} {email}"}), 400
    
    try:
        user = mongo.db.users.find_one({'username' : username})
        if user:
            return jsonify({'error' : 'Username already taken'}), 400
    except Exception as e:
        return jsonify({"error" : str(e)}), 500

    user = {
        'username' : username,
        'password' : password,
        'email' : email
    }

    try:
        mongo.db.users.insert_one(user)
        return jsonify({"msg: User added successfully"})
    except Exception as e:
        return jsonify({"error" : str(e)}), 500


# Route for update password
@app.route('/user', methods=['PUT'])
def update_password():
    data = request.json

    username = data.get('username')
    newPassword = data.get('newpassword')

    if not username or not newPassword:
        return jsonify({'error' : 'Missing required input'}), 400
    
    try:
        result = mongo.db.users.update_one(
            {'username' : username},   # Object we are looking for
            {"$set" : {'password' : newPassword}}   # Set means updating the object located and we are only changing password
        )

        if result.matched_count == 0:
            return jsonify({'error': "No user found"}), 404
        elif result.modified_count == 0:
            return jsonify({"error" : "No change was made"}), 500
        else:
            return jsonify({"msg" : f"Password for {username} has been updated."}), 200
    except Exception as e:
        return jsonify({"error": str(e)})

# Route for getting a user
@app.route('/user', methods=['GET'])
def get_user():
    data = request.json
    
    username = data.get('username')
    if not username:
        return jsonify({"error" : "No username provided"}), 400
    
    try:
        user = mongo.db.users.find_one({'username' : username})

        if user:
            user['_id'] = str(user['_id'])
            return jsonify(user), 200
        else:
            return jsonify({"error" : "No user found"}), 404
    except Exception as e:
        return jsonify({"error" : str(e)}), 500

# Delete a user
@app.route('/user', methods=['DELETE'])
def delete_user():
    data = request.json

    username = data.get('username')
    if not username:
        return jsonify({"error" : "Username not found"}), 400
    
    try:
        result = mongo.db.users.delete_one({'username' : username})
        if result.deleted_count == 1:
            return jsonify({"msg" : f"User {username} deleted successfully"}), 200
        else:
            return jsonify({"error" : "User not found"}), 404
    except Exception as e:
        return jsonify({"error" : str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
