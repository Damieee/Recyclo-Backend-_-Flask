from flask import request, jsonify, abort

# Define some sample rewards
reward_cards = [
    {
        'id': 1,
        'name': 'Amazon Gift Card',
        'points': 100
    },
    {
        'id': 2,
        'name': 'Starbucks Gift Card',
        'points': 100
    },
    {
        'id': 3,
        'name': 'Paypal',
        'points': 275
    },
    {
        'id': 4,
        'name': 'One Month Netflix Sub',
        'points': 75
    },
    {
        'id': 5,
        'name': 'Enter into a raffle',
        'points': 10
    }
]

# Define the API routes



@staticmethod
def get_rewards():
    return jsonify({'rewards': reward_cards})

@staticmethod
def get_reward(reward_id):
    reward = [reward for reward in reward_cards if reward['id'] == reward_id]
    if len(reward) == 0:
        abort(404)
    return jsonify({'reward': reward[0]})


@staticmethod
# @app.route('/rewards', methods=['POST'])
def create_reward():
    if not request.json or not 'name' in request.json or not 'points' in request.json:
        abort(400)
    reward = {
        'id': reward_cards[-1]['id'] + 1,
        'name': request.json['name'],
        'points': request.json['points']
    }
    reward_cards.append(reward)
    return jsonify({'reward': reward}), 201

@staticmethod
# @app.route('/rewards/<int:reward_id>', methods=['PUT'])
def update_reward(reward_id):
    reward = [reward for reward in reward_cards if reward['id'] == reward_id]
    if len(reward) == 0:
        abort(404)
    if not request.json:
        abort(400)
    reward[0]['name'] = request.json.get('name', reward[0]['name'])
    reward[0]['points'] = request.json.get('points', reward[0]['points'])
    return jsonify({'reward': reward[0]})


@staticmethod
# @app.route('/rewards/<int:reward_id>', methods=['DELETE'])
def delete_reward(reward_id):
    reward = [reward for reward in reward_cards if reward['id'] == reward_id]
    if len(reward) == 0:
        abort(404)
    reward_cards.remove(reward[0])
    return jsonify({'result': True})

