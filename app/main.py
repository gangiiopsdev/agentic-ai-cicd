from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(allowed_chars.__contains__, input_string))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', f'"{sanitized_host}"'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode('utf-8'), "stderr": result.stderr.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stdout": e.output.decode('utf-8'), "stderr": e.stderr.decode('utf-8')}