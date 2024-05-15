import aiosqlite


async def new_user(users_id):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        insert_query = '''INSERT INTO users (id)
                            VALUES (?);'''
        data_tuple = (users_id,)
        await db.execute(insert_query, data_tuple)
        await db.commit()
        print('Запись успешно добавлена.')

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQlite", error)
    finally:
        await db.close()


async def check_worker_in_database(user_id):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        cursor = await db.execute("SELECT EXISTS(SELECT 1 FROM users WHERE id = ?);", (user_id,))
        result = await cursor.fetchone()
        return True if result[0] else False

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
        return "ошибка"
    finally:
        await db.close()


async def get_all_ids_from_db():
    async with aiosqlite.connect('data/db/base.db') as db:
        async with db.execute('SELECT id FROM users') as cursor:
            rows = await cursor.fetchall()
            return [row[0] for row in rows]
        

async def get_user(user_id):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        select_query = '''SELECT * FROM users WHERE id = ?;'''
        data_tuple = (user_id,)
        cursor = await db.execute(select_query, data_tuple)
        user_data = await cursor.fetchone()
        await cursor.close()
        if user_data:
            return user_data
        else:
            print('Пользователь с таким ID не найден.')

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
    finally:
        await db.close()


async def update_wallet(user_id, new_wallet_value):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        update_query = '''UPDATE users SET wallet = ? WHERE id = ?;'''
        data_tuple = (new_wallet_value, user_id)
        await db.execute(update_query, data_tuple)
        await db.commit()
        print('Значение кошелька успешно обновлено.')

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
    finally:
        await db.close()
