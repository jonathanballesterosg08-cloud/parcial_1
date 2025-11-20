#                      ┌────────────────────┐                                    
#                      │      Criatura      │
#                      ├────────────────────┤
#                      │ - nombre: str      │
#                      │ - energia: int     │
#                      │ - amigable: bool   │
#                      ├────────────────────┤
#                      │ + interactuar(j)   │
#                      └─────────┬──────────┘
#                        ▲       │
#            ┌───────────┘       └──────────────┐
#            │                                   │
# ┌──────────────────────────┐      ┌──────────────────────────┐
# │   CriaturaAmigable       │      │    CriaturaHostil        │
# ├──────────────────────────┤      ├──────────────────────────┤
# │ - regalo: str            │      │ - daño: int              │
# ├──────────────────────────┤      ├──────────────────────────┤
# │ + interactuar(jugador)   │      │ + interactuar(jugador)   │
# └──────────────────────────┘      └──────────────────────────┘


# ┌──────────────────────────┐
# │        Jugador           │
# ├──────────────────────────┤
# │ - nombre: str            │
# │ - vida: int              │
# │ - inventario: list       │
# ├──────────────────────────┤
# │ + decidir(): str         │
# │ + interactuar(criatura)  │
# └──────────────────────────┘


# ┌──────────────────────────┐
# │         Bosque           │
# ├──────────────────────────┤
# │ - criaturas: list        │
# ├──────────────────────────┤
# │ + generar_evento(): C    │
# │ + recorrer(jugador)      │
# └──────────────────────────┘


# Relaciones:
# - Bosque *contiene* múltiples Criatura.
# - Jugador *interactúa* con Criatura (composición débil).
# - CriaturaAmigable y CriaturaHostil **heredan** de Criatura.


# Descripción de relaciones
# Herencia

# CriaturaAmigable → hereda de → Criatura

# CriaturaHostil → hereda de → Criatura

# Composición / Agregación

# Bosque tiene una lista de criaturas

# Jugador interactúa con criaturas, pero no las posee

# Asociación

# Jugador.interactuar() llama a criatura.interactuar(self)

# Bosque.recorrer(jugador) usa la clase Jugador durante el recorrido