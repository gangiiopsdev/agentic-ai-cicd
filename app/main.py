from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to prevent injection attacks
        if not all(c.isalnum() or c in '.-\/' for c in host):
            raise ValueError("Invalid input")
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}