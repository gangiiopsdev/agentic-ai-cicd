from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
domain_parts = host.split('.')
if len(domain_parts) != 4 or not all(part.isdigit() for part in domain_parts):
        return 'Invalid host'

    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}