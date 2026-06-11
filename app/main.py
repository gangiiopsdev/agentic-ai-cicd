from fastapi import FastAPI
import subprocess
import shlex
global_result = {}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global global_result
    try:
        # Validate and sanitize input
        if not host or not host.isalnum():
            raise ValueError("Invalid hostname")
        result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True, check=True)
        global_result['output'] = result.stdout
        return {"status": "completed", "output": result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        global_result['error'] = str(e)
        return {"status": "failed", "error": str(e)}