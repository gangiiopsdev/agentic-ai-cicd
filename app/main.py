from fastapi import FastAPI
import subprocess
generate_ping_command = ['ping', host]
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if host and host.isalnum():
        try:
            subprocess.run(generate_ping_command, check=True)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": str(e)}
    else:
        return {"status": "error", "message": "Invalid host parameter"}