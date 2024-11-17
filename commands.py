from telegram import Update, ReplyKeyboardRemove
from telegram.ext import (
    ConversationHandler,
    ContextTypes,
    filters,
)
import json
from messages import *
import os
import logging

# Estados para la conversación
VERIFICAR, NOMBRE, APELLIDO, TELEFONO = range(4)
LOGIN = range(1)

# Cargar códigos de operadores
with open("CODES.json", "r") as file:
    operadores = json.load(file)

# Diccionario para mantener el estado de sesiones
sesiones = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nombre = update.effective_user.first_name
    await update.message.reply_text(
        bienvenida.format(nombre=nombre), reply_markup=menu_principal_markup
    )

async def verificar_operador(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(mensaje_solicitar_codigo, reply_markup=ReplyKeyboardRemove())
    return VERIFICAR

async def proceso_verificar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    codigo = update.message.text.strip()
    user_id = str(update.effective_user.id)
    if codigo in operadores["codigos"]:
        operador = operadores["codigos"][codigo]
        if operador["nombre"]:
            await update.message.reply_text(
                mensaje_ya_verificado.format(nombre=operador["nombre"]),
                reply_markup=menu_operador_markup,
            )
            sesiones[user_id] = codigo
            return ConversationHandler.END
        else:
            context.user_data["codigo"] = codigo
            await update.message.reply_text(mensaje_solicitar_datos)
            return NOMBRE
    else:
        await update.message.reply_text(mensaje_codigo_incorrecto, reply_markup=menu_principal_markup)
        return ConversationHandler.END

async def proceso_nombre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["nombre"] = update.message.text.strip()
    await update.message.reply_text(mensaje_solicitar_apellido)
    return APELLIDO

async def proceso_apellido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["apellido"] = update.message.text.strip()
    await update.message.reply_text(mensaje_solicitar_telefono)
    return TELEFONO

async def proceso_telefono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["telefono"] = update.message.text.strip()
    codigo = context.user_data["codigo"]
    operadores["codigos"][codigo]["nombre"] = context.user_data["nombre"]
    operadores["codigos"][codigo]["apellido"] = context.user_data["apellido"]
    operadores["codigos"][codigo]["telefono"] = context.user_data["telefono"]
    with open("CODES.json", "w") as file:
        json.dump(operadores, file, indent=4)
    await update.message.reply_text(
        mensaje_verificado.format(
            nombre=context.user_data["nombre"], apellido=context.user_data["apellido"]
        ),
        reply_markup=menu_operador_markup,
    )
    sesiones[str(update.effective_user.id)] = codigo
    return ConversationHandler.END

async def iniciar_sesion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(mensaje_solicitar_codigo, reply_markup=ReplyKeyboardRemove())
    return LOGIN

async def proceso_login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    codigo = update.message.text.strip()
    user_id = str(update.effective_user.id)
    if codigo in operadores["codigos"] and operadores["codigos"][codigo]["nombre"]:
        sesiones[user_id] = codigo
        nombre = operadores["codigos"][codigo]["nombre"]
        await update.message.reply_text(
            mensaje_sesion_iniciada.format(nombre=nombre),
            reply_markup=menu_operador_markup,
        )
    else:
        await update.message.reply_text(mensaje_codigo_incorrecto, reply_markup=menu_principal_markup)
    return ConversationHandler.END

async def soporte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Envía el enlace al usuario
        await update.message.reply_text(
            mensaje_redireccion_soporte,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
    except Exception as e:
        # Manejo de errores
        logging.error(f"Error al redirigir al soporte: {e}")
        await update.message.reply_text(mensaje_error_soporte)

async def soporte_operador(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Envía el enlace al operador
        await update.message.reply_text(
            mensaje_redireccion_soporte,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
    except Exception as e:
        # Manejo de errores
        logging.error(f"Error al redirigir al soporte: {e}")
        await update.message.reply_text(mensaje_error_soporte)

async def informacion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(mensaje_informacion, reply_markup=menu_principal_markup)

async def iniciar_viaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(mensaje_iniciar_viaje, reply_markup=menu_operador_markup)

async def paradas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(mensaje_paradas.format(parada="Estación Central"), reply_markup=menu_operador_markup)

async def finalizar_viaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(mensaje_finalizar_viaje, reply_markup=menu_operador_markup)

async def cerrar_sesion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    if user_id in sesiones:
        del sesiones[user_id]
    await update.message.reply_text(mensaje_sesion_cerrada, reply_markup=menu_principal_markup)

async def handle_menu_principal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == 'Verificar Operador':
        return await verificar_operador(update, context)
    elif text == 'Iniciar Sesión':
        return await iniciar_sesion(update, context)
    elif text == 'Soporte':
        return await soporte(update, context)
    elif text == 'Información':
        return await informacion(update, context)
    else:
        await update.message.reply_text(mensaje_opcion_invalida, reply_markup=menu_principal_markup)

async def handle_menu_operador(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == 'Iniciar Viaje':
        await iniciar_viaje(update, context)
    elif text == 'Paradas':
        await paradas(update, context)
    elif text == 'Finalizar Viaje':
        await finalizar_viaje(update, context)
    elif text == 'Soporte':
        return await soporte_operador(update, context)
    elif text == 'Cerrar Sesión':
        return await cerrar_sesion(update, context)
    else:
        await update.message.reply_text(mensaje_opcion_invalida, reply_markup=menu_operador_markup)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(mensaje_error)
