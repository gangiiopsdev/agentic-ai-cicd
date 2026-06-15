from fastapi import FastAPI
import subprocess
cimport = subprocess.check_output

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = cimport(f"ping {host}", shell=False, text=True)
        return {"status": "completed", "result": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}