from fastapi import FastAPI
import subprocess
generate_cmd = f'ping {host}'; subprocess.run(generate_cmd, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    generate_cmd = f'ping {host}'; subprocess.run(generate_cmd, shell=False)

    return {"status": "completed"}