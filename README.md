# vacamanager-bot
Simulador de chatbot para gestión de vacaciones - TUP OE
#  VacaManager Bot

Simulador de chatbot para la gestión de solicitudes de vacaciones de empleados.  
Trabajo Práctico Integrador — Cátedra: Organización Empresarial  
Tecnicatura Universitaria en Programación (TUP) — UTN

---

##  Descripción del Proyecto

**VacaManager S.A.** es una empresa ficticia de desarrollo de software con 20 empleados.  
Este proyecto automatiza el proceso de solicitud de vacaciones mediante un chatbot simulado,
modelado con la metodología BPMN 2.0.

El bot permite a un empleado:
1. Iniciar una solicitud de vacaciones
2. Verificar su saldo de días disponibles
3. Enviar la solicitud a RRHH para aprobación
4. Recibir notificación de aprobación o rechazo

---

##  Estructura del Repositorio

```
vacamanager-bot/
│
├── README.md                        # Este archivo
├── docs/
│   ├── bpmn/
│   │   └── diagrama_vacaciones.xml  # Diagrama BPMN 2.0 del proceso
│   └── manual_usuario.md            # Guía de uso del simulador
│
├── data/
│   └── empleados.json               # Base de datos simulada (20 empleados)
│
└── src/
    └── bot_simulador.py             # Código del simulador del chatbot
```

---

## ⚙️ Tecnologías Utilizadas

| Elemento | Elección |
|---|---|
| Lenguaje | Python 3 |
| Plataforma | Consola (simulador local) |
| Base de datos | JSON (empleados.json) |
| Modelado | BPMN 2.0 (draw.io) |
| IA utilizada | Claude (Anthropic) |

---

##  Cómo Ejecutar el Simulador

### Requisitos
- Python 3.8 o superior instalado
- No requiere librerías externas

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/juan22retamar/vacamanager-bot.git

# 2. Entrar a la carpeta
cd vacamanager-bot

# 3. Ejecutar el simulador
python src/bot_simulador.py
```

---

##  Flujo del Proceso (resumen)

```
Empleado inicia solicitud
        ↓
Bot solicita: nombre + legajo + días solicitados
        ↓
¿Tiene saldo suficiente? ── No ──→ Informa saldo insuficiente → FIN
        ↓ Sí
Bot registra solicitud como "pendiente"
        ↓
RRHH evalúa la solicitud (simulado)
        ↓
¿RRHH aprueba? ── No ──→ Notifica rechazo al empleado → FIN
        ↓ Sí
Notifica aprobación + descuenta días del saldo → FIN
```

---

##  Integrante

| Nombre | apellido |
|---|---|
| juan | retamar |


---

##  Documentación adicional

-  Diagrama BPMN: `/docs/bpmn/diagrama_vacaciones.xml`
-  Manual de usuario: `/docs/manual_usuario.md`
-  Base de datos: `/data/empleados.json`
