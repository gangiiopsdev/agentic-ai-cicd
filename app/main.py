from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_characters)

@app.get("/ping")
def ping(host: str):

    # Sanitize the input
    sanitized_host = sanitize_input(host)

    # Use subprocess.Popen instead of shell=True
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)

    return {'status': 'completed', 'output': result.stdout}