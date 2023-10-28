from logic import generate_password, check_password


def test_generate_password():
	password = 'password'
	hashed_password = generate_password(password)

	assert check_password(password, hashed_password)
