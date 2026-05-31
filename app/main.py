from fastapi import FastAPI
import subprocess
def sanitize_input(host):
    return ''.join(e for e in host if e.isalnum() or e == '.' or e == '-').strip()
app = FastAPI()
@app.get("/ping")
def ping(host: str): 
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"error": "Host parameter is empty, invalid, or contains special characters"}
    args = ['ping', '-c', '1', sanitized_host]
    subprocess.run(args, check=True)
    return {"status": "completed"}