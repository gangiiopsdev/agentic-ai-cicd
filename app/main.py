from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.Popen safely
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=403, detail="Invalid host")
    output = safe_ping(host)
    return {"status": "completed", "output": output}
def is_safe_host(host: str) -> bool:
    allowed_hosts = ["example.com", "test.com"]  # Add your allowed hosts here
    return host in allowed_hosts