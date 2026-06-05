from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate and sanitize the host input
        if not all(c.isalnum() or c in '.-' for c in host):
            raise ValueError('Invalid hostname')
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
    except ValueError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)