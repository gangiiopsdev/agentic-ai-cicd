from fastapi import FastAPI
import subprocess
def safe_subprocess_call(command, args):
    try:
        result = subprocess.run([command] + args, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e.stderr.strip()}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 50:
        return {'status': 'error', 'message': 'Invalid input'}
    output = safe_subprocess_call('ping', ['-c', '1', f'"{host}"'])
    return {'status': 'completed', 'output': output}