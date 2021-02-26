import json
from flask import Flask, render_template, request, redirect, url_for

#プロフィールを取得
def get_profile():
    # JSONファイルの読み込み
    file_json = "data/profile.json"
    prof = open(file_json, encoding='utf-8')
    json_str = prof.read()
    prof.close()

    # JSON（配列）から辞書型リストに変換
    prof_dict = json.loads(json_str)
    return prof_dict

#JSONファイルの更新
def update_profile(prof):
    f = open('data/profile.json', 'w')
    json.dump(prof, f)
    f.close()

#Flaskのインスタンスを作成
app = Flask(__name__)

#データ一覧画面へリダイレクト
@app.route('/')
def root():
    return redirect(url_for("profile"))

#データ一覧画面
@app.route('/profile')
def profile():
    prof_dict = get_profile()
    return render_template('profile.html', title='json', users=prof_dict)

#データ編集画面
@app.route('/edit/<int:id>')
def edit(id):
    prof_dict = get_profile()
    user_dict = ""
    for data in prof_dict:
        if data['id'] == id:
            user_dict = data
    return render_template('edit.html', title='json', user=user_dict)

#データ更新処理
@app.route('/update', methods=['POST'])
def update():
    #POSTで送信されたデータを受け取り、変数に格納
    id_str = request.form['id']
    name   = request.form['name']
    age    = request.form['age']
    sex    = request.form['sex']

    #データを更新してJSONファイルを上書き
    prof_dict_before = get_profile()
    prof_dict_after = []

    for data in prof_dict_before:
        if str(data['id']) == id_str:
            prof_dict_after.append({"id":int(id_str), "name":name, "age":age, "sex":sex})
        else:
            prof_dict_after.append(data)
    
    update_profile(prof_dict_after)

    #データを更新したら/profile画面に戻る（リダイレクト）
    return redirect(url_for("profile"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
