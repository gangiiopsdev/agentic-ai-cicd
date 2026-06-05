from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        output = subprocess.run(['ping', f"-c 4 {sanitized_host}"], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}