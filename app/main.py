from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(cmd):
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    cmd = ["ping", host]
    result = execute_command(cmd)
    return {"status": "completed", "result": result}