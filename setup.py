from cx_Freeze import setup, Executable
base = None
executables = [Executable("main.py", base=base)]
packages = ["idna", "FPDF", "search", "json", "os", "requests", "Counter", "OrderedDict"]
options = {
    'build_exe': {
        'packages':packages,
    },
}
setup(
    name = "Logds to pdf",
    options = options,
    version = "1.0",
    description = 'Programme permettant de transformer des logs nationsglory en PDF',
    executables = executables
)