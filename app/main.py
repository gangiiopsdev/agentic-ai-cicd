from fastapi import FastAPI
import subprocess
def execute_command(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output, error = execute_command(command)
    if error:
        return {"status": "error", "message": str(error)}
    else:
        return {"status": "completed", "output": str(output)}