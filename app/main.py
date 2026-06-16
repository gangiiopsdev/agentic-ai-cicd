from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command: str):
    try:
        result = subprocess.run(command.split(), capture_output=True, check=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    output = run_command(command)
    return {"status": "completed", "output": output}