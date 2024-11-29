from datetime import datetime
import os

class Log:
    carpeta_logs = "log"

    @staticmethod
    def get_archivo_log():
        ahora = datetime.now().strftime("%Y-%m-%d")
        file_name = f"{ahora}-airEuropa.log"
        file_path = os.path.join(Log.carpeta_logs, file_name)

        # Crear carpeta si no existe
        os.makedirs(Log.carpeta_logs, exist_ok=True)

        # Si el archivo no corresponde al día actual, se creará uno nuevo
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("")  # Crear archivo vacío

        return file_path

    @staticmethod
    def log(message, level):
        log_file = Log.get_archivo_log()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
        try:
            with open(log_file, "r") as f:
                id = len(f.readlines()) + 1
        except FileNotFoundError:
            id = 1
        log_message = f"{timestamp} {id} {level} {message}\n"

        with open(log_file, "a") as f:
            f.write(log_message)