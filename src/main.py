from telegram.ext import ApplicationBuilder
from src.config import settings
from src.core.ai import AIClient
from src.handlers import MessageHandler
from redis import Redis

def main():
    # Initialisation
    redis = Redis.from_url(settings.REDIS_URL)
    ai = AIClient(redis)
    handler = MessageHandler(ai)

    # Application Telegram
    app = ApplicationBuilder().token(settings.TELEGRAM_TOKEN).build()
    handler.register(app)
    
    # Monitoring (optionnel)
    from prometheus_client import start_http_server
    start_http_server(8000)

    app.run_polling()

if __name__ == "__main__":
    main()
