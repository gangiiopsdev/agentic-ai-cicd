from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output, _ = execute_command(command)
    return {"status": "completed", "output": output.decode()}