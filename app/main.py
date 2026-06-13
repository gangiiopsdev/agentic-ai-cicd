from fastapi import FastAPI
import subprocess
def escape_shell_arg(s):
    return ' '.join(shlex.quote(arg) for arg in s.split())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = escape_shell_arg(host)
    try:
        result = subprocess.run(['ping', safe_host], check=True, text=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}