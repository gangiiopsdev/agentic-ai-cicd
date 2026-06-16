from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command: str):
    try:
        completed_process = subprocess.run(command, shell=False, check=True)
        return completed_process.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e.returncode}, Output: {e.output.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    result = execute_safe_command(command)
    return {"status": "completed", "result": result}