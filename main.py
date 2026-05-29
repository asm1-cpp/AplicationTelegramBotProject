import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

TOKEN = "8940162665:AAGgo9n8Rxjwpor57gruuU4DvK9KO8IwScc"
ADMIN_ID = 6840631785

dp = Dispatcher()
bot = Bot(token=TOKEN)

logging.basicConfig(level=logging.INFO)


class OrderForm(StatesGroup):
    waiting_for_item = State()
    waiting_for_count = State()
    waiting_for_type = State()


def get_inline_buttons1():
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(text="💬 Info", callback_data="info"),
        types.InlineKeyboardButton(text="💻 Catalog", callback_data="catalog"),
        types.InlineKeyboardButton(text="📝 Order Service", callback_data="application"),
    )
    builder.adjust(2, 1)
    return builder.as_markup()


def get_inline_buttons2():
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(text="Custom Bot Development", callback_data="bot_app"),
        types.InlineKeyboardButton(text="OS Optimization", callback_data="system_opt"),
        types.InlineKeyboardButton(text="Deploy Bot/Script", callback_data="run_script"),
        types.InlineKeyboardButton(text="⬅️ Back to Menu", callback_data="start_b"),
    )
    builder.adjust(1)
    return builder.as_markup()


def get_inline_buttons3():
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(text="Windows 11", callback_data="win_11"),
        types.InlineKeyboardButton(text="Windows 10", callback_data="win_10"),
        types.InlineKeyboardButton(text="Linux", callback_data="linux"),
        types.InlineKeyboardButton(text="⬅️ Back to Services", callback_data="application"),
    )
    builder.adjust(2, 2)
    return builder.as_markup()


def get_inline_buttons4():
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(text="📝 Order Service", callback_data="application"),
        types.InlineKeyboardButton(text="🏠 Main Menu", callback_data="start_b"),
    )
    builder.adjust(1)
    return builder.as_markup()


def get_user_link(user: types.User) -> str:
    if user.username:
        return f"@{user.username}"
    return f'<a href="tg://user?id={user.id}">Open Chat (Hidden Username)</a>'


@dp.message(Command("start"))
async def start_message(message: types.Message):
    await message.answer(
        "Welcome! I am a bot for accepting freelance development orders.\n\n"
        "Select an option using the buttons below:",
        reply_markup=get_inline_buttons1()
    )


@dp.callback_query(F.data == "start_b")
async def start_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        "Welcome! I am a bot for accepting freelance development orders.\n\n"
        "Select an option using the buttons below:",
        reply_markup=get_inline_buttons1()
    )
    await callback.answer()


@dp.callback_query(F.data == "info")
async def info_message(callback: types.CallbackQuery):
    info_text = (
        "🤖 <b>About the Developer (Kernel Custom)</b>\n"
        "───────────────────────\n"
        "Hello! My name is Adil. I specialize in custom Telegram bot "
        "development and low-level system optimizations.\n"
        "Writing clean asynchronous code under Arch Linux using Neovim.\n\n"
        "───────────────────────\n"
        "💼 <b>Contact:</b> @mastermind_init4\n"
        "🚀 <i>Providing clean code, fast deployment, and high stability.</i>"
    )
    await callback.message.edit_text(
        text=info_text,
        reply_markup=get_inline_buttons4(),
        parse_mode="HTML"
    )
    await callback.answer()


@dp.callback_query(F.data == "catalog")
async def catalog(callback: types.CallbackQuery):
    catalog_text = (
        "💻 <b>Service Catalog</b>\n"
        "───────────────────────\n"
        "All development is done turn-key — from structure design to server deployment.\n\n"
        "👇 <b>Select a service category below to place an order:</b>"
    )
    await callback.message.edit_text(
        text=catalog_text,
        reply_markup=get_inline_buttons2(),
        parse_mode="HTML"
    )
    await callback.answer()


@dp.callback_query(F.data == "application")
async def post_appw(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="What type of service do you want to order?",
        reply_markup=get_inline_buttons2()
    )
    await state.set_state(OrderForm.waiting_for_item)
    await callback.answer()


@dp.callback_query(F.data == "bot_app")
async def get_botapp(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(app_type="Telegram Bot Development")
    await callback.message.edit_text(
        text="How many bots do you need? (Enter a number from 1 to 100):"
    )
    await state.set_state(OrderForm.waiting_for_count)
    await callback.answer()


@dp.message(OrderForm.waiting_for_count)
async def post_app(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("❌ Please enter a valid number (e.g., 2).")
        return

    bc = int(message.text)
    if bc < 1 or bc > 100:
        await message.answer("❌ Please enter a number between 1 and 100.")
        return

    user_data = await state.get_data()
    app_type = user_data.get("app_type")
    user_id = message.from_user.id
    client_link = get_user_link(message.from_user)

    admin_text = (
        "🚨 <b>NEW ORDER RECEIVED</b>\n"
        "───────────────────────\n"
        f"👤 <b>Client:</b> {client_link}\n"
        f"🆔 <b>Telegram ID:</b> <code>{user_id}</code>\n"
        "───────────────────────\n"
        f"📦 <b>Service Type:</b> {app_type}\n"
        f"📊 <b>Details / Quantity:</b> {bc} pcs.\n"
    )

    await bot.send_message(chat_id=ADMIN_ID, text=admin_text, parse_mode="HTML")
    await message.answer(
        text="✅ Order successfully submitted! The administrator will contact you soon.",
        reply_markup=get_inline_buttons4()
    )
    await state.clear()


@dp.callback_query(F.data == "system_opt")
async def sys_optimization(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(app_type="OS Optimization")
    await callback.message.edit_text(
        text="Which Operating System needs optimization?",
        reply_markup=get_inline_buttons3()
    )
    await state.set_state(OrderForm.waiting_for_type)
    await callback.answer()


@dp.callback_query(F.data.in_({"win_11", "win_10", "linux"}), OrderForm.waiting_for_type)
async def os_optimization_finish(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    app_type = user_data.get("app_type")

    os_mapping = {
        "win_11": "Windows 11",
        "win_10": "Windows 10",
        "linux": "Linux"
    }
    selected_os = os_mapping.get(callback.data)

    user_id = callback.from_user.id
    client_link = get_user_link(callback.from_user)

    admin_text = (
        "🚨 <b>NEW ORDER RECEIVED</b>\n"
        "───────────────────────\n"
        f"👤 <b>Client:</b> {client_link}\n"
        f"🆔 <b>Telegram ID:</b> <code>{user_id}</code>\n"
        "───────────────────────\n"
        f"📦 <b>Service Type:</b> {app_type}\n"
        f"💿 <b>Target OS:</b> {selected_os}\n"
    )

    await state.clear()
    await bot.send_message(chat_id=ADMIN_ID, text=admin_text, parse_mode="HTML")
    await callback.message.edit_text(
        text=f"✅ Order for <b>{app_type} ({selected_os})</b> successfully submitted!",
        reply_markup=get_inline_buttons4(),
        parse_mode="HTML"
    )
    await callback.answer()


@dp.callback_query(F.data == "run_script")
async def run_script_handle(callback: types.CallbackQuery):
    await callback.answer(
        text="⏳ This service is currently processed manually via PM @mastermind_init4",
        show_alert=True
    )


async def main():
    try:
        print("Bot is running...")
        await dp.start_polling(bot)
    finally:
        print("Bot stopped.")


if __name__ == "__main__":
    asyncio.run(main())
