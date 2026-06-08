# MANUAL DE USUARIO
## VacaManager Bot — Sistema de Gestión de Vacaciones

---

## 1. INTRODUCCION

VacaManager Bot es un simulador de chatbot para gestionar solicitudes de vacaciones de los empleados de VacaManager S.A. El empleado ingresa sus datos, el sistema verifica su saldo y RRHH aprueba o rechaza la solicitud.

---

## 2. REQUISITOS

- Python 3.8 o superior
- Archivo `empleados.json` en la carpeta `data/`

---

## 3. COMO EJECUTAR EL BOT

Abrir una terminal y ejecutar:

```
python src/bot_simulador.py
```

---

## 4. PASOS DEL BOT

**Paso 1 — Legajo**
El bot pide el numero de legajo del empleado. Solo acepta numeros.

**Paso 2 — Dias solicitados**
El bot muestra los dias disponibles y pide cuantos dias quiere tomar. Maximo 15 dias por solicitud.

**Paso 3 — Verificacion de saldo**
El bot verifica si tiene dias suficientes. Si no tiene, el proceso termina.

**Paso 4 — Respuesta de RRHH**
RRHH evalua la solicitud. Aprueba hasta 10 dias. Mas de 10 dias requiere gestion especial.

---

## 5. EJEMPLOS

### Solicitud aprobada
```
Bot: Ingrese su legajo: 001
Bot: Empleado encontrado: Ana Garcia. Dias disponibles: 15
Bot: Cuantos dias solicita? 5
Bot: Solicitud APROBADA. Dias restantes: 10
```

### Saldo insuficiente
```
Bot: Ingrese su legajo: 003
Bot: Empleado encontrado: Maria Fernandez. Dias disponibles: 0
Bot: Cuantos dias solicita? 5
Bot: Saldo insuficiente. Contacte a RRHH.
```

### Legajo incorrecto
```
Bot: Ingrese su legajo: abc
Advertencia: Solo se aceptan numeros.
```

---

## 6. ERRORES POSIBLES

| Error | Causa | Respuesta |
|---|---|---|
| Legajo con letras | Se ingreso texto | Pide solo numeros |
| Legajo inexistente | No esta en la base de datos | Finaliza el proceso |
| Dias con letras | Se ingreso texto | Pide solo numeros |
| Dias mayor a 15 | Supera el limite | Pide un valor menor |
| Saldo insuficiente | No tiene dias disponibles | Finaliza el proceso |

---

## 7. INTEGRANTE

Juan Retamar
