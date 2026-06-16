from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_characters)

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}