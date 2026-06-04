from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with shell=False and proper sanitization
    try:
        output = subprocess.check_output(shlex.split(f'ping -c 1 {host}'), stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}
    except Exception as e:
        return {"status": "failed", "error": str(e)}