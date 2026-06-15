from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command, *args):
    if command not in ['ping', 'ls']:
        raise ValueError('Invalid command')
    return subprocess.run([command] + list(args), capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):  
    # Secure implementation
    result = execute_safe_command("ping", host)
    return {"status": "completed", "output": result.stdout}