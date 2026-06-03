from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command_parts):
    try:
        completed_process = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return completed_process.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    command_parts = ['ping', host]
    result = run_command(command_parts)
    return {'status': 'completed', 'result': result}