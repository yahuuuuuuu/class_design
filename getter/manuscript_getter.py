import sqlite3

def get_name(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT name FROM manuscript WHERE id = ?;"

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


def get_user(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT user FROM manuscript WHERE id = ?;"

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



def get_author(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT author FROM manuscript WHERE id = ?;"

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


def get_status(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT status FROM manuscript WHERE id = ?;"

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


def get_abstract(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT abstract FROM manuscript WHERE id = ?;"

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


def get_unit(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT unit FROM manuscript WHERE id = ?;"

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


def get_keywords(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT keywords FROM manuscript WHERE id = ?;"

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


def get_root(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT root FROM manuscript WHERE id = ?;"

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

def get_direction(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        sql = "SELECT direction FROM manuscript WHERE id = ?;"

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


def get_manuscript_id(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        sql = "SELECT id FROM manuscript WHERE user = ?;"

        cursor.execute(sql, (user_id,))

        result = cursor.fetchall()

        if result:
            print(result)
            return result
        else:
            return None

    except sqlite3.Error as e:
        print(f"根据用户ID查询稿件ID时出错：{e}")
        return None

    finally:
        if conn:
            conn.close()

def get_manuscript_name(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        sql = "SELECT name FROM manuscript WHERE user = ?;"

        cursor.execute(sql, (user_id,))

        result = cursor.fetchall()

        if result:
            print(result)
            return result
        else:
            return None

    except sqlite3.Error as e:
        print(f"根据用户ID查询稿件名称时出错：{e}")
        return None

    finally:
        if conn:
            conn.close()

def get_manuscript_author(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        sql = "SELECT author FROM manuscript WHERE user = ?;"

        cursor.execute(sql, (user_id,))

        result = cursor.fetchall()

        if result:
            print(result)
            return result
        else:
            return None

    except sqlite3.Error as e:
        print(f"根据用户ID查询稿件作者时出错：{e}")
        return None

    finally:
        if conn:
            conn.close()


def get_manuscript_unit(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        sql = "SELECT unit FROM manuscript WHERE user = ?;"

        cursor.execute(sql, (user_id,))

        result = cursor.fetchall()

        if result:
            print(result)
            return result
        else:
            return None

    except sqlite3.Error as e:
        print(f"根据用户ID查询稿件作者单位时出错：{e}")
        return None

    finally:
        if conn:
            conn.close()

def get_manuscript_status(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        sql = "SELECT status FROM manuscript WHERE user = ?;"

        cursor.execute(sql, (user_id,))

        result = cursor.fetchall()

        if result:
            print(result)
            return result
        else:
            return None

    except sqlite3.Error as e:
        print(f"根据用户ID查询稿件作者单位时出错：{e}")
        return None

    finally:
        if conn:
            conn.close()



def get_manuscript_keywords(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        sql = "SELECT keywords FROM manuscript WHERE user = ?;"

        cursor.execute(sql, (user_id,))

        result = cursor.fetchall()

        if result:
            print(result)
            return result
        else:
            return None

    except sqlite3.Error as e:
        print(f"根据用户ID查询稿件关键词时出错：{e}")
        return None

    finally:
        if conn:
            conn.close()


def get_manuscript_direction(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        sql = "SELECT direction FROM manuscript WHERE user = ?;"

        cursor.execute(sql, (user_id,))

        result = cursor.fetchall()

        if result:
            print(result)
            return result
        else:
            return None

    except sqlite3.Error as e:
        print(f"根据用户ID查询稿件去向时出错：{e}")
        return None

    finally:
        if conn:
            conn.close()


def get_manuscript_abstract(user_id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        sql = "SELECT abstract FROM manuscript WHERE user = ?;"

        cursor.execute(sql, (user_id,))

        result = cursor.fetchall()

        if result:
            print(result)
            return result
        else:
            return None

    except sqlite3.Error as e:
        print(f"根据用户ID查询稿件去向时出错：{e}")
        return None

    finally:
        if conn:
            conn.close()