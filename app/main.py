from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = subprocess.list2cmdline([host])
    return safe_ping(safe_host)