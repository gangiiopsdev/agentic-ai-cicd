from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    try:
        # Validate host input to ensure it only contains allowed characters
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            return 'Invalid host'
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to avoid command injection
    sanitized_host = host.replace(';', '').replace('&', '')
    return safe_ping(sanitized_host)