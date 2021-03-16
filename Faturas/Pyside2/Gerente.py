from Faturas.Pyside2 import GUITela_de_Login as tl, Tela_Principal as tp
import sys


def system_load():
    logged = tl.execution()
    if logged:
        tp.execution()


system_load()
sys.exit(0)
