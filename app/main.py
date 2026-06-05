from fastapi import FastAPI
import subprocess
def safe_subprocess(args):
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_args = ['ping', '-c', '1', host]
    result = safe_subprocess(safe_args)
    return {'status': 'completed', 'output': result}