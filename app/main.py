from fastapi import FastAPI
import subprocess
global_result = {
    "status": "completed"
}
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        global_result['output'] = result.stdout
    except subprocess.CalledProcessError as e:
        global_result['error'] = str(e.stderr)
    return global_result