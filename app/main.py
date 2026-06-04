from fastapi import FastAPI
import subprocess
def escape_host(host: str) -> str:
    return ''.join(c if c.isalnum() or c in '-.' else '_' for c in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    try:
        result = subprocess.run(['ping', f'-c 1 {safe_host}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}