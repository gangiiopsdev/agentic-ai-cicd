from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize input to prevent command injection
        if '&&' in host or ';' in host or '|' in host:
            raise ValueError('Invalid characters in host parameter')
        safe_host = subprocess.list2cmdline([host])
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}