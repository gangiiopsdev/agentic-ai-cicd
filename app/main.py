from fastapi import FastAPI
import subprocess
def validate_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_/\')
    return all(char in allowed_chars for char in input_str)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_input(host):
        raise ValueError("Invalid host input")
    # Secure implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}