from fastapi import FastAPI
import subprocess
global allowed_hosts = set(['example.com'])

app = FastAPI()

def escape_input(user_input):
    # Simple escaping, real-world use should be more robust
    return ''.join(c if c.isalnum() else '_' for c in user_input)

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {"status": "error", "message": "Invalid host"}
    escaped_host = escape_input(host)
    subprocess.call(['ping', escaped_host])
    return {"status": "completed"}