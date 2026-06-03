from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ["ping", host]
    response = run_command(command)
    return {"status": "completed", "response": response}