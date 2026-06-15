from fastapi import FastAPI
import subprocess
generate_subprocess_command = lambda cmd, *args: [cmd] + list(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(generate_subprocess_command("ping", host))
    return {"status": "completed"}