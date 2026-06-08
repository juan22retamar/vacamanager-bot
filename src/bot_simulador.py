# VACAMANAGER BOT - Simulador de Chatbot

import json
import os
import time


RUTA_DB = os.path.join(os.path.dirname(__file__), '..', 'data', 'empleados.json')

# ==========================================
# FUNCIONES DE BASE DE DATOS
# ==========================================

def cargar_empleados():
    """Carga la base de datos de empleados desde el archivo JSON."""
    try:
        with open(RUTA_DB, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("ERROR: No se encontro el archivo de base de datos.")
        print("Verifique que el archivo 'empleados.json' existe en la carpeta 'data'.")
        exit(1)
    except json.JSONDecodeError:
        print("ERROR: El archivo de base de datos tiene un formato invalido.")
        exit(1)

def guardar_empleados(empleados):
    """Guarda los cambios en la base de datos."""
    try:
        with open(RUTA_DB, 'w', encoding='utf-8') as f:
            json.dump(empleados, f, indent=2, ensure_ascii=False)
    except IOError:
        print("ADVERTENCIA: No se pudieron guardar los cambios en la base de datos.")

def buscar_empleado(legajo, empleados):
    """Busca un empleado por su legajo."""
    for emp in empleados:
        if emp['legajo'] == legajo:
            return emp
    return None

# ==========================================
# MAQUINA DE ESTADOS
# ==========================================

ESTADO_INICIO          = "INICIO"
ESTADO_PEDIR_LEGAJO    = "PEDIR_LEGAJO"
ESTADO_PEDIR_DIAS      = "PEDIR_DIAS"
ESTADO_VERIFICAR_SALDO = "VERIFICAR_SALDO"
ESTADO_ESPERAR_RRHH    = "ESPERAR_RRHH"
ESTADO_FIN             = "FIN"

# ==========================================
# FUNCIONES DEL BOT
# ==========================================

def imprimir_separador():
    print("-" * 50)

def bienvenida():
    imprimir_separador()
    print("Bienvenido a VACAMANAGER BOT")
    print("Sistema de Gestion de Vacaciones")
    print("VacaManager S.A.")
    imprimir_separador()

def pedir_legajo():
    """Solicita el legajo al empleado con validacion."""
    while True:
        try:
            legajo = input("\nBot: Por favor ingrese su numero de legajo (ej: 001): ").strip()

            if not legajo:
                print("Advertencia: El legajo no puede estar vacio. Intente nuevamente.")
                continue

            if not legajo.isdigit():
                print("Advertencia: El legajo debe contener solo numeros. Intente nuevamente.")
                continue

            legajo = legajo.zfill(3)
            return legajo

        except KeyboardInterrupt:
            print("\nOperacion cancelada por el usuario.")
            exit(0)

def pedir_dias():
    """Solicita la cantidad de dias con validacion."""
    while True:
        try:
            entrada = input("\nBot: Cuantos dias de vacaciones desea solicitar? ").strip()

            if not entrada:
                print("Advertencia: Debe ingresar una cantidad de dias. Intente nuevamente.")
                continue

            if not entrada.isdigit():
                print("Advertencia: Ingrese solo numeros. Intente nuevamente.")
                continue

            dias = int(entrada)

            if dias <= 0:
                print("Advertencia: La cantidad de dias debe ser mayor a cero. Intente nuevamente.")
                continue

            if dias > 15:
                print("Advertencia: No se pueden solicitar mas de 15 dias por solicitud. Intente nuevamente.")
                continue

            return dias

        except KeyboardInterrupt:
            print("\nOperacion cancelada por el usuario.")
            exit(0)

def simular_decision_rrhh(dias_solicitados):
    """
    Simula la decision de RRHH.
    En un sistema real, RRHH recibiria una notificacion y responderia.
    Aqui simulamos su decision automaticamente.
    RRHH aprueba solicitudes de 10 dias o menos.
    """
    print("\nBot: Su solicitud fue enviada a RRHH para evaluacion...")
    print("Bot: Esperando respuesta de RRHH", end="")

    for _ in range(3):
        time.sleep(0.8)
        print(".", end="", flush=True)
    print()

    if dias_solicitados <= 10:
        return True
    else:
        return False

# ==========================================
# FLUJO PRINCIPAL DEL BOT
# ==========================================

def ejecutar_bot():
    """
    Ejecuta el flujo principal del bot siguiendo el diagrama BPMN.

    Estados:
    1. PEDIR_LEGAJO    -> Solicita y valida legajo
    2. PEDIR_DIAS      -> Solicita cantidad de dias
    3. VERIFICAR_SALDO -> Compuerta 1: Tiene saldo suficiente?
    4. ESPERAR_RRHH    -> Compuerta 2: RRHH aprueba?
    5. FIN             -> Notifica resultado
    """

    bienvenida()
    estado = ESTADO_PEDIR_LEGAJO
    empleado = None
    dias_solicitados = 0
    empleados = cargar_empleados()

    # ESTADO: PEDIR LEGAJO
    if estado == ESTADO_PEDIR_LEGAJO:
        legajo = pedir_legajo()
        empleado = buscar_empleado(legajo, empleados)

        if not empleado:
            print(f"\nBot: No se encontro ningun empleado con el legajo '{legajo}'.")
            print("Bot: Verifique el numero e intente nuevamente.")
            imprimir_separador()
            print("Proceso finalizado.\n")
            return

        print(f"\nBot: Empleado encontrado: {empleado['nombre']}")
        print(f"Bot: Dias disponibles: {empleado['dias_disponibles']} | Dias tomados: {empleado['dias_tomados']}")
        estado = ESTADO_PEDIR_DIAS

    # ESTADO: PEDIR DIAS
    if estado == ESTADO_PEDIR_DIAS:
        dias_solicitados = pedir_dias()
        estado = ESTADO_VERIFICAR_SALDO

    # ESTADO: VERIFICAR SALDO (Compuerta 1)
    if estado == ESTADO_VERIFICAR_SALDO:
        print(f"\nBot: Verificando saldo... Solicitado: {dias_solicitados} dia/s | Disponible: {empleado['dias_disponibles']} dia/s")

        if dias_solicitados > empleado['dias_disponibles']:
            print(f"\nBot: Saldo insuficiente.")
            print(f"     Usted solicito {dias_solicitados} dias pero solo tiene {empleado['dias_disponibles']} disponibles.")
            print("Bot: Por favor contacte a RRHH para mas informacion.")
            imprimir_separador()
            print("Proceso finalizado.\n")
            return

        print("Bot: Saldo suficiente. Registrando solicitud como PENDIENTE...")
        empleado['estado_solicitud'] = "pendiente"
        guardar_empleados(empleados)
        estado = ESTADO_ESPERAR_RRHH

    # ESTADO: ESPERAR RRHH (Compuerta 2)
    if estado == ESTADO_ESPERAR_RRHH:
        aprobado = simular_decision_rrhh(dias_solicitados)

        if aprobado:
            empleado['dias_disponibles'] -= dias_solicitados
            empleado['dias_tomados']     += dias_solicitados
            empleado['estado_solicitud']  = "aprobada"
            guardar_empleados(empleados)

            print(f"\nBot: Su solicitud fue APROBADA por RRHH.")
            print(f"     Dias solicitados : {dias_solicitados}")
            print(f"     Dias restantes   : {empleado['dias_disponibles']}")
        else:
            empleado['estado_solicitud'] = "rechazada"
            guardar_empleados(empleados)

            print(f"\nBot: Su solicitud fue RECHAZADA por RRHH.")
            print(f"     Motivo: Las solicitudes de mas de 10 dias requieren aprobacion especial.")
            print("Bot: Comuniquese con RRHH para coordinar sus vacaciones.")

        estado = ESTADO_FIN

    # ESTADO: FIN
    if estado == ESTADO_FIN:
        imprimir_separador()
        print("Bot: Gracias por usar VacaManager. Hasta pronto!")
        imprimir_separador()

# ==========================================
# PUNTO DE ENTRADA
# ==========================================

if __name__ == "__main__":
    while True:
        ejecutar_bot()
        print()
        try:
            otra = input("Desea realizar otra solicitud? (s/n): ").strip().lower()
            if otra != 's':
                print("\nHasta luego!\n")
                break
        except KeyboardInterrupt:
            print("\nHasta luego!\n")
            break

