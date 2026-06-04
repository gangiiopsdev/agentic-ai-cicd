from fastapi import FastAPI
import subprocess
global ping_count
ping_count = 0

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_count
    if ping_count < 10:  # Limit the number of pings to prevent abuse
        try:
            output = subprocess.check_output(f"ping {host}", shell=False, text=True)
            return {"status": "completed", "output": output}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "exceeded limit"}