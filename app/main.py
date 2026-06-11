from fastapi import FastAPI
import subprocess

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

app = FastAPI()
@app.get("/ping")
def ping(host: str):\n    sanitized_host = sanitize_host(host)\n    try:\n        result = subprocess.run(['ping', '-c', '1', '--'] + [sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)\n        return {"status": "completed", "output": result.stdout.decode()}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": str(e)}