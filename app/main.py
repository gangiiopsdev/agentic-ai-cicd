from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize host input
    if not all(c.isalnum() or c in [".", "-"] for c in host):
        raise ValueError("Invalid hostname")

    app = FastAPI()

    @app.get="/ping")
    def ping(host: str):
        sanitized_host = subprocess.list2cmdline([host])
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}