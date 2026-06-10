from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize user input to prevent command injection
        safe_host = subprocess.list2cmdline([host])
        result = subprocess.Popen(['ping', safe_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}