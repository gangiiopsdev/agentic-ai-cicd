from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __call__(self, host):
        try:
            if not self.is_safe_host(host):
                raise ValueError("Invalid host name")
            cmd = ['ping'] + shlex.split(host)
            output = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return {"status": "completed", "output": output.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    def is_safe_host(self, host):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
        for char in host:
            if char not in allowed_chars:
                return False
        return True
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping_instance = SafePing()
    return safe_ping_instance(host)