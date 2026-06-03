from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def run(host):
        # Sanitize input to prevent command injection
        host = subprocess.list2cmdline([host])
        try:
            result = subprocess.run(['ping', '--', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it's a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid host"}
    return SafePing.run(host)