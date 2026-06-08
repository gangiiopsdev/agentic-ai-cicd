from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to prevent command injection
        if not host.isalnum():
            raise ValueError("Invalid host name")
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    except ValueError as ve:
        return {"error": str(ve)}