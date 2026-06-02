from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Sanitize input
    host = host.strip()
    if ' ' in host or '"' in host:
        raise ValueError('Invalid host name')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.returncode} - {e.stderr.strip()}

@app.post("/ping")
def ping(host: str):
    # Secure implementation
    output = run_ping(host)
    return {'status': 'completed', 'output': output}