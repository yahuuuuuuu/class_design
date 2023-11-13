import sqlite3

def get_name(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT name FROM journal WHERE id = ?;"

        cursor.execute(sql, (id,))

        result = cursor.fetchone()
        print(result)

        if result:
            return result[0]
        else:
            return None

    except sqlite3.Error as e:
        print(f"查询用户密码时出现错误:{e}")

        return None

    finally:
        if conn:
            conn.close()


def get_notice(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT notice FROM journal WHERE id = ?;"

        cursor.execute(sql, (id,))

        result = cursor.fetchone()
        print(result)

        if result:
            return result[0]
        else:
            return None

    except sqlite3.Error as e:
        print(f"查询用户密码时出现错误:{e}")

        return None

    finally:
        if conn:
            conn.close()


def get_introduce(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT introduce FROM journal WHERE id = ?;"

        cursor.execute(sql, (id,))

        result = cursor.fetchone()
        print(result)

        if result:
            return result[0]
        else:
            return None

    except sqlite3.Error as e:
        print(f"查询用户密码时出现错误:{e}")

        return None

    finally:
        if conn:
            conn.close()