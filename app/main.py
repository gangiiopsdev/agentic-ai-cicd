from fastapi import FastAPI
import subprocess
def execute_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the input to prevent command injection
        if not host.isalnum():
            raise ValueError("Invalid host name")
        status = execute_ping(host)
        return {"status": "completed", "output": status}
    except Exception as e:
        return {"status": "failed", "error": str(e)}