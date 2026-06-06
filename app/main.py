from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.Popen instead of shell=True for security
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

class SafePingApp(FastAPI):
    @app.get("/ping")
    def ping(host: str):
        return safe_ping(host)

app = SafePingApp()