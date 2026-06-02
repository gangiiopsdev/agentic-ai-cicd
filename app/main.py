from fastapi import FastAPI
import subprocess
import re

def safe_ping(host):
    try:
        # Validate host input more strictly using regex for allowed characters and length
        if not re.match(r'^[a-zA-Z0-9._%+-]+$', host) or len(host) > 255:
            raise ValueError('Invalid input')
        args = ['ping', host]
        output = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)