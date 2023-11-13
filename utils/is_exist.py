import sqlite3


def check_data_exists(table_name, column_name, data_to_check):
    try:
        # 连接到数据库
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        # 准备SQL查询语句
        query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = ?"
        cursor.execute(query, (data_to_check,))

        # 获取结果
        count = cursor.fetchone()[0]

        # 关闭数据库连接
        conn.close()

        # 如果 count 大于 0，表示数据存在
        return count > 0

    except sqlite3.Error as e:
        print("SQLite错误:", e)
        return False