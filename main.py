from typing import Annotated

from fastapi import FastAPI, Depends

from logic import generate_password, check_password


app = FastAPI()


@app.get('/hash_password', name="hash_password")
async def hash_password(password: Annotated[str, Depends()]) -> dict:
	hashed_password = generate_password(password)
	return {'hashed_password': hashed_password}


@app.get('/check_password', name="check-password")
async def check_password(password: Annotated[str, Depends()]) -> dict:
	return {'ok': check_password(password)}
