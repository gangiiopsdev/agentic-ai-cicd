from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Validate and sanitize host input before passing to subprocess
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    return ping(host)

def is_valid_host(host: str) -> bool:
    # Example validation logic, adjust as needed
    return all(char.isalnum() or char in ('.', '-') for char in host)