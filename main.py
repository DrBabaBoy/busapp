# main.py

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)
from config import API
from commands import *
import logging

# Configuración del registro de errores
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

def main():
    application = ApplicationBuilder().token(API).build()

    # Handlers de conversación para verificar operador
    conv_handler_verificar = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('^Verificar Operador$'), verificar_operador)],
        states={
            VERIFICAR: [MessageHandler(filters.TEXT & ~filters.COMMAND, proceso_verificar)],
            NOMBRE: [MessageHandler(filters.TEXT & ~filters.COMMAND, proceso_nombre)],
            APELLIDO: [MessageHandler(filters.TEXT & ~filters.COMMAND, proceso_apellido)],
            TELEFONO: [MessageHandler(filters.TEXT & ~filters.COMMAND, proceso_telefono)],
        },
        fallbacks=[MessageHandler(filters.ALL, error)],
    )

    # Handler de conversación para iniciar sesión
    conv_handler_login = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('^Iniciar Sesión$'), iniciar_sesion)],
        states={
            LOGIN: [MessageHandler(filters.TEXT & ~filters.COMMAND, proceso_login)],
        },
        fallbacks=[MessageHandler(filters.ALL, error)],
    )

    # Handlers para los menús
    application.add_handler(CommandHandler("start", start))
    application.add_handler(conv_handler_verificar)
    application.add_handler(conv_handler_login)

    # Menú principal
    application.add_handler(MessageHandler(
        filters.Regex('^(Verificar Operador|Iniciar Sesión|Soporte|Información)$'), handle_menu_principal
    ))

    # Menú de operador
    application.add_handler(MessageHandler(
        filters.Regex('^(Iniciar Viaje|Paradas|Finalizar Viaje|Soporte|Cerrar Sesión)$'), handle_menu_operador
    ))

    # Handler de errores
    application.add_error_handler(error)

    # Iniciar el bot
    application.run_polling()

if __name__ == "__main__":
    main()
