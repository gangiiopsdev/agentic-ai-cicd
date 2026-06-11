from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Use a whitelist of allowed hosts or IP ranges
        if host in ['example.com', '192.168.1.1']:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        else:
            raise ValueError('Invalid host')
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}