from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Secure implementation using shlex.quote to escape special characters in the host input.
    from shlex import quote
    result = subprocess.run(['ping', '-c', '1', quote(host)], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = secure_ping(host)
    return {'status': 'completed', 'output': output}