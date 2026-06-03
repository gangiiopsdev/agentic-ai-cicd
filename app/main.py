from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using list of arguments
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stderr": str(e)}

app = FastAPI()
@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/secure-ping")
def secure_ping(host: str):
    # Secure implementation using list of arguments
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stderr": str(e)}