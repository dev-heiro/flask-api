from flask import Flask
app = Flask(__name__)

@app.route('/')
def health_check():
    return { "message" : "ok"}

if __name__ == '__main__':
    app.run()