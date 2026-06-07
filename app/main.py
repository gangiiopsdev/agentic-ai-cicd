from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate host format if necessary
        subprocess.call(['ping', quote(host)], shell=False)
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return {'status': 'completed'}