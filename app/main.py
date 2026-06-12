from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        socket.inet_aton(host)
        subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (socket.error, subprocess.CalledProcessError) as e:
        return {"status": "error", "message": str(e)}

    return {"status": "completed"}