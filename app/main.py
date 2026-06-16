from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Simple validation for demonstration purposes
    return host.strip().replace('.', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    command = ['ping', '-c', '1', host]  # Use specific options to mitigate risks and include the host in the command
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {"status": "completed", "output": result.stdout}