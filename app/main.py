from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use shell=False and avoid passing user input directly to shell commands
        output = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr.decode()}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}