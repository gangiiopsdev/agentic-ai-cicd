from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Ensure the host input does not contain malicious content
        result = subprocess.run(['ping', subprocess.quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)