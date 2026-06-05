from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the input to ensure it is a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {"error": "Invalid input"}, 400
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500