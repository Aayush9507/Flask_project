users = [

    {
        'id': 1,
        'username': 'aayush',
        'password': 'asdf'
    }
]

username_mapping = {'aayush': {

    'id': 1,
    'username': 'aayush',
    'password': 'asdf'
    }

}

userid_mapping = {1: {

    'id': 1,
    'username': 'aayush',
    'password': 'asdf'
    }

}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user is not None and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

