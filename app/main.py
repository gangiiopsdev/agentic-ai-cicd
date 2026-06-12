from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote
class SecureSubprocess:
    @staticmethod
def ping(host: str):
        # Sanitize the host parameter to only allow alphanumeric characters and specific symbols
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-'
        sanitized_host = ''.join(e for e in host if e in allowed_chars)
        try:
            result = subprocess.run(['ping', '-c', str(1), shell_quote(f'{sanitized_host}')], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}