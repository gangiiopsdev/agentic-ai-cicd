from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid input for host")
app = FastAPI()
@app.get('/ping_fixed')
def ping_fixed(host: str):
    try:
        if not host.isalnum() or len(host) > 64:
            raise ValueError("Invalid input for host")
        args = ["ping", host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"error": str(e)}