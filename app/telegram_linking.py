import logging
import re

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import TOKEN


# ============================================================
# 1. LOGGING SETUP
# ============================================================

class TokenFilter(logging.Filter):
    def filter(self, record):
        message = record.getMessage()

        # Hide Telegram bot token
        message = re.sub(
            r'/bot\d+:[A-Za-z0-9_-]+',
            '/bot***',
            message
        )

        record.msg = message
        record.args = ()

        return True


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Hide ONLY the token, but keep httpx INFO logs
for handler in logging.getLogger().handlers:
    handler.addFilter(TokenFilter())


logger = logging.getLogger(__name__)

logger.info("🚀 Program started")


# ============================================================
# 2. /start COMMAND FUNCTION
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.info("📩 /start command received")

    logger.info(
        f"👤 User: {update.effective_user.first_name}"
    )

    logger.info(
        f"🆔 User ID: {update.effective_user.id}"
    )

    logger.info("🤖 Sending response to user...")

    await update.message.reply_text(
        "Hello! 🤖 Bot working perfectly!"
    )

    logger.info("✅ Response sent successfully")


# ============================================================
# 3. CREATE TELEGRAM APPLICATION
# ============================================================

logger.info("🏗️ Creating Telegram Application...")

app = Application.builder().token(TOKEN).build()

logger.info("✅ Telegram Application created")


# ============================================================
# 4. ADD /start COMMAND HANDLER
# ============================================================

logger.info("🔗 Registering /start command handler...")

app.add_handler(
    CommandHandler("start", start)
)

logger.info("✅ /start handler registered")


# ============================================================
# 5. START BOT
# ============================================================

logger.info("🤖 Starting Telegram bot...")
logger.info("👂 Bot is now listening for messages...")

app.run_polling()

logger.info("🛑 Bot stopped")