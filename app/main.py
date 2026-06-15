from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    # Add your sanitization logic here, e.g., whitelist allowed hostnames/IPs
    return host

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = ["ping", shlex.quote(sanitized_host)]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}