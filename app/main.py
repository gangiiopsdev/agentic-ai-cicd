from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        # Validate the host input to ensure it only contains valid characters
        if not all(c.isalnum() or c in ['-', '.'] for c in host):
            raise ValueError('Invalid host name')
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return execute_ping(host)