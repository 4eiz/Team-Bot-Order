from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram import types
from config import CHANNEL_URL, CHAT_URL, link_instr, P_V

class Menu_callback(CallbackData, prefix="menu"):
    menu: str


class Answer_callback(CallbackData, prefix="answer"):
    answer: str
    user_id: int


def worker_menu():
    kb = [
        [
            types.InlineKeyboardButton(text='📖 Ознакомление', callback_data=Menu_callback(menu="familiarization").pack()),
            types.InlineKeyboardButton(text='🫦 Актуальное', callback_data=Menu_callback(menu="offers").pack()),
        ],
        [
            types.InlineKeyboardButton(text='📚 Инструкции', callback_data=Menu_callback(menu="manuals").pack()),
            types.InlineKeyboardButton(text='👨‍💻 Для работы', callback_data=Menu_callback(menu="for_work").pack()),
        ],
        [
            types.InlineKeyboardButton(text='🙋‍♂️ Филиалы', callback_data=Menu_callback(menu="branches").pack()),
            types.InlineKeyboardButton(text='💸 Выплаты', callback_data=Menu_callback(menu="payments").pack()),
        ],
        [
            types.InlineKeyboardButton(text='💼 Кабинет', callback_data=Menu_callback(menu="profil").pack()),
        ],
        [
            types.InlineKeyboardButton(text='⚙️ Поддержка', callback_data=Menu_callback(menu="support").pack()),
        ],
    ]
    
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def worker_menu_admin():
    kb = [
        [
            types.InlineKeyboardButton(text='📖 Ознакомление', callback_data=Menu_callback(menu="familiarization").pack()),
            types.InlineKeyboardButton(text='🫦 Актуальное', callback_data=Menu_callback(menu="offers").pack()),
        ],
        [
            types.InlineKeyboardButton(text='📚 Инструкции', callback_data=Menu_callback(menu="manuals").pack()),
            types.InlineKeyboardButton(text='👨‍💻 Для работы', callback_data=Menu_callback(menu="for_work").pack()),
        ],
        [
            types.InlineKeyboardButton(text='🙋‍♂️ Филиалы', callback_data=Menu_callback(menu="branches").pack()),
            types.InlineKeyboardButton(text='💸 Выплаты', callback_data=Menu_callback(menu="payments").pack()),
        ],
        [
            types.InlineKeyboardButton(text='💼 Кабинет', callback_data=Menu_callback(menu="profil").pack()),
        ],
        [
            types.InlineKeyboardButton(text='⚙️ Поддержка', callback_data=Menu_callback(menu="support").pack()),
        ],
        [
            types.InlineKeyboardButton(text='💎 Админ панель', callback_data=Menu_callback(menu="admin_menu").pack()),
        ]
    ]
    
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def familiarization():
    kb = [
        [
            types.InlineKeyboardButton(text='📰 Новости', url=CHANNEL_URL),
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack())
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def fillial_kb(url):
    kb = [
        [
            types.InlineKeyboardButton(text='🙋‍♂️ Чат', url=url),
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack())
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def instructions():
    kb = [
        [
            types.InlineKeyboardButton(text='Инструкции', url=link_instr),
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack())
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def send_request():
    kb = [
        [
            types.InlineKeyboardButton(text='Заполнить анкету', callback_data=Menu_callback(menu="request").pack())
        ],
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def confirm():
    kb = [
        [
            types.InlineKeyboardButton(text='Отправить', callback_data=Menu_callback(menu="send_request").pack())
        ],
        [
            types.InlineKeyboardButton(text='Заполнить заявку еще раз', callback_data=Menu_callback(menu="request").pack())
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def materials():
    kb = [
        [
            types.InlineKeyboardButton(text='Запрос ссылки', callback_data=Menu_callback(menu="url_req").pack())
        ],
        [
            types.InlineKeyboardButton(text='Фото и видео', url=P_V)
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack())
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def cancel():
    kb = [
        [
            types.KeyboardButton(text='Отмена')
        ]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def admin_conf(user_id):
    kb = [
        [
            types.InlineKeyboardButton(text='Принять', callback_data=Answer_callback(answer="accept", user_id=user_id).pack())
        ],
        [
            types.InlineKeyboardButton(text='Отклонить', callback_data=Answer_callback(answer="decline", user_id=user_id).pack())
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def accept():
    kb = [
        [
            types.InlineKeyboardButton(text='Принято', callback_data=Menu_callback(menu="accepted").pack())
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def decline():
    kb = [
        [
            types.InlineKeyboardButton(text='Отклонено', callback_data=Menu_callback(menu="declined").pack())
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def menu():
    kb = [
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack())
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def profil_True():
    kb = [
        [
            types.InlineKeyboardButton(text='💳 Изменить кошелёк', callback_data=Menu_callback(menu="wallet").pack())
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack())
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def profil_False():
    kb = [
        [
            types.InlineKeyboardButton(text='💳 Привязать кошелёк', callback_data=Menu_callback(menu="wallet").pack())
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack())
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def admin_panel():
    kb = [
        [
            types.InlineKeyboardButton(text='Изменить актуальное', callback_data=Menu_callback(menu="change_offers").pack())
        ],
        [
            types.InlineKeyboardButton(text='Рассылка', callback_data=Menu_callback(menu="newsletter").pack())
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack())
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def offers_cancel():
    kb = [
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="admin_menu").pack())
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def send_req_branches():
    kb = [
        [
            types.InlineKeyboardButton(text='Подать заявку', callback_data=Menu_callback(menu="send_req_branches").pack())
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data=Menu_callback(menu="menu").pack())
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def admin_conf_branches(user_id):
    kb = [
        [
            types.InlineKeyboardButton(text='Принять', callback_data=Answer_callback(answer="accept_branches", user_id=user_id).pack())
        ],
        [
            types.InlineKeyboardButton(text='Отклонить', callback_data=Answer_callback(answer="decline_branches", user_id=user_id).pack())
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def url_chat(channel):
    kb = [
        [
            types.InlineKeyboardButton(text='Чат', url=channel),
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def send_req_urls():
    kb = [
        [
            types.InlineKeyboardButton(text='Подать заявку', callback_data=Menu_callback(menu="send_req_urls").pack())
        ],
        [
            types.InlineKeyboardButton(text='Отмена', callback_data=Menu_callback(menu="menu").pack())
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def admin_conf_urls(user_id):
    kb = [
        [
            types.InlineKeyboardButton(text='Принять', callback_data=Answer_callback(answer="accept_urls", user_id=user_id).pack())
        ],
        [
            types.InlineKeyboardButton(text='Отклонить', callback_data=Answer_callback(answer="decline_urls", user_id=user_id).pack())
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)