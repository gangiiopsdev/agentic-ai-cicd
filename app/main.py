from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate input to prevent injection attacks
    if not isinstance(host, str) or len(host.strip()) == 0:
        return 'Invalid input'
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}