from fastapi import FastAPI
import subprocess
class SecureSubprocess:
    @staticmethod
def ping(host: str):
        sanitized_host = ''.join(e for e in host if e.isalnum() or e in '._-')
        try:
            result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}