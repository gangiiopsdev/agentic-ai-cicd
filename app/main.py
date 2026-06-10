from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    if validate_host(host):\n        args = ['ping', '-c', '1', host]\n        try:\n            subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n            return {"status": "completed"}\n        except subprocess.CalledProcessError as e:\n            return {"error": f"Ping failed: {e.stderr.decode('utf-8')}"}\n    else:\n        return {"error": "Invalid host"}