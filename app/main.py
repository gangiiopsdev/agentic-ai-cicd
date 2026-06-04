from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    try:
        result = ping(host)
        return {"status": "completed", "result": result}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}