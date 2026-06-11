from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command, args):
    try:
        result = subprocess.run([command] + args, capture_output=True, text=True, timeout=5)
        return result.stdout
    except subprocess.TimeoutExpired:
        return None

@app.get("/ping")
def ping(host: str):
    output = execute_command('ping', [host])
    if output:
        return {"status": "completed", "output": output}
    else:
        return {"status": "timeout"}