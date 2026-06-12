from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e == '.' or e == '-' or e == '_')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}