from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: str):
    process = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    output, error = execute_command(command)
    if error:
        return {"status": "error", "message": error}
    else:
        return {"status": "completed", "output": output}