from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output = run_command(command)
    return {"status": "completed", "output": output}