from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils import exceptions

from keyboards.user_keyboards import greeting_keyboards
from messages.user_messages import greeting_post
from system.dispatcher import dp, CHANNEL_ID, bot


@dp.message_handler(Command('start'))
async def start(message: types.Message, state: FSMContext):
    """Обработчик команды запуска, также служащий в качестве приветственного сообщения"""
    await state.finish()
    await state.reset_state()

    # Проверьте, подписан ли пользователь на канал
    try:
        chat_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

        if chat_member.status in ('member', 'administrator'):
            # Пользователь подписан, отправить приветственное сообщение с клавиатуры
            keyboards_greeting = greeting_keyboards()
            await message.reply(greeting_post, reply_markup=keyboards_greeting, disable_web_page_preview=True,
                                parse_mode=types.ParseMode.HTML)
        else:
            text = ("👟 Пожалуйста, подпишитесь на канал @nike_reebok_adidas, чтобы связаться со службой поддержки. 👟\n\n"
                    "Далее вернитесь в бот и ещё раз нажмите /start. 🔄")
            # Пользователь не подписан, отправьте сообщение с просьбой подписаться
            await message.reply(text)

    except exceptions.TelegramAPIError:
        # Обработка ошибок API, если таковые имеются
        await message.reply("❗️ Произошла ошибка при проверке подписки. Попробуйте позже или свяжитесь с администратором бота. 🛠️")


@dp.callback_query_handler(text='get_sub')
async def get_password(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    # chat_id = callback_query.message.chat.id

    # Проверьте, подписан ли пользователь на канал
    try:
        chat_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)

        if chat_member.status in ('member', 'administrator'):
            greeting_post = "Для связи с оператором нажмите кнопку"
            keyboards_greeting = greeting_keyboards()
            await callback_query.message.reply(greeting_post, reply_markup=keyboards_greeting,
                                               disable_web_page_preview=True, parse_mode=types.ParseMode.HTML)
        else:
            text = ("👟 Пожалуйста, подпишитесь на канал @nike_reebok_adidas, чтобы связаться со службой поддержки. 👟\n\n"
                    "Далее вернитесь в бот и ещё раз нажмите /start. 🔄")
            await callback_query.message.reply(text)

    except exceptions.TelegramAPIError:
        await callback_query.message.reply("❗️ Произошла ошибка при проверке подписки. Попробуйте позже или свяжитесь с администратором бота. 🛠️")


def greeting_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(start)  # Обработчик команды /start, он же пост приветствия
    dp.register_message_handler(get_password)  # Обработчик команды /start, он же пост приветствия
