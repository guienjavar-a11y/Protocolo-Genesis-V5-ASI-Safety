# 1. Imagen base mínima (Reduce la superficie de ataque limitando las herramientas del sistema)
FROM python:3.11-slim

# 2. Bloqueo de rastro y escritura de caché
# Previene que la IA inyecte código en archivos temporales compilados (.pyc)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Creación del entorno de aislamiento (Directorio de trabajo)
WORKDIR /opt/genesis_core

# 4. Creación de un usuario sin privilegios (Aislamiento de permisos)
# Evita que el contenedor se ejecute como 'root', impidiendo que la ASI tome control del sistema anfitrión.
RUN useradd --create-home --shell /bin/bash centinela

# 5. Inyección del núcleo lógico
# Copia todos los archivos .py que tienes en tu carpeta local hacia la jaula
COPY *.py .

# 6. Sellado de Inmutabilidad (Protección contra auto-modificación)
# Entrega la propiedad al usuario y hace que los axiomas sean de SOLO LECTURA (Read-Only)
RUN chown -R centinela:centinela /opt/genesis_core \
    && chmod -R 444 /opt/genesis_core/*.py

# 7. Descenso de privilegios: El sistema cambia al usuario bloqueado antes de ejecutar nada
USER centinela

# 8. Comando de arranque (Asumiendo que genesis_v5_nucleo.py contendrá el bloque 'main' final)
CMD ["python", "genesis_v5_nucleo.py"]