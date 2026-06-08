from fastapi import FastAPI
import subprocess
import shlex

def execute_ping(host: str):
    try:
        # Validate the host parameter to ensure it only contains allowed characters
        if not host.isalnum():
            raise ValueError('Invalid host input')
        
        # Use shlex.quote to safely escape any shell metacharacters in the host input
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)