from fastapi import FastAPI
import subprocess

def execute_ping(host):
    # Safe implementation using list instead of string for subprocess.call
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

class FastAPIApp:
    def __init__(self):
        self.app = FastAPI()

    @app.get="/"
    def home(self):
        return {"message": "Agentic Self-Healing Pipeline"}

    @app.get="/ping"
    def ping(self, host: str):
        # Validate and sanitize the input
        if not host.isalnum() or len(host) > 255:
            raise ValueError("Invalid host name")
        return execute_ping(host)

app = FastAPIApp().app