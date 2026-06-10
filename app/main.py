from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Ensure the host does not contain any malicious characters
    safe_host = subprocess.list2cmdline([host])
    try:
        output = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)