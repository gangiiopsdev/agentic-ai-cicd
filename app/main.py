from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isdigit():
        return 'Invalid input'
    return subprocess.call(['ping', host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, int) and 0 <= result <= 255:
        return {'status': 'completed', 'exit_code': result}
    else:
        return {'status': 'failed'}