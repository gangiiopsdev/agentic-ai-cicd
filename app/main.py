from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout, result.stderr

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    stdout, stderr = run_command(command)
    return {"status": "completed", "stdout": stdout, "stderr": stderr}