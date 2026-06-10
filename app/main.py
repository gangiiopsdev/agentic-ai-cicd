from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use ping3 library for safer and more secure pinging
    from ping3 import ping, verbose_ping
    try:
        response = ping(host)
        if response is not None:
            return True
        else:
            return False
    except Exception as e:
        return False

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the input to prevent injection attacks
        if not host.isalnum() or len(host) > 255:
            raise ValueError("Invalid host name")
        if safe_ping(host):
            return {"status": "completed"}
        else:
            return {"status": "failed", "error": "Ping failed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}