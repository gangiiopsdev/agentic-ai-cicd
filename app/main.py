from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = lambda host: ["ping", shlex.quote(host)]
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    command = generate_ping_command(host)
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {
        "status": "completed",
        "output": result.stdout.decode()
    }