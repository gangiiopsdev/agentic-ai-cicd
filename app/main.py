from fastapi import FastAPI
import subprocess
import shlex
def safe_host(host):
    return host.replace('&&', '').replace(';', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = safe_host(host)
    try:
        result = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, timeout=5, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}