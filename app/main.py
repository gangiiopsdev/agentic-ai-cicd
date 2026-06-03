from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = run_ping(host)
    return {'status': 'completed', 'result': result}