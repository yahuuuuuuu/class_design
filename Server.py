import sqlite3

from flask import Flask,render_template,jsonify, request, send_file
from flask_admin.contrib import sqla
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from getter import user_getter
from utils import is_exist,setter
import uuid
import os
from flask_basicauth import BasicAuth



app = Flask(__name__, static_folder='statics', template_folder='templates')
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/xusihang/PycharmProjects/keshe/mydatabase.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
basic_auth = BasicAuth(app)



class ModelView(sqla.ModelView):
    column_display_pk = True
    can_set_page_size = True
    can_export = True

class UserModelView(ModelView):
    column_display_pk = True
    column_filters = ("user_id", "password", "sex", "background", "degree", "is_editor", "is_admin")
    form_columns = ("user_id", "password", "sex", "background", "degree", "is_editor", "is_admin")

class EditorModelView(ModelView):
    column_display_pk = True
    column_filters = ("id", "charge")
    form_columns = ("id", "charge")

class JournalModelView(ModelView):
    column_display_pk = True
    column_filters = ("name", "notice", "introduce")
    form_columns = ("name", "notice", "introduce")


class ManuscriptModelView(ModelView):
    column_display_pk = True
    column_filters = ("id", "name", "user", "author", "status", "abstract", "unit", "keywords", "direction")
    form_columns = ("id", "name", "user", "author", "status", "abstract", "unit", "keywords", "direction")

class Editor(db.Model):
    __tablename__ = 'editor'
    id = db.Column(db.TEXT, primary_key=True)
    charge = db.Column(db.TEXT)

class Journal(db.Model):
    __tablename__ = 'journal'
    name = db.Column(db.TEXT, primary_key=True)
    notice = db.Column(db.Text)
    introduce = db.Column(db.Text)

class Manuscript(db.Model):
    __tablename__ = 'manuscript'
    id = db.Column(db.TEXT, primary_key=True)
    name = db.Column(db.TEXT)
    user = db.Column(db.TEXT)  # Assuming user is a string, you might want to use a foreign key relationship
    author = db.Column(db.TEXT)
    status = db.Column(db.TEXT)
    abstract = db.Column(db.Text)
    unit = db.Column(db.TEXT)
    keywords = db.Column(db.TEXT)
    direction = db.Column(db.TEXT)

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.TEXT, primary_key=True)
    password = db.Column(db.TEXT)
    sex = db.Column(db.TEXT)
    background = db.Column(db.TEXT)
    degree = db.Column(db.TEXT)
    is_editor = db.Column(db.Integer)
    is_admin = db.Column(db.Integer)

# 创建所有模型
with app.app_context():
    db.create_all()
# 创建管理员界面
admin = Admin(app, name='My Admin', template_mode='bootstrap3')


# 添加模型到管理员界面
admin.add_view(EditorModelView(Editor, db.session))
admin.add_view(JournalModelView(Journal, db.session))
admin.add_view(ManuscriptModelView(Manuscript, db.session))
admin.add_view(UserModelView(User, db.session))



@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signup')
def sign_up_page():
    return render_template('sign_up.html')

@app.route('/forget_pw')
def forget_pw():
    return render_template('forget_password.html')


@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/check_id_pw', methods=['POST'])
def check_id_pw():
    data = request.get_json()
    user_id = data['user_id']
    password = data['password']
    true_password = user_getter.get_password(user_id)
    if(password == true_password):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

@app.route('/sign_up', methods=['POST'])
def sign_up():
    #JSON.stringify({user_id: input_id, password: input_password, sex: sex, background: background, degree:degree, name: name})
    data = request.get_json()
    user_id = data['user_id']
    password = data['password']
    sex = data['sex']
    background = data['background']
    degree = data['degree']
    if(is_exist.check_data_exists(table_name='user', column_name='user_id', data_to_check=user_id)):
        return jsonify({'success': False})
    else:
        setter.new_user(user_id=user_id, password=password, sex=sex, background=background, degree=degree)
        return jsonify({'success': True})


@app.route('/mydoc')
def mydoc():
    return render_template('mydoc.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/qikan')
def qikan():
    return render_template('journal.html')

@app.route('/shengao')
def shengao():
    return render_template('shengao.html')

@app.route('/yonghu')
def yonghu():
    return render_template('yonghu.html')



@app.route('/upload_doc',methods=['POST'])
def upload_doc():
    data = request.form
    title = data['title']
    author = data['author']
    unit = data['unit']
    keywords = data['keywords']
    abstract = data['abstract']
    file = request.files['file']
    doc_id = str(uuid.uuid4())
    status = '未投稿'
    direction = '无'
    user = data['userId']
    save_root = os.path.join('upload_data', doc_id)
    os.makedirs(save_root, exist_ok=True)
    setter.new_manuscript(id=doc_id, name=title, user=user, author=author, status=status, abstract=abstract, unit=unit, keywords=keywords, direction=direction)
    file.save(save_root+ '/' + file.filename)
    return jsonify({'success': True})



@app.route('/get_user_docs/<user_id>')
def get_user_docs(user_id):
    # 在这里执行查询数据库的操作，获取用户的所有稿件信息
    # 假设您有一个名为 "db" 的SQLite数据库连接
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # 执行查询
    cursor.execute("SELECT name, author, unit, direction, status, abstract, keywords, id FROM manuscript WHERE user = ?", (user_id,))
    rows = cursor.fetchall()

    # 将查询结果转换为字典形式
    docs = []
    for row in rows:
        doc = {
            'title': row[0],
            'author': row[1],
            'unit': row[2],
            'destination': row[3],
            'status': row[4],
            'abstract': row[5],
            'keywords': row[6],
            'id': row[7]
        }
        docs.append(doc)

    conn.close()

    return jsonify(docs)



@app.route('/delete_document', methods=['POST'])
def delete_document():
    try:
        data = request.get_json()
        id_to_delete = data.get('id')

        # 连接到数据库
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        # 删除 manscript 表中的对应行
        cursor.execute("DELETE FROM manuscript WHERE id = ?", (id_to_delete,))
        conn.commit()

        conn.close()

        return jsonify({'message': 'Document deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_journal_data', methods=['GET'])
def get_journal_data():

    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, notice, introduce FROM journal")
    rows = cursor.fetchall()
    journal_data = [{'name': row[0], 'notice': row[1], 'introduction': row[2]} for row in rows]

    conn.close()

    return jsonify(journal_data)


@app.route('/get_manuscripts/<user_id>', methods=['GET'])
def get_manuscripts(user_id):
    try:
        # 连接到数据库
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        # 查询 manuscript 表中与给定 user_id 匹配的数据
        cursor.execute("SELECT id, name FROM manuscript WHERE user = ?", (user_id,))
        rows = cursor.fetchall()

        # 将查询结果转换为字典列表
        manuscripts_data = [{'id': row[0], 'name': row[1]} for row in rows]

        conn.close()

        return jsonify(manuscripts_data)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/get_shengao/<user_id>', methods=['GET'])
def get_shengao(user_id):
    try:
        # 连接到数据库
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        # 查询 manuscript 表中与给定 user_id 匹配的数据
        cursor.execute("SELECT id, name, author FROM manuscript WHERE direction = (SELECT charge from editor WHERE id = ?)", (user_id,))
        rows = cursor.fetchall()

        # 将查询结果转换为字典列表
        manuscripts_data = [{'id': row[0], 'name': row[1], 'author': row[2]} for row in rows]

        conn.close()
        return jsonify(manuscripts_data)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/update_manuscript', methods=['POST'])
def update_manuscript():
    try:
        data = request.get_json()

        selected_journal = data['selected_journal']
        selected_manu = data['selected_manu']

        # 连接到数据库
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        # 更新数据库中的记录
        cursor.execute("UPDATE manuscript SET direction = ? WHERE id = ?", (selected_journal, selected_manu))
        cursor.execute("UPDATE manuscript SET status = '审稿中' WHERE id = ?", (selected_manu,))
        conn.commit()
        conn.close()

        return jsonify({'message': '更新成功'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/downloaddoc', methods=['POST'])
def downloaddoc():
    data = request.get_json()
    docID = data['docID']
    for i in os.listdir(os.path.join('upload_data', docID)):
        file = i
    path = os.path.join('upload_data', docID, file)
    return send_file(path)

@app.route('/access', methods=['POST'])
def access():
    data = request.get_json()
    docID = data['docID']
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE manuscript SET status = ? WHERE id = ?", ('已接收', docID))
    conn.commit()
    conn.close()
    return jsonify({'message': '更新成功'})


@app.route('/reject', methods=['POST'])
def reject():
    data = request.get_json()
    docID = data['docID']
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE manuscript SET status = ? WHERE id = ?", ('已拒稿', docID))
    conn.commit()
    conn.close()
    return jsonify({'message': '更新成功'})

@app.route('/get_userinfo/<user_id>', methods=['GET'])
def get_userinfo(user_id):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password, sex, background, degree from user where user_id = ?", (user_id,))
    result = cursor.fetchone()
    password = result[0]
    sex = result[1]
    background = result[2]
    degree = result[3]
    return jsonify({'password':password, 'sex':sex, 'background':background, 'degree':degree})


@app.route('/update_user', methods=['POST'])
def update_info(): #xhr.send(JSON.stringify({user_id: userId, degree: newDegree, background: newBackground, sex: newSex, password: newPassword}))
    data = request.get_json()
    user_id = data['user_id']
    degree = data['degree']
    background = data['background']
    sex = data['sex']
    password = data['password']
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET degree=?, background=?, sex=?, password=? WHERE user_id=?", (degree, background, sex, password, user_id))
    conn.commit()
    conn.close()
    return jsonify({'message': '更新成功'})



if __name__ == '__main__':
    app.run(host='127.0.0.6', debug=True, port=5895)