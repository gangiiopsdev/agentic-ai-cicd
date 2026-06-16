from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_input(user_input):
    return subprocess.list2cmdline(user_input)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        escaped_host = escape_input([host])
        result = subprocess.run(escaped_host, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}