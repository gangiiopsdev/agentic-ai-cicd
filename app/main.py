from fastapi import FastAPI
import subprocess
import socket
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit() or e.isspace())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        if not sanitized_host.isdigit():
            result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        else:
            raise ValueError("Invalid host")
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)