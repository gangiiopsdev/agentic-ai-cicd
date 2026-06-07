from fastapi import FastAPI
import subprocess
allow_hosts = {"example.com", "localhost"}

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):    
    sanitized_host = sanitize_input(host)
    if sanitized_host not in allow_hosts:
        return {"status": "failed", "error": "Host not allowed"}
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except subprocess.TimeoutExpired as e:
        return {"status": "timeout", "error": str(e)}