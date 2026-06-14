from fastapi import FastAPI
import subprocess
def execute_command(command, *args):
    if not all(arg.isalnum() for arg in args) and command != 'ping':  # Basic validation
        raise ValueError('Invalid input')
    result = subprocess.run([command] + list(args), capture_output=True, text=True, check=True, shell=False)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = execute_command('ping', host)
    return {'status': 'completed', 'output': output}