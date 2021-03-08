from flask import Flask, render_template, request, redirect, url_for
# sqliteをPythonから実行するためのモジュール
import sqlite3

app = Flask(__name__)

# sqliteからデータを取り出す関数
def get_profile():
    conn = sqlite3.connect('profile.sqlite3')
    c = conn.cursor()
    prof_list = []
    for i in c.execute('select * from persons'):
        prof_list.append({'id':i[0], 'name':i[1], 'age':i[2], 'sex':i[3]})
    conn.commit()
    conn.close()
    return prof_list

print(0)
# sqliteのテーブルを更新する関数
def update_profile(prof):
    conn = sqlite3.connect('profile.sqlite3')
    c = conn.cursor()
    c.execute("update persons set name='{0}', age={1}, sex='{2}' where id={3}".format(prof['name'], prof['age'], prof['sex'], prof['id']))
    conn.commit()
    conn.close()

print(1)
@app.route('/profile')
def profile():
    prof_dict = get_profile()
    return render_template('profile.html', title='sql', user=prof_dict)

print(2)
@app.route('/edit/<int:id>')
def edit(id):
    prof_list = get_profile()
    prof_dict = prof_list[id-1]
    print(2222)
    return render_template('edit.html', title='sql', user=prof_dict)

print(3)
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    prof_list = get_profile()
    prof_dict = prof_list[id-1]
    # prof_dict　の値を変更
    prof_dict['name'] = request.form['name']
    prof_dict['age'] = request.form['age']
    prof_dict['sex'] = request.form['sex']
    update_profile(prof_dict)
    return redirect(url_for('profile'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
