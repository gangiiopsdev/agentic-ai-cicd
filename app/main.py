from fastapi import FastAPI
import subprocess
def execute_safe_command(command, args):
    try:
        result = subprocess.run([command] + args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = 'ping'
    args = [host]
    output = execute_safe_command(command, args)
    return {'status': 'completed', 'output': output}