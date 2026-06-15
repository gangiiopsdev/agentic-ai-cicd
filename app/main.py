from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output, error = run_command(command)
    if error:
        return {"status": "failed", "error": error}
    return {"status": "completed", "output": output}