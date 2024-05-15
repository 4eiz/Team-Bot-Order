import aiosqlite



async def update_offers(text):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        insert_query = "UPDATE messages SET text=? WHERE id=1;"
        await db.execute(insert_query, (text,))
        await db.commit()

    except aiosqlite.Error as error:
        print("Не удалось изменить данные из таблицы.", error)
    finally:
        await db.close()


async def get_offers():
    db = await aiosqlite.connect('data/db/base.db')
    try:
        cursor = await db.execute("SELECT text FROM messages WHERE id=1;")
        text = await cursor.fetchone()  # Получаем все строки с помощью курсора
        return text[0]
    except aiosqlite.Error as error:
        print("Не удалось получить прокси-серверы из базы данных.", error)
    finally:
        await cursor.close()  # Закрываем курсор
        await db.close()  # Закрываем соединение
