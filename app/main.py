from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    command = generate_ping_command(host)
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()} except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}