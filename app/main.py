from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    url_parts = urlparse(host)
    if not all([url_parts.scheme, url_parts.netloc]):
        return {'status': 'failed', 'error': 'Invalid host'}
    safe_host = subprocess.list2cmdline([host])
    try:
        result = subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive Controls
# - Use parameterized queries or ORM instead of raw SQL when dealing with databases.
# - Avoid using the shell=True argument in subprocess calls if possible.
# - Validate and sanitize all user inputs before processing them.