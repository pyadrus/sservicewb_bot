from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def greeting_keyboards():
    """Клавиатуры поста приветствия 👋"""
    keyboards_greeting = InlineKeyboardMarkup()
    get_a_bonus = InlineKeyboardButton(text='Связь с оператором', url="https://t.me/lina545")
    # reference_keyboard = InlineKeyboardButton(text='📤 Вторая кнопка', callback_data='tv_key')
    keyboards_greeting.row(get_a_bonus)
    # keyboards_greeting.row(reference_keyboard)
    return keyboards_greeting


def subscription():
    """Кнопка подписки"""
    subscription_key = InlineKeyboardMarkup()
    sub_key = InlineKeyboardButton(text="Проверка подписки", callback_data="get_sub")
    subscription_key.row(sub_key)
    return subscription_key


if __name__ == '__main__':
    greeting_keyboards()
    subscription()
