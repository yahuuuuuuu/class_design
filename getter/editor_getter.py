import sqlite3


def get_charge(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT charge FROM editor WHERE id = ?;"

        cursor.execute(sql, (id,))

        result = cursor.fetchone()
        print(result)

        if result:
            return result
        else:
            return None

    except sqlite3.Error as e:
        print(f"查询用户密码时出现错误:{e}")

        return None

    finally:
        if conn:
            conn.close()