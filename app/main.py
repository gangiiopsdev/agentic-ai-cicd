from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Validate and sanitize host input
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid hostname')
    try:
        args = ['ping', '-c', '1', host]  # Limit the number of pings to avoid denial-of-service
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class FastAPIApp:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    def ping(self, host: str):
        return safe_ping(host)

# Create and run the app
app_instance = FastAPIApp().app