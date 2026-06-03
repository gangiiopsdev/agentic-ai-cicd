from fastapi import FastAPI
import subprocess
class SafeHostEscape:
    def escape(self, host):
        return ''.join(char for char in host if char.isalnum() or char in '._-')

app = FastAPI()
safe_host_escape = SafeHostEscape()

@app.get("/ping")
def ping(host: str):
    safe_host = safe_host_escape.escape(host)
    # Secure implementation
    subprocess.run(['ping', f'-c 1 {safe_host}'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}