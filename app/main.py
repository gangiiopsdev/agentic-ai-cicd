from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}