from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Enhanced input validation and sanitization
        if not host.isalnum() or len(host) > 100 or not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.' for c in host):  # Ensure only alphanumeric and '.' characters are allowed
            raise ValueError("Invalid host")
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}
    except ValueError as ve:
        return {"status": "error", "error": str(ve)}