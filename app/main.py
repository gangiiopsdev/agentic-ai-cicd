from fastapi import FastAPI
import subprocess
global ping_counter
ping_counter = 0

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_counter
    if ping_counter < 10:
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": output.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}
    else:
        return {"status": "rate_limited"}

    ping_counter += 1