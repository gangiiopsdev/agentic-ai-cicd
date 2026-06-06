from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        args = ['ping', host]
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}