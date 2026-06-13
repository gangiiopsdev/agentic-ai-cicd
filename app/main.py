from fastapi import FastAPI
import subprocess
def is_safe_hostname(hostname):
    # Implement safe hostname checking logic here
    return all(c.isalnum() or c in ['-', '_'] for c in hostname)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if is_safe_hostname(host):
        try:
            output = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": output.stdout}
        except subprocess.CalledProcessError as e:
            return {"error": str(e)}
    else:
        return {"error": "Invalid hostname"}