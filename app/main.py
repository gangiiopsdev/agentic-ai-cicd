from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def quote_host(s):
    return ''.join(c if c.isalnum() or c in '-.' else '_' for c in s)

def is_safe_host(host):
    return all(char.isalnum() or char in '-.' for char in host)

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if not is_safe_host(host):
        return {"status": "failed", "error": "Invalid host name"}
    try:
        cmd = ['ping', '-c', '1', shlex.quote(quote_host(host))]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}