from fastapi import FastAPI
import subprocess
def execute_command(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    cmd = ["ping", host]
    output, error = execute_command(cmd)
    if error:
        return {"status": "error", "error": error}
    else:
        return {"status": "completed", "output": output}