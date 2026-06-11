from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command, *args):
    result = subprocess.run([command] + list(args), capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = execute_command('ping', host)
    return {'status': 'completed', 'output': output}