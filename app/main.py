from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Preventive Controls:
# 1. Validate the input to ensure it only contains allowed characters.
# 2. Use a whitelist of allowed hostnames or IP addresses.
# 3. Log and monitor all ping requests for anomaly detection.