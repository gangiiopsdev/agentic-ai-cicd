from fastapi import FastAPI
import subprocess
def run_secure_command(command, *args):
    process = subprocess.Popen([command] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        raise Exception(f'Command failed: {error.decode()}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    run_secure_command('ping', host)
    return {"status": "completed"}