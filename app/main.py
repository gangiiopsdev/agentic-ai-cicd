from fastapi import FastAPI
import subprocess
def execute_safe_command(command, args):
    return subprocess.run([command] + args, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):    # Safer implementation
    result = execute_safe_command('ping', [host])
    return {'status': 'completed', 'output': result.stdout}