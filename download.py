import os

print(os.getcwd())
os.system('VisualStudioSetup.exe --layout {path}'.format(path=os.getcwd()+r'\vs2022'))
