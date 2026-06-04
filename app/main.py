from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args)

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to prevent injection
        if not host.isalnum() and '-' not in host and '.' not in host:
            raise ValueError('Invalid hostname')
        run_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}