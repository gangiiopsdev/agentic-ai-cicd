from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    try:
        if '@' in host or ';' in host or '&&' in host or '|' in host or '>' in host or '<' in host or '`' in host or '&' in host:
            raise ValueError('Invalid input detected')
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}