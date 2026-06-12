from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        if not all(c.isalnum() or c in [".", "-"] for c in host):  # Validate input
            raise ValueError('Invalid hostname')
        result = subprocess.run([quote('ping'), quote(host)], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}