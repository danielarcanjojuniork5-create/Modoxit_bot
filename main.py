import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 Ver Demo", callback_data="demo")],
        [InlineKeyboardButton("💰 Comprar", callback_data="buy")],
        [InlineKeyboardButton("📞 Suporte", callback_data="support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 HACKER MODE VISUAL 🔥\n\nEscolha uma opção:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "demo":
        await query.edit_message_text(
            "🎬 Demonstração:\n\nOverlay visual estilo hacker para entretenimento."
        )

    elif query.data == "buy":
        await query.edit_message_text(
            "💰 Valor: R$ XX\n\nChave Pix: SUA-CHAVE-AQUI\n\nEnvie o comprovante para receber."
        )

    elif query.data == "support":
        await query.edit_message_text(
            "📞 Suporte:\nEntre em contato: @seuuser"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
