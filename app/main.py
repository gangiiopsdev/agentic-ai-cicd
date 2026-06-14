from fastapi import FastAPI
import subprocess
def get_ip(ping):
    try:
        result = subprocess.run(['ping', '-c', '1', ping], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = get_ip(host)
    return {'status': 'completed' if not output.startswith('ping:') else 'failed', 'output': output}