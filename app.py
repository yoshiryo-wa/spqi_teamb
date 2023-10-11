# Flaskモジュールをインポート
from flask import Flask, render_template, request
import requests
import json

# Flaskオブジェクトの作成
app = Flask(__name__)

# ルート（/）にアクセスがあったときの処理
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
 
# loginにアクセスがあったときの処理
@app.route('/login', methods=['POST'])
def login():
  name = request.form['name']
  phone = request.form['phone']
  
  payload = ({'name': name, 'phone': phone})
  headers = {'Content-Type': 'application/json'}
  
  response = requests.post("http://at-qatest01.internaladds.wingarc.com:8080/api/v1/t_teamb/login", json=payload, headers=headers)
  data = response.json()
  if data.get("result"): # 'result'がtrueであれば
      return render_template('profile.html', data=data)
  else:
      print(f"Error: {response.status_code}")  # エラーの場合はステータスコードを出力

# アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)
