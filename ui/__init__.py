from PySide2.QtWidgets import QApplication
from binaryninjaui import DockHandler
from PySide2.QtCore import Qt
from .registers_view import RegisterView
from .memory_view import MemoryView

RW = None
MW = None

def _get_registerview_widget(name, parent, data):
    global RW
    if RW is not None:
        return RW
    RW = RegisterView(parent, name, data)
    RW.setEnabled(False)
    return RW

def _get_memoryview_widget(name, parent, data):
    global MW
    if MW is not None:
        return MW
    MW = MemoryView(parent, name, data)
    MW.setEnabled(False)
    return MW

def _registerDynamicWidgets():
    mw = QApplication.allWidgets()[0].window()
    dock_handler = mw.findChild(DockHandler, '__DockHandler')
    dock_handler.addDockWidget (
        "SENinja Registers",
        _get_registerview_widget,
        Qt.RightDockWidgetArea,
        Qt.Vertical,
        False
    )
    dock_handler.addDockWidget (
        "SENinja Memory",
        _get_memoryview_widget,
        Qt.BottomDockWidgetArea,
        Qt.Horizontal,
        False
    )

def enable_widgets():
    assert RW is not None
    assert MW is not None

    RW.setEnabled(True)
    MW.setEnabled(True)

def disable_widgets():
    assert RW is not None
    assert MW is not None

    RW.setEnabled(False)
    MW.setEnabled(False)

def ui_set_arch(arch, state):
    assert RW is not None
    assert MW is not None
    RW.init(arch, state)
    MW.init(arch, state)

def ui_sync_view(state, delta=True):
    assert RW is not None
    assert MW is not None
    if RW.isVisible():
        RW.set_reg_values(state)
    if MW.isVisible():
        if delta:
            MW.update_mem_delta(state)
        else:
            MW.update_mem(state)

def ui_reset_view():
    assert RW is not None
    assert MW is not None

    RW.reset()
    MW.reset()

_registerDynamicWidgets()
