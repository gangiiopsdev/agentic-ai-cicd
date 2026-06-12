from fastapi import FastAPI
import subprocess
generate_ping_command = subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = generate_ping_command.stdout
    return {'status': 'completed', 'result': result}