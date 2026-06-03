from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/ping')
def ping(host: str):
    safe_command = ['ping', host]
    output = run_safe_command(safe_command)
    return {'status': 'completed' if not output.startswith('ping:') else 'error', 'output': output}