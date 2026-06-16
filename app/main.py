from fastapi import FastAPI
import subprocess
generate_ping_command = ['ping', '-c', '4', '{host}']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.run(generate_ping_command.format(host=host), check=True)
    return {"status": "completed"}