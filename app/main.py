from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Constructing the command safely without shell=True
        args = ['ping', host]
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