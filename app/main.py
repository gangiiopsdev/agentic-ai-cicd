from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(allowed_chars.__contains__, input_string))

@app.get("/ping")
def ping(host: str):

    # Sanitize user input
    sanitized_host = sanitize_input(host)

    # Use subprocess.Popen for a safer execution
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=False)

    return {'status': 'completed', 'output': result.stdout}