from fastapi import FastAPI
import subprocess
import re
generate_ping_command = lambda host: ['ping', host]
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid host name"}
    try:
        result = subprocess.run(generate_ping_command(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}