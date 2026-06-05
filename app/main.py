from fastapi import FastAPI
import subprocess
import socket
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit() or e.isspace())

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    sanitized_host = sanitize_input(host)\n    try:\n        if not sanitized_host.isdigit() and socket.gethostbyname_ex(sanitized_host)[2]:\n            result = subprocess.run(["ping", sanitized_host], capture_output=True, text=True, check=True)\n            return {"status": "completed", "output": result.stdout}\n        else:\n            raise ValueError("Invalid host")\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": str(e)}
if __name__ == '__main__':\n    import uvicorn\n    uvicorn.run(app, host='127.0.0.1', port=8000)