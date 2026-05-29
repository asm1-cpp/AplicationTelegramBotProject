# ApplicationTelegramBotProject

A clean, asynchronous Telegram bot built with **Aiogram 3** to accept and process freelance development and system optimization orders.

## 🚀 Features

- **Service Catalog**: Interactive inline keyboards to browse available services.
- **Order Form (FSM)**: Multi-step state machine for tracking order details.
- **Admin Notifications**: Automatically formats and forwards new client orders directly to the administrator's Telegram ID.
- **Asynchronous Architecture**: Built on top of `asyncio` for high performance and stability.

## 🛠️ Stack

- **Language**: Python 3.10+
- **Framework**: [Aiogram 3.x](https://github.com/aiogram/aiogram) (Telegram Bot API wrapper)
- **Environment**: Linux (Arch Linux preferred)

## 📋 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/asm1-cpp/AplicationTelegramBotProject.git](https://github.com/asm1-cpp/AplicationTelegramBotProject.git)
   cd AplicationTelegramBotProject
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install aiogram
   ```

4. **Configure the Environment:**
   Open `main.py` and replace the placeholder configuration values with your actual data:
   ```python
   TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
   ADMIN_ID = YOUR_TELEGRAM_CHAT_ID
   ```

## 🏎️ Running the Bot

To start the bot in polling mode, simply run:
```bash
python main.py
```

## 📂 Project Structure

- `main.py` — The core script containing all handlers, inline keyboard builders, and FSM states.
- `.gitignore` — Standard rule file to avoid tracking local files like `.idea/` or virtual environments.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
