from cx_Freeze import setup, Executable

setup(
    name = "hmm_generator",
    version = "1.0",
    description = "test",
    executables = [Executable(script="hmm_generator.py")])