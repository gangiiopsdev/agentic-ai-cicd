from fastapi import FastAPI
import subprocess
def sanitize_input(input_str: str) -> str:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(filter(allowed_chars.__contains__, input_str))
def is_valid_host(host: str) -> bool:
    # Add validation logic for the host here
    return '.' in host
app = FastAPI()
@app.get("/ping")
def ping(host: str) -> Dict[str, str]:
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    sanitized_host = subprocess.quote(sanitize_input(host))
    try:
        result = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}