import _winreg

key = "SOFTWARE\Microsoft\VisualStudio\%s"

possible_versions = ["10.0", "11.0"]
installed_versions = []

for v in possible_versions:
    try:
        _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, key%v, 0, _winreg.KEY_ALL_ACCESS)
        installed_versions.append(v)
    except Exception, e:
        pass

print installed_versions
