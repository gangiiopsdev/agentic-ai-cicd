from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('|', ' ')

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    allowed_hosts = ["example.com", "test.example.com"]
    if host not in allowed_hosts:
        return {"status": "failed", "error": "Invalid host"}
    try:
        escaped_host = escape_shell_argument(host)
        output = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}