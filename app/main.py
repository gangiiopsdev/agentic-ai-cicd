from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> str:
    if host.strip() and all(c.isalnum() or c in '.-' for c in host):  # Basic validation
        command = ['ping', '-c', '1', host]  # Limit the number of pings to mitigate potential abuse
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Invalid input'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host parameter to prevent command injection
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        return safe_ping(host)
    else:
        return {"error": "Invalid input"}