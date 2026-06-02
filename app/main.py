from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use a whitelist for hosts if possible
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    args = ['ping', '--'] + [host]  # Add -- to prevent command line injection
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}