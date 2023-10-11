# Flaskモジュールをインポート
from flask import Flask

# Flaskオブジェクトの作成
app = Flask(__name__)

# ルート（/）にアクセスがあったときの処理
@app.route('/')
def hello_world():
    return 'Hello, World!'

# アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)
