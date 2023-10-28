import bcrypt


def generate_password(password: str) -> str:
	return bcrypt.hashpw(
		password.encode(encoding="utf8"),
		bcrypt.gensalt()
	).decode(encoding="utf8")


def check_password(password: str, hashed_password: str) -> bool:
	return bcrypt.checkpw(bytes(password, encoding="utf8"), bytes(hashed_password, encoding='utf8'))
