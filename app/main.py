from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping_host(host: str):
    try:
        # Validate the host to ensure it's a valid IP address or hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError("Invalid host")
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except (subprocess.CalledProcessError, ValueError) as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return await ping_host(host)