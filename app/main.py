from fastapi import FastAPI
import subprocess
import shlex

global_config = {
    'allowed_hosts': ['example.com']
}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in global_config['allowed_hosts']:
        raise HTTPException(status_code=403, detail="Access denied")
    command = ["ping", host]
    subprocess.run(command, check=True)
    return {"status": "completed"}