import sqlite3


path_to_db= 'data/main.db'

def create_table():
    conn = sqlite3.connect('data/main.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
            chat_id INTEGER NOT NULL,
            full_name TEXT,
            username TEXT,
            language VARCHAR(3) NOT NULL DEFAULT uz,
            dushanba TEXT,
            seshanba integer,
            chorshanba TEXT,
            payshanba TEXT,
            juma TEXT,
            shanba TEXT
        )""")
    
    conn.commit()
    conn.close()
    

def add_user(user_id, full_name, username = None, language = 'uz'):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE chat_id = '{user_id}'")
    if not c.fetchone():
        new_data = (user_id, full_name, username, language)
        c.execute(f"INSERT INTO users(chat_id, full_name, username, language) VALUES (?,?,?,?)", new_data)
        conn.commit()
    conn.close()


def get_lessons(chat_id, day_name):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"SELECT {day_name} FROM users WHERE chat_id = '{chat_id}'")
    lessons= c.fetchone()[0]
    return lessons
    
def add_lessons(chat_id, day_name, lessons):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    sql_update_query = f"""UPDATE users SET {day_name} = ? WHERE chat_id = ?"""
    data = (lessons, chat_id)
    c.execute(sql_update_query, data)
    conn.commit()
    conn.close()
    

# ADMIN
def count_users():
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"SELECT COUNT() FROM users")
    count = c.fetchone()[0]
    return count


def get_users_id():
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"SELECT chat_id FROM users")
    sender_id = c.fetchall()
    return sender_id