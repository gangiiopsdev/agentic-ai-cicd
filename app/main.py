from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Sanitize host input
        sanitized_host = subprocess.check_output(f'echo {host} | cut -d" " -f1'.split()).decode().strip()
        subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)