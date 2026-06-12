from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout
class MainApp:
    def __init__(self):
        self.app = FastAPI()

    @app.get('/ping')
    async def ping(self, host: str):
        try:
            response = execute_ping(host)
            return {'status': 'completed', 'response': response}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

if __name__ == '__main__':
    main_app = MainApp()
    app = main_app.app