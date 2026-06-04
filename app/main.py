from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    return output, error

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    result, error = run_command(command)
    if error:
        return {"status": "failed", "error": error}
    else:
        return {"status": "completed", "result": result}