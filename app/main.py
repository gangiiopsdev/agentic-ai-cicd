from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        host_parts = shlex.split(host)
        result = subprocess.run(['ping'] + [shlex_quote.quote(arg) for arg in host_parts], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

def is_valid_host(host: str) -> bool:
    # Basic validation of the host format (e.g., no control characters)
    return all(c.isalnum() or c in [".", "-"] for c in host)