from flask_pymongo import PyMongo
from flask import Flask
from flask import request, jsonify
from bson import ObjectId
import uuid

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/users"
mongo = PyMongo(app)
#mongo.db.create_collection('users')

# Route for creating sets
# NOTE: I see that you're storing the length. That is completely unnecessary in this case since the sets are so small. Just call len(list) to get.
# NOTE: Why are you returning the whole object when you can just return the id of the set? Debugging right?
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json

    userSet = data.get('set')

    if not userSet:
        return jsonify({"error": f"Arguments not provided\n{userSet}"}), 400
    
    try:
        userSet = list(map(int, userSet.split(", ")))
    except Exception as e:
        return jsonify({"error" : str(e)}), 500

    nums = {
        'set' : userSet,
        'length' : len(userSet)
    }

    try:
        obj = mongo.db.users.insert_one(nums)
        # return jsonify({f"msg: Set added successfully\nID of set: {obj.inserted_id}"}), 200
        return jsonify(nums), 200
    except Exception as e:
        return jsonify({"error" : str(e)}), 500


# # Route for update password <- Huh?
# NOTE: Make two separate routes for adding and removing. Removing pops, up to you if you want to pop from the front or the back idrc. Adding appends
# NOTE: $set is for changing things. You are appending to a list  when adding so using $push.
@app.route('/user', methods=['PUT'])
def update_password():
    data = request.json

    setID = data.get('id')
    add = data.get('add')
    remove = data.get('remove')

    if not setID or (not add and not remove):
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


# NOTE: Please fix the function names and comments because it so hard to read.
# NOTE: setData is a terrible name because it looks like that's what you're trying to set the data to.
# NOTE: Your keys need to be consistent. You can't have message be dynamic. It should be something like "equation" : and then you can have a dynamic value
# The whole point of key: value in maps is so that you can look in a consistent place for dynamic data.
# Route for getting a user
@app.route('/user', methods=['GET'])
def get_user():
    data = request.json
    
    operators = data.get('operators')
    setID = data.get('id')

    if not setID:
        return jsonify({"error": f"Arguments not provided\n{setID} {operators}"}), 400
    
    try:
        setData = mongo.db.users.find_one({'_id' : ObjectId(setID)})

        if not setData:
            return jsonify({"error" : "No set found"}), 404

        if not operators:
            return jsonify({"Set" : setData["set"]})

        ops = operators.split(", ")

        if len(ops) + 1 != len(setData["set"]):
            return jsonify({"error" : "Wrong number of operations"}), 400

        nums = setData["set"]

        total = nums[0]
        msg = f"{nums[0]}"

        for i in range(len(nums)-1):
            if ops[i] == "+":
                total += nums[i+1]
                msg += f" + {nums[i+1]}"
            elif ops[i] == "-":
                total -= nums[i+1]
                msg += f" - {nums[i+1]}"
            elif ops[i] == "*":
                total *= nums[i+1]
                msg += f" * {nums[i+1]}"
            elif ops[i] == "/":
                total /= nums[i+1]
                msg += f" / {nums[i+1]}"
            else:
                return jsonify({"error" : "Invalid input"}), 400
        
        return jsonify({f"{msg}" : total})

        # if setData:
        #     return jsonify(setData), 200
        # else:
        #     return jsonify({"error" : "No set found"}), 404
        # # return jsonify({"msg": f"Found the user: {setData["set"]}"}), 200
        # return jsonify(setData), 200

    #     if setData:
    #         user['_id'] = str(user['_id'])
    #         return jsonify(user), 200
    #     else:
    #         return jsonify({"error" : "No set found"}), 404
    except Exception as e:
        return jsonify({"error" : str(e)}), 500

# Delete a user
@app.route('/user', methods=['DELETE'])
def delete_user():
    data = request.json
    
    setID = data.get('id')
    if not setID:
        return jsonify({"error": f"Arguments not provided\n{setID}"}), 400
    
    try:
        setData = mongo.db.users.delete_one({'_id' : ObjectId(setID)})
        if setData.deleted_count == 1:
            return jsonify({"msg" : f"Set {setID} deleted successfully"}), 200
        else:
            return jsonify({"error" : "Set not found"}), 404
    except Exception as e:
        return jsonify({"error" : str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
