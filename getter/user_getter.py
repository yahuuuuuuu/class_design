import sqlite3


def get_password(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT password FROM user WHERE user_id = ?;"

        cursor.execute(sql, (user_id,))

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



def get_name(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT name FROM user WHERE user_id = ?;"

        cursor.execute(sql, (user_id,))

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

def get_sex(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT sex FROM user WHERE user_id = ?;"

        cursor.execute(sql, (user_id,))

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


def get_background(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT background FROM user WHERE user_id = ?;"

        cursor.execute(sql, (user_id,))

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


def get_degree(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT degree FROM user WHERE user_id = ?;"

        cursor.execute(sql, (user_id,))

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


def get_is_editor(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT is_editor FROM user WHERE user_id = ?;"

        cursor.execute(sql, (user_id,))

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


def get_is_admin(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT is_admin FROM user WHERE user_id = ?;"

        cursor.execute(sql, (user_id,))

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