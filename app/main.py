from fastapi import FastAPI
import subprocess
class SecureSubprocess:
    @staticmethod
def ping(host: str):
        # Sanitize the host parameter to prevent command injection
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-'
        sanitized_host = ''.join(e for e in host if e in allowed_chars)
        try:
            result = subprocess.run(['ping', f'{sanitized_host}'], check=True, capture_output=True, text=True, shell=False)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}