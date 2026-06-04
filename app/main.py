from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str) -> str:
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return "Invalid host"
    
    # Use shlex to safely escape command arguments
    cmd = ['ping', shlex.quote(host)]
    try:
        subprocess.run(cmd, check=True)
        return 'Completed'
    except subprocess.CalledProcessError as e:
        return f'Failed: {str(e)}'

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)