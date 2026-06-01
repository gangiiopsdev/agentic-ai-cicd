from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    try:
        safe_host = host.strip()[:100]  # Limit length to prevent excessive input
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)