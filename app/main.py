from fastapi import FastAPI
import subprocess
import shlex

class App:
    def __init__(self):
        self.app = FastAPI()
        self.app.add_route('/ping', self.ping)

    async def ping(self, host: str):
        sanitized_host = self.sanitize_input(host)
        try:
            command = ['ping', shlex.quote(sanitized_host)]
            result = await asyncio.subprocess.run(command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

    def sanitize_input(self, value):
        return ''.join(c if c.isalnum() or c in '-.' else '_' for c in value)

if __name__ == '__main__':
    app_instance = App()
    uvicorn.run(app_instance.app, host='0.0.0.0', port=8000)