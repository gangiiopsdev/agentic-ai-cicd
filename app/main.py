from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.strip().isalnum():
        raise ValueError("Invalid hostname")
    return host

@app.get("/ping")
def ping(host: str):
    try:
        validated_host = validate_host(host)
        args = ['ping', validated_host]
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Ping failed with error code {e.returncode}")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {str(e)}")

    return {"status": "completed"}