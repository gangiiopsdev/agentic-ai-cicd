from fastapi import FastAPI
import subprocess

class PingException(Exception):
    pass

def sanitize_host(host: str) -> str:
    return shlex.quote(host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        # Secure implementation using subprocess.run to avoid shell injection and check return code
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(result.stderr)
        return {'status': 'completed'}
    except Exception as e:
        raise PingException(str(e))