from fastapi import FastAPI
import subprocess
def escape_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, host))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    escaped_host = escape_host(host)
    if escaped_host != host:
        return {"status": "error", "message": "Invalid characters in host name"}
    subprocess.call(['ping', escaped_host])
    return {"status": "completed"}