from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f"ping {host}")
    result = subprocess.run(args, shell=False, check=True)
    return {'status': 'completed', 'returncode': result.returncode}