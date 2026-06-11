from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.list2cmdline([sanitize_host(part) for part in shlex.split(host)])
    result = subprocess.run(sanitized_host, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}