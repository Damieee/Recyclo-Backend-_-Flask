from flask import Flask, jsonify, request

app = Flask(__name__)

# Define some sample rewards
rewards = [
    {
        'id': 1,
        'name': 'Amazon Gift Card',
        'points': 100
    },
    {
        'id': 2,
        'name': 'Starbucks Gift Card',
        'points': 50
    },
    {
        'id': 3,
        'name': 'Free Movie Ticket',
        'points': 75
    },
    {
        'id': 4,
        'name': 'Get a Drink Card',
        'points': 25
    },
    {
        'id': 5,
        'name': 'Enter into a raffle',
        'points': 10
    }
]

# Define the API routes


@app.route('/rewards', methods=['GET'])
def get_rewards():
    return jsonify({'rewards': rewards})


@app.route('/rewards/<int:reward_id>', methods=['GET'])
def get_reward(reward_id):
    reward = [reward for reward in rewards if reward['id'] == reward_id]
    if len(reward) == 0:
        abort(404)
    return jsonify({'reward': reward[0]})


@app.route('/rewards', methods=['POST'])
def create_reward():
    if not request.json or not 'name' in request.json or not 'points' in request.json:
        abort(400)
    reward = {
        'id': rewards[-1]['id'] + 1,
        'name': request.json['name'],
        'points': request.json['points']
    }
    rewards.append(reward)
    return jsonify({'reward': reward}), 201


@app.route('/rewards/<int:reward_id>', methods=['PUT'])
def update_reward(reward_id):
    reward = [reward for reward in rewards if reward['id'] == reward_id]
    if len(reward) == 0:
        abort(404)
    if not request.json:
        abort(400)
    reward[0]['name'] = request.json.get('name', reward[0]['name'])
    reward[0]['points'] = request.json.get('points', reward[0]['points'])
    return jsonify({'reward': reward[0]})


@app.route('/rewards/<int:reward_id>', methods=['DELETE'])
def delete_reward(reward_id):
    reward = [reward for reward in rewards if reward['id'] == reward_id]
    if len(reward) == 0:
        abort(404)
    rewards.remove(reward[0])
    return jsonify({'result': True})


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
