from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize the host input
    allowed_hosts = ['example.com']
    if host in allowed_hosts:
        # Use shlex.quote to safely escape command arguments
        from shlex import quote
        subprocess.run(['ping', quote(host)], check=True, shell=False)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except Exception as e:
        return {"error": str(e)}