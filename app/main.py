from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Use subprocess.run with shell=False and capture_output=True to mitigate risks
    command = ['ping', sanitized_host]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}