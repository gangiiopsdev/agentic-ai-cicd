from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in input_string:
        if char not in allowed_chars:
            return False
    return True

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_input(host):
        # Secure implementation using subprocess.run with shell=False and argument unpacking
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}, 400