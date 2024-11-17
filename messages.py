from telegram import ReplyKeyboardMarkup

# Teclados personalizados (sin emojis para evitar errores)
menu_principal_keyboard = [['Verificar Operador', 'Iniciar Sesión'],
                           ['Soporte', 'Información']]

menu_operador_keyboard = [['Iniciar Viaje', 'Paradas'],
                          ['Finalizar Viaje', 'Soporte'],
                          ['Cerrar Sesión']]

menu_principal_markup = ReplyKeyboardMarkup(menu_principal_keyboard, resize_keyboard=True)
menu_operador_markup = ReplyKeyboardMarkup(menu_operador_keyboard, resize_keyboard=True)

# Mensajes
bienvenida = (
    "👋 ¡Hola, {nombre}! 🚍 Bienvenido al *Bot de Operadores de Transporte*. "
    "Estamos aquí para facilitarte el día. ¿Qué necesitas hacer hoy? 🚦"
)

mensaje_verificado = (
    "✅ ¡Todo en orden! Tu verificación como operador fue *exitosa*. \n"
    "🎉 ¡Bienvenido a bordo, {nombre} {apellido}! 🌟"
)

mensaje_ya_verificado = (
    "⚠️ Hola, {nombre}. Parece que ya has completado tu registro. 👷‍♂️\n"
    "Si necesitas ayuda adicional, no dudes en consultarnos. 😊"
)

mensaje_solicitar_codigo = (
    "🔑 *¡Tu seguridad es importante!*\n"
    "Por favor, escribe tu *código de operador* para continuar. 🚧"
)

mensaje_codigo_incorrecto = (
    "❌ *Oops... algo no está bien.*\n"
    "El código que ingresaste no es válido. Inténtalo nuevamente o contacta a soporte si el problema persiste. 🤔"
)

mensaje_solicitar_datos = (
    "✏️ *Estamos casi listos.*\n"
    "Por favor, ingresa tu *nombre completo* para continuar. 😊"
)

mensaje_solicitar_apellido = "👤 ¡Perfecto! Ahora escribe tu *apellido* para completar el registro. 📝"
mensaje_solicitar_telefono = "📞 Por último, ingresa tu *número de teléfono*. ¡Ya casi terminamos! 📱"

mensaje_sesion_iniciada = (
    "🔓 *¡Hola de nuevo!* \n"
    "Tu sesión se inició exitosamente, {nombre}. 🎉\n"
    "Estamos listos para ayudarte a gestionar tus rutas. 🚍"
)

mensaje_sesion_cerrada = (
    "🔒 *Cierre de sesión exitoso.* \n"
    "Gracias por usar nuestro sistema. ¡Hasta la próxima! 👋"
)

mensaje_iniciar_viaje = (
    "🗺️ *Hora de emprender el viaje.*\n"
    "Selecciona tu ruta preferida:\n"
    "1️⃣ *Mina-Canticas/Coatza*\n"
    "2️⃣ *Cosolea-Mina/Coatza*\n"
    "¡Buena suerte en el camino! 🚚"
)

mensaje_paradas = (
    "🛑 *Próxima parada detectada.*\n"
    "🗺️ Deteniéndonos en: {parada}. ¡Asegúrate de estar listo! 🎒"
)

mensaje_finalizar_viaje = (
    "🏁 *¡Buen trabajo!* \n"
    "Has completado tu viaje satisfactoriamente. 🚍\n"
    "Recuerda descansar y estar listo para tu próxima ruta. ¡Hasta pronto! 🌟"
)

mensaje_soporte = (
    "📞 *¡Gracias por contactarnos!* \n"
    "Un representante se pondrá en contacto contigo en breve. ✉️\n"
    "Si necesitas atención personalizada, revisa el [Chat de Soporte](https://t.me/xyzxgll)."
)

mensaje_informacion = (
    "ℹ️ *Información importante sobre el bot.* \n"
    "Este bot está diseñado para ayudarte a gestionar tus viajes y rutas como operador. 🚌\n"
    "📩 Para más información sobre nuestros servicios o la renta del bot, ¡contáctanos!"
)

mensaje_redireccion_soporte = (
    "📞 *¿Necesitas ayuda inmediata?*\n"
    "Contacta a nuestro equipo de soporte a través del siguiente enlace: "
    "[Chat de Soporte](https://t.me/xyzxgll). ✉️"
)

mensaje_error_soporte = (
    "⚠️ *Lo sentimos mucho.* \n"
    "No pudimos redirigirte al soporte en este momento. Inténtalo nuevamente más tarde. 😔"
)

mensaje_opcion_invalida = (
    "❌ *Ups... esa opción no es válida.* \n"
    "Por favor, selecciona una de las opciones del menú. 🎛️"
)

mensaje_error = (
    "⚠️ *Ha ocurrido un error inesperado.* \n"
    "Por favor, intenta nuevamente más tarde. Si el problema persiste, contacta a soporte. 🛠️"
)
