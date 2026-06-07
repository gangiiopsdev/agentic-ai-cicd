from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in input_string)

@app.get("/ping")
def ping(host: str):
    if not validate_input(host):
        raise ValueError('Invalid input')

    # Safe implementation
    subprocess.call(f'ping {host}', shell=False)

    return {"status": "completed"}