from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isnumeric() and 1 <= int(host) <= 254:
        args = ['ping', f'192.168.0.{host}']
        subprocess.run(args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": subprocess.getoutput('ping 192.168.0.' + host)}
    else:
        return {"error": "Invalid host input"}