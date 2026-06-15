from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: str):
    try:
        result = subprocess.run(command, check=True, shell=False, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error executing command: {e.output}'

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = ['ping', host]
    output = execute_command(' '.join(command))
    return {'status': 'completed', 'output': output}