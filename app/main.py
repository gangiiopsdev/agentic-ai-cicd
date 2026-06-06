from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command: str):
    try:
        result = subprocess.run(command, shell=False, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    safe_command = f"ping {host}"
    output = execute_safe_command(safe_command)
    return {'status': 'completed', 'output': output}