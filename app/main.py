from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_chars)

def validate_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        sanitized_host = sanitize_input(host)
        try:
            output = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, shell=False)
            return {'status': 'completed', 'output': output.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}