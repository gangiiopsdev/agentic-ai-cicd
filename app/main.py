from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Validate input to prevent command injection
        if not host.isalnum():
            raise ValueError('Invalid input')
        args = ['ping', '-c', '1', shlex.quote(host)]
        result = subprocess.run(args, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)