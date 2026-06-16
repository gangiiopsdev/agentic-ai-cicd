from fastapi import FastAPI
import subprocess
generate_ping_command = ['ping', '--count=1', '{host}']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(generate_ping_command.format(host=host))
    return {"status": "completed"}