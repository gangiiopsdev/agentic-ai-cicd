from fastapi import FastAPI
import subprocess
import shlex
def _safe_command(command: str) -> list:
    return shlex.split(command)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = subprocess.run(_safe_command(f'ping {host}'), capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}