from fastapi import FastAPI
import subprocess
def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    output, error = execute_command(command)
    if error:
        return {"status": "failed", "error": error.decode()}
    return {"status": "completed", "output": output.decode()}