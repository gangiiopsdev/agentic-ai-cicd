from fastapi import FastAPI
import subprocess
generate_safe_command = {'ping': ['ping', '-c', '1']}
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if host in generate_safe_command['ping']:
        subprocess.run(generate_safe_command['ping'], check=True)
    else:
        raise ValueError('Invalid host')
    return {"status": "completed"}