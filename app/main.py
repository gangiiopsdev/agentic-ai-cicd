from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command, *args):
    return subprocess.run([command] + list(args), capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    result = execute_command('ping', host)
    return {'status': 'completed', 'output': result.stdout}