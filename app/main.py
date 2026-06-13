from fastapi import FastAPI
import subprocess

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(allowed_chars.__contains__, input_str))

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', f'-c 1 {sanitized_host}']  # Corrected to avoid shell=True
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}