from fastapi import FastAPI
import subprocess
def execute_safe_command(command, args):
    try:
        result = subprocess.run([command] + args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = "ping"
    args = [host]
    output = execute_safe_command(command, args)
    return {"status": "completed", "output": output}