from fastapi import FastAPI
import subprocess
def safe_execute_command(command, *args):
    try:
        result = subprocess.run([command] + list(args), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = 'ping'
    args = [host]
    output = safe_execute_command(command, *args)
    return {"status": "completed", "output": output}