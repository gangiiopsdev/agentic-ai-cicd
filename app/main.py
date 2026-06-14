from fastapi import FastAPI
import subprocess
def run_command(command: list) -> str:
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    return {'status': 'completed', 'output': run_command(command)}