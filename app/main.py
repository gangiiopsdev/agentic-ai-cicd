from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        # Sanitize the host input to prevent command injection
        if not host.isalnum():
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = execute_ping(host)
    return {"status": "completed", "output": output}