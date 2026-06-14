from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation without shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
app = FastAPI()
@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get('/ping')
def ping(host: str):
    # Add input validation
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    return safe_ping(host)