from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    if request.headers.get('X-GitHub-Event') == 'push':
        subprocess.run(['git', 'pull'])
        subprocess.run(['docker', 'stop', 'mein-nginx'])
        subprocess.run(['docker', 'rm', 'mein-nginx'])
        subprocess.run(['docker', 'run', '-d', '--name', 'mein-nginx', '-p', '80:80', 'mein-nginx'])
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
