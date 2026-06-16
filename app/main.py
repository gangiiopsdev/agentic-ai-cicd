from fastapi import FastAPI
import subprocess
cmd = ["ping", "-c", "1"]
cmd.append(host)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.run(cmd, check=True, capture_output=True)
    return {"status": "completed"}