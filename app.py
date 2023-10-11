# Flaskモジュールをインポート
from flask import Flask, render_template, request
import requests
import json

# Flaskオブジェクトの作成
app = Flask(__name__)

# ルート（/）にアクセスがあったときの処理
@app.route('/')
def index():
    return render_template('index.html')
 
# loginにアクセスがあったときの処理
@app.route('/login', methods=['POST'])
def login():
  name = request.form['name']
  phone = request.form['phone']
  
  payload = json.dumps({'name': name, 'phone': phone})
  
  response = requests.post("http://at-qatest01.internaladds.wingarc.com:8080/api/v1/t_teamb/login", data=payload)
  if response.status_code == 200:  # ステータスコードが200かどうかをチェック
      return render_template('profile.html')
  else:
      print(f"Error: {response.status_code}")  # エラーの場合はステータスコードを出力

# アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)
