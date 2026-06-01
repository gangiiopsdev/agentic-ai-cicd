from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized_input = ''.join(filter(allowed_chars.__contains__, input_str))
    return sanitized_input

@app.get("/ping")
def ping(host: str):

    # Sanitize the input
    host = sanitize_input(host)

    # Use subprocess without shell=True for security
    result = subprocess.run(['ping', host], capture_output=True, text=True)

    return {'status': 'completed', 'result': result.stdout}