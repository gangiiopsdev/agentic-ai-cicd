from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        # Validate the host input to prevent injection attacks
        if not host or not isinstance(host, str) or ' ' in host:
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)