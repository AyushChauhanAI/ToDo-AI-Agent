from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging
from config import TOKEN

# ============================================================
# 1. LOGGING SETUP
# ============================================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

logger.info("🚀 Program started")


# ============================================================
# 4. /start COMMAND FUNCTION
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
# 5. CREATE TELEGRAM APPLICATION
# ============================================================

logger.info("🏗️ Creating Telegram Application...")

app = Application.builder().token(TOKEN).build()

logger.info("✅ Telegram Application created")


# ============================================================
# 6. ADD /start COMMAND HANDLER
# ============================================================

logger.info("🔗 Registering /start command handler...")

app.add_handler(
    CommandHandler("start", start)
)

logger.info("✅ /start handler registered")


# ============================================================
# 7. START BOT
# ============================================================

logger.info("🤖 Starting Telegram bot...")
logger.info("👂 Bot is now listening for messages...")

app.run_polling()

logger.info("🛑 Bot stopped")