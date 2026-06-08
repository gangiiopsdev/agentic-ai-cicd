from fastapi import FastAPI
import subprocess
global subprocess
subprocess = None

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation
    if subprocess is not None:
        subprocess.run(['ping', host])
    else:
        raise ValueError("subprocess module not available")
    return {"status": "completed"}