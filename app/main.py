from fastapi import FastAPI
import subprocess
tostring = lambda x: x.replace('\n', '\\n').replace('\t', '\\t')
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        raise ValueError("Invalid hostname")
    # Use a whitelist of allowed hosts instead of validating the input
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError("Host is not allowed")
    result = subprocess.run(['ping', tostring(host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}