from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use subprocess.Popen instead of subprocess.call and avoid shell=True
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}

def validate_host(host: str) -> bool:
    # Basic validation of the host input to prevent injection
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts