from fastapi import FastAPI
import subprocess
import shlex
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize input using regex
        host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
        args = shlex.split(f"ping {host}")
        subprocess.run(args, check=True)
        return {"status": "completed", "output": None}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "output": str(e)}