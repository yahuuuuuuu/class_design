import sqlite3

def new_user(user_id, password, sex, background, degree, is_editor=0, is_admin=0):
    try:
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        sql = "INSERT INTO user (user_id,password,sex,background,degree,is_editor,is_admin) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (user_id, password, sex, background, degree, is_editor, is_admin))
        conn.commit()

        return True
    except sqlite3.Error as e:
        print(f"新建用户时发生错误：{e}")
        return False

    finally:
        if conn:
            conn.close()



def new_manuscript(id,name,user,author,status,abstract,unit,keywords,direction):
    try:
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        sql = "INSERT INTO manuscript (id,name,user,author,status,abstract,unit,keywords,direction) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (id,name,user,author,status,abstract,unit,keywords,direction))
        conn.commit()

        return True
    except sqlite3.Error as e:
        print(f"新建文稿时发生错误：{e}")
        return False

    finally:
        if conn:
            conn.close()













