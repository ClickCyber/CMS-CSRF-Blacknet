from flask import Flask

app = Flask('apps')
try:
    @app.route('/index.html')
    def wellcome():
        with open('file.txt', 'r') as file:
            return file.read()

    @app.route('/Scan.html')
    def scan_page():
        with open('scan.txt', 'r') as file:
            return file.read()



    app.run('127.0.0.1', port=80, debug=True)
except Exception as debugs:
    print(debugs)
