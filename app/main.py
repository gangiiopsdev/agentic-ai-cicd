from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host to ensure it's safe
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}

    app = FastAPI()

    @app.get("/ping")
    def ping(host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', f'"{host}"'], timeout=5, shell=False)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

    return app