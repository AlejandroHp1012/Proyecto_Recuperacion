import tkinter as tk

# Configuración de la ventana principal
root = tk.Tk()
root.title("Centro de Control")
root.geometry("520x260")

# --- Estado ---
input_value = tk.StringVar(value="")
last_event = tk.StringVar(value="(sin eventos)")

# En Tkinter también podemos tener estado numérico.
# Para esta semana lo iniciamos como entero simple.
event_count = 0

# --- Controles (widgets) ---

# 1. Encabezado
header = tk.Label(
    root,
    text="Centro de Control",
    font=("Arial", 14, "bold"),
)
header.pack(pady=(10, 6))

# Entrada de texto (para generar eventos de teclado)
entry = tk.Entry(root, textvariable=input_value, width=50)
entry.pack(pady=6)

# Botón (para generar eventos de click)
btn = tk.Button(root, text="Registrar evento")
btn.pack(pady=6)

# 2. Sección de "último evento recibido"
out = tk.Label(root, textvariable=last_event)
out.pack(pady=6)

# 3. Contador de eventos
counter = tk.Label(root, text=f"Contador de eventos: {event_count}")
counter.pack(pady=6)

# --- Funciones (Handlers) ---

def on_input_change(event):
    """Evento: el usuario soltó una tecla dentro del Entry."""
    v = input_value.get()

    # Evidencia visible
    last_event.set(f"input_change | value='{v}'")

    # Evidencia adicional (terminal)
    print("EVENT input_change", v)

# Conectamos el evento del widget a nuestro handler
entry.bind("<KeyRelease>", on_input_change)

def on_button_click():
    """Evento: click del botón."""
    global event_count

    event_count += 1
    v = input_value.get()

    # Evidencia visible
    last_event.set(f"button_click | value='{v}'")
    # Actualizamos el label del contador manualmente
    counter.config(text=f"Contador de eventos: {event_count}")

    # Evidencia adicional
    print("EVENT button_click", v)

# Conectamos el evento click del botón
btn.config(command=on_button_click)

def on_submit_enter(event):
    """Evento: Enter dentro del Entry (simula submit)."""
    on_button_click()  # Reutiliza la lógica del click

    v = input_value.get()
    # Sobrescribimos el mensaje para ser más específicos
    last_event.set(f"submit_enter | value='{v}'")
    print("EVENT submit_enter", v)

# Conectamos Enter del Entry
entry.bind("<Return>", on_submit_enter)

# --- Ciclo principal ---
root.mainloop()