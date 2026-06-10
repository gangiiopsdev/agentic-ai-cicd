from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.Popen for better security and easier handling
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout, 'error': result.stderr}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)