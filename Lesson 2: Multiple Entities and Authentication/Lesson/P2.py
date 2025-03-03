from flask_pymongo import PyMongo
from flask import Flask
from flask import request, jsonify
import uuid
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/users"
mongo = PyMongo(app)
SECRET_KEY = "Class-2"
#mongo.db.create_collection('users')
#mongo.db.create_collection('cars')

# What attributes does a user need have?

# Username
# Password
# [] of car ids

# What attributes does a car have

# id
# License Plate

def middleware(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'error': 'Token is missing!'}), 403
        
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            username = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token!'}), 403
        
        return f(username, *args, **kwargs)
    
    return decorated
  

# Route for creating users
@app.route('/register', methods=['POST'])
def register():
    data = request.json

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": f"Arguments not provided\n{username} {password}"}), 400
    
    try:
        user = mongo.db.users.find_one({'username' : username})
        if user:
            return jsonify({'error' : 'Username already taken'}), 400
    except Exception as e:
        return jsonify({"error" : str(e)}), 500

    user = {
        'username' : username,
        'password' : generate_password_hash(password),
        'cars' : []
    }

    try:
        mongo.db.users.insert_one(user)
        return jsonify({"msg: User added successfully"})
    except Exception as e:
        return jsonify({"error" : str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": f"Arguments not provided\n{username} {password}"}), 400
    
    try:
        user = mongo.db.users.find_one({'username' : username})

        if check_password_hash(user['password'], password):
            jwt_config = {
                'username' : str(user['username']),
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }
            jwt_token = jwt.encode(jwt_config, SECRET_KEY, algorithm='HS256')
            return jsonify({'jwt' : jwt_token})
        
    except Exception as e:
        return jsonify({"error" : str(e)}), 500

# Route for update password
@app.route('/user/password', methods=['PUT'])
@middleware
def update_password(username):
    data = request.json

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
@middleware
def get_user(username):
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
@middleware
def delete_user(username):
    # Step 1: Get user
    # Step 2: For each car id: delete that car
    # Step 3: Delete the user
    
    pass

# Adding a car to a user
@app.route('/user', methods=['PUT'])
@middleware
def add_car(username):
    # Create the car in the car collection
    # Add id to user
    # To do this need: username, car license plate

    data = request.json
    license_plate = data.get('license')
    if not username or not license_plate:
        return jsonify({"error" : "Username not found"}), 400
    
    try:
        user = mongo.db.users.find_one( {'username' : username } )
        if not user:
            return jsonify({"error" : "User not found"}), 404
        
        # Make the car now that we know the user exists
        car = {
            '_id' : str(uuid.uuid4()),
            'license' : license_plate
        }

        try:
            mongo.db.cars.insert_one(car)

            result = mongo.db.users.update_one(
                {'username' : username},
                {"$push" : {'cars' : car['_id']}}
            )

            if result.modified_count == 0:
                return jsonify({"error" : "No change was made"}), 500
            
            return jsonify({"msg" : f"Successfully added {car['license']} to {username}"}), 200
            
        except Exception as e:
            return jsonify({"error" : str(e)}), 500

    except Exception as e:
        return jsonify({"error" : str(e)}), 500

# Getting a user's cars
@app.route('/car', methods=['GET'])
def get_user_car(username):
    if not username:
        return jsonify({"error" : "No username provided"}), 400
    
    try:
        user = mongo.db.users.find_one({'username' : username})

        if user:
            user['_id'] = str(user['_id'])
            return jsonify(user['cars']), 200
        else:
            return jsonify({"error" : "No user found"}), 404
    except Exception as e:
        return jsonify({"error" : str(e)}), 500
      



if __name__ == '__main__':
    app.run(debug=True)