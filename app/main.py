from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', sanitized_host]
    # Use subprocess.run instead of subprocess.call to avoid shell=True and potential injection
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}