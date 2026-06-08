from fastapi import FastAPI
import subprocess
class HomeResponse:
    message: str

app = FastAPI()

@app.get('/')
def home() -> HomeResponse:
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}