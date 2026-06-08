from fastapi import FastAPI
import subprocess
def run_safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return str(e.output)
    except subprocess.TimeoutExpired:
        return "timeout"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = run_safe_ping(host)
    return {"status": "completed", "output": result}