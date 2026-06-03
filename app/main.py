from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_hostname(hostname):
    # Define a set of allowed hosts or patterns
    allowed_hosts = {'example.com', 'test.com'}
    return hostname in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        # Use a safe command and avoid shell=True
        args = ['ping', shlex.quote(host)]  # Securely quote the hostname to prevent injection
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}