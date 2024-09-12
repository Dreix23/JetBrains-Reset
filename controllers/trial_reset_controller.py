import os
import platform
import subprocess

class TrialResetController:
    def __init__(self):
        self.products = [
            {"name": "IntelliJ IDEA", "icon": "intellij-idea-ce.svg"},
            {"name": "CLion", "icon": "0.svg"},
            {"name": "DataGrip", "icon": "1.svg"},
            {"name": "GoLand", "icon": "2.svg"},
            {"name": "PhpStorm", "icon": "3.svg"},
            {"name": "PyCharm", "icon": "4.svg"},
            {"name": "ReSharper", "icon": "5.svg"},
            {"name": "Rider", "icon": "6.svg"},
            {"name": "RubyMine", "icon": "7.svg"},
            {"name": "WebStorm", "icon": "8.svg"}
        ]
        self.os_name = platform.system().lower()

    def reset_product_windows(self):
        commands = [
            "@echo off",
            "echo [ INFO ] Eliminando clave de usuario JavaSoft...",
            "reg delete \"HKEY_CURRENT_USER\\Software\\JavaSoft\" /f",
            "if %ERRORLEVEL% equ 0 (",
            "echo [ OK ] Clave eliminada correctamente.",
            ") else (",
            "echo [ ! ] La clave ha sido eliminada.",
            ")",
            "echo [ INFO ] Eliminando PermanentUserId...",
            "del /F /Q \"%APPDATA%\\JetBrains\\PermanentUserId\"",
            "if %ERRORLEVEL% equ 0 (",
            "echo [ OK ] PermanentUserId eliminado correctamente.",
            ") else (",
            "echo [ ! ] PermanentUserId ha sido eliminado.",
            ")"
        ]

        script_path = "reset_windows.bat"
        with open(script_path, "w") as script_file:
            script_file.write("\n".join(commands))

        try:
            output = subprocess.check_output(["cmd", "/c", script_path], stderr=subprocess.STDOUT,
                                             universal_newlines=True)
            return output
        except subprocess.CalledProcessError as e:
            return f"Error: {e.output}"
        finally:
            os.remove(script_path)

    def reset_product_linux(self, products):
        config_path = os.path.expanduser("~/.config/JetBrains/")
        output = []

        for product in products:
            result_path = os.path.join(config_path, product)
            product_name = os.path.basename(result_path)
            name_path = os.path.join(config_path, product_name)

            if os.path.isdir(name_path):
                output.append(f"[ INFO ] Restableciendo período de prueba para [{product_name}]")

                try:
                    subprocess.run(["rm", "-rf", os.path.join(name_path, "eval")], check=True)
                    output.append("[ OK ] Clave de evaluación eliminada correctamente.")
                except subprocess.CalledProcessError:
                    output.append("[ ERROR ] No se pudo eliminar la clave de evaluación.")

                try:
                    subprocess.run(["sed", "-i", "s/evlsprt//", os.path.join(name_path, "options", "other.xml")],
                                   check=True)
                    output.append("[ OK ] Propiedades evlsprt eliminadas correctamente.")
                except subprocess.CalledProcessError:
                    output.append("[ ERROR ] No se pudieron eliminar las propiedades evlsprt.")

                try:
                    subprocess.run(["rm", "-rf", os.path.expanduser("~/.java/.userPrefs")], check=True)
                    output.append("[ OK ] Archivos userPrefs eliminados correctamente.")
                except subprocess.CalledProcessError:
                    output.append("[ ERROR ] No se pudieron eliminar los archivos userPrefs.")
            else:
                output.append(f"[ ADVERTENCIA ] El directorio para {product_name} no existe.")

        return "\n".join(output)
