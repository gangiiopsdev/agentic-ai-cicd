from fastapi import FastAPI
import subprocess
import re

class PingCommand:
    @staticmethod
def sanitize_input(input_string):
        return re.sub(r'[^a-zA-Z0-9.-_@:]', '', input_string)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = PingCommand.sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}