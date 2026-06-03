from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the input using shlex.quote
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': f'Ping failed: {e.stderr}'}