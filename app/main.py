from fastapi import FastAPI
import subprocess
import shlex
class SecureSubprocess:
    @staticmethod
def ping(host: str):
        sanitized_host = shlex.quote(host)
        try:
            result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}