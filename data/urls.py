import aiosqlite



async def new_request(users_id):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        insert_query = '''INSERT INTO requests_urls (id)
                            VALUES (?);'''
        data_tuple = (users_id,)
        await db.execute(insert_query, data_tuple)
        await db.commit()
        print('Запись успешно добавлена.')

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQlite", error)
    finally:
        await db.close()


async def check_req_in_database(user_id):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        cursor = await db.execute("SELECT EXISTS(SELECT 1 FROM requests_urls WHERE id = ?);", (user_id,))
        result = await cursor.fetchone()
        return True if result[0] else False

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
        return "ошибка"
    finally:
        await db.close()
    

async def delete_req(user_id):
    db = await aiosqlite.connect('data/db/base.db')

    try:
        delete_query = "DELETE FROM requests_urls WHERE id=?;"
        await db.execute(delete_query, (user_id,))
        await db.commit()
        print(f"Записи для пользователя {user_id} успешно удалены.")

    except aiosqlite.Error as error:
        print("Не удалось выполнить запрос на удаление данных из таблицы.", error)
    
    finally:
        await db.close()