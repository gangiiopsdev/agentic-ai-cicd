from fastapi import FastAPI
import subprocess
def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    return stdout, stderr

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    stdout, stderr = execute_command(command)
    if stderr:
        return {"status": "failed", "error": stderr}
    else:
        return {"status": "completed", "output": stdout}