from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def validate_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return all(char in allowed_chars for char in input_string)

global ping = app.get("/ping")
def ping(host: str):
    if not validate_input(host):
        return {"error": "Invalid input"}, 400
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {"status": "completed"}