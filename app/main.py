from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        # Use a safe and secure way to execute the ping command
        output = subprocess.check_output(['ping', host], universal_newlines=True, shell=False)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

class AppFastAPI(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_middleware(
            SecurityMiddleware,
            force_https=True,
            hsts_max_age_seconds=31536000,
            include_subdomains=True,
        )

app = AppFastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        raise HTTPException(status_code=400, detail="Invalid host input")
    return run_ping(host)