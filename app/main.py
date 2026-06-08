from fastapi import FastAPI
import subprocess
import shlex
class SanitizedHost:
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    @staticmethod
def sanitize_host(host):
        return host if host in SanitizedHost.allowed_hosts else '127.0.0.1'
class PingEndpoint:
    @staticmethod
def ping(sanitized_host: str):
        result = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    sanitized_host = SanitizedHost.sanitize_host(host)
    return PingEndpoint.ping(sanitized_host)