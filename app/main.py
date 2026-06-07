from fastapi import FastAPI
import subprocess
app = FastAPI()

def safe_command(cmd):
    return [c for c in cmd.split() if c.isalnum()]

@app.get("/execute")
def execute_command(command: str):
    safe_commands = safe_command(command)
    result = subprocess.run(safe_commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
    return {'output': result.stdout, 'error': result.stderr}