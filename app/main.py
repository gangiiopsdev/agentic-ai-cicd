from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if host and all(c.isalnum() or c in ('.', '-', '_') for c in host):
        safe_host = subprocess.list2cmdline([host])  # Use list2cmdline to escape shell special characters
        try:
            subprocess.run(['ping', '-c', '4', safe_host], check=True)  # Specify number of pings
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}
    else:
        raise ValueError('Invalid host name')

    return {"status": "completed"}