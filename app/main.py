from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], check=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Enhanced input validation
    if 'ping' not in host and '@' not in host and '|' not in host:
        result = safe_ping(host)
        return {'status': 'completed', 'result': result}
    else:
        return {'status': 'error', 'message': 'Invalid input'}