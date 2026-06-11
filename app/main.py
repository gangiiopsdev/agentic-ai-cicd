from fastapi import FastAPI
import subprocess
generate_ping_command = ['ping', '--count=1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    generate_ping_command.append(host)
    subprocess.call(generate_ping_command)
    return {"status": "completed"}