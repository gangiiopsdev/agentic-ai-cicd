from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate host to prevent command injection
        socket.gethostbyname(host)
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}