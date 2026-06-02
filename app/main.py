from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    args = ['ping', '-c', '1', host]  # Limit the number of pings to prevent excessive resource consumption
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

class FastAPIApp:
    def __init__(self):
        self.app = FastAPI()

    def add_routes(self):
        self.app.get("/")()(lambda: {"message": "Agentic Self-Healing Pipeline"})
        self.app.get("/ping")()(lambda host: safe_ping(host))

app_instance = FastAPIApp()
app = app_instance.app

def is_safe_host(host: str):
    # Implement logic to check if the host is safe
    return True