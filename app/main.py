from fastapi import FastAPI
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    allowed_hosts = ["example.com", "test.com"]  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        return {"status": "error", "message": "Invalid host"}
    command = ["ping", host]
    output = run_command(command)
    return {"status": "completed", "output": output}