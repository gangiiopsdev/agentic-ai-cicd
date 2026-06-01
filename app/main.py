from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command, args):
    result = subprocess.run([command] + args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': execute_command('ping', [host])}