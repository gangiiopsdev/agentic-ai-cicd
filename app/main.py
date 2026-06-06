from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = subprocess.list2cmdline([host])
    try:
        output = subprocess.check_output(["ping", safe_host], universal_newlines=True, timeout=5)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "error", "message": str(e)}