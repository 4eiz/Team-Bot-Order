import aiosqlite


async def new_fillial(user_id, url):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        insert_query = '''INSERT INTO fillials (id, url)
                            VALUES (?, ?);'''
        data_tuple = (user_id, url)
        await db.execute(insert_query, data_tuple)
        await db.commit()
        print('Запись успешно добавлена.')

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQlite", error)
    finally:
        await db.close()


async def get_fillial_info(user_id):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        select_query = '''SELECT * FROM fillials WHERE id = ?;'''
        data_tuple = (user_id,)
        cursor = await db.execute(select_query, data_tuple)
        user_data = await cursor.fetchone()
        await cursor.close()
        if user_data:
            return user_data  # Возвращает данные пользователя в виде кортежа
        else:
            return
    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
        return 'Ошибка при запросе данных.'

    finally:
        await db.close()
