from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host to prevent shell injection
    if not all(c.isalnum() or c in '-_.@:/\' for c in host):
        return {'status': 'failed', 'error': 'Invalid host'}
    app = FastAPI()

    @app.get("/ping")
    def ping(host: str):
        try:
            output = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)