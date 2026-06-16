from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', '--', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()
@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)