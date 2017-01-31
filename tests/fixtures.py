correct_params = {
    'username': 'test_user',
    'email': 'testuser@gmail.com',
    'password': 'test1234'
}

# ----- Password -----
params_without_pass = {
    'username': 'test_user',
    'email': 'testuser@gmail.com',
}

minlength_pass = {
    'username': 'test_user',
    'email': 'testuser@gmail.com',
    'password': 'test'
}

maxlength_pass = {
    'username': 'test_user',
    'email': 'testuser@gmail.com',
    'password': 'testtestets165565j6536565165165165165165165165165165rege'
                'rgergergerger6g51e65r1gergergerg1651651'
}

# ----- Username -----
params_without_username = {
    'email': 'testuser@gmail.com',
    'password': 'test1234'
}

minlength_username = {
    'username': 'tes',
    'email': 'testuser@gmail.com',
    'password': 'test1234'
}

maxlength_username = {
    'username': 'test1test2test3test45',
    'email': 'testuser@gmail.com',
    'password': 'test1234'
}

# ----- Email -----
params_without_email = {
    'username': 'test_user',
    'password': 'test1234'
}