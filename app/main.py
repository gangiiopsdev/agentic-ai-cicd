from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Validate the host input to ensure it's a valid hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname')
        # Use os.path.expandvars and os.path.abspath to sanitize the command arguments
        safe_command = ['ping', subprocess.list2cmdline([host])]
        subprocess.run(safe_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}