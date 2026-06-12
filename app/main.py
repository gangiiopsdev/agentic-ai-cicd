from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_'))
def run_ping(host):\n    safe_host = sanitize_input(host)\n    result = subprocess.run(['ping', '-c', '1', f'"{safe_host}"'], capture_output=True, text=True)\n    return {'status': 'completed', 'output': result.stdout}\n
app = FastAPI()
@app.get('/ping')
def ping(host: str):\n    return run_ping(host)