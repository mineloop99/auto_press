from win32gui import GetWindowText, GetForegroundWindow


def get_active_window():
    return GetWindowText(GetForegroundWindow())
