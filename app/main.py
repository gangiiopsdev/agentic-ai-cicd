from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        # Validate host input to ensure it does not contain malicious commands
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)