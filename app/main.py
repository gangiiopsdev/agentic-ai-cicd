from fastapi import FastAPI
import subprocess
class SecureSubprocess:
    @staticmethod
def ping(host: str):
        # Use a whitelist of allowed hosts or validate the input more strictly
        if not any(char in host for char in [' ', '	', '
', '', ';', '&', '|', '(', ')', '<', '>', '*', '?', '[', ']', '{', '}', '\\']):
            try:
                result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
                return {"status": "completed", "output": result.stdout}
            except subprocess.CalledProcessError as e:
                return {"status": "failed", "error": e.stderr}
        else:
            return {"status": "invalid", "message": "Invalid host parameter"}