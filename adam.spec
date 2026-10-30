# -*- mode: python ; coding: utf-8 -*-
import os
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None
base_dir = Path(r"C:\Users\Shravan\Downloads\Compressed\Mark-LIII-main\Mark-LIII-main")

datas = [
    (str(base_dir / "core" / "prompt.txt"), "core"),
    (str(base_dir / "config"), "config"),
    (str(base_dir / "dashboard" / "static"), "dashboard/static"),
    (str(base_dir / "actions"), "actions"),
    (str(base_dir / "core"), "core"),
    (str(base_dir / "memory"), "memory"),
    (str(base_dir / "plugins"), "plugins"),
]

for pkg in ("openwakeword", "playwright", "docx", "pptx"):
    try:
        datas += collect_data_files(pkg)
    except Exception:
        pass

hiddenimports = [
    "PyQt6",
    "PyQt6.QtCore",
    "PyQt6.QtGui",
    "PyQt6.QtWidgets",
    "google.genai",
    "google.genai.types",
    "sounddevice",
    "numpy",
    "requests",
    "bs4",
    "psutil",
    "PIL",
    "cv2",
    "mss",
    "fastapi",
    "uvicorn",
    "cryptography",
    "pyautogui",
    "pyperclip",
    "pygetwindow",
    "win32com",
    "win32com.client",
    "pycaw",
    "pycaw.pycaw",
    "comtypes",
    "wmi",
    "asyncio",
    "json",
    "threading",
    "webbrowser",
    "runpy",
    # Newly bundled action dependencies
    "playwright",
    "playwright.sync_api",
    "playwright.async_api",
    "youtube_transcript_api",
    "pdfplumber",
    "pdfminer",
    "pdfminer.high_level",
    "pypdfium2",
    "PyPDF2",
    "docx",
    "pptx",
    "pandas",
    "openpyxl",
    "send2trash",
    "plyer",
    "plyer.platforms.win.notification",
    "win10toast",
    "openwakeword",
    "openwakeword.model",
    "openwakeword.utils",
    "onnxruntime",
    "ddgs",
    "duckduckgo_search",
    "keyboard",
]

for _mod in ("plyer", "uvicorn", "fastapi", "starlette", "cryptography", "anyio", "websockets"):
    try:
        hiddenimports += collect_submodules(_mod)
    except Exception:
        pass

a = Analysis(
    [str(base_dir / "main.py")],
    pathex=[str(base_dir)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['sklearn', 'scikit-learn', 'scipy', 'torch', 'torchvision'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ADAM',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(base_dir / "config" / "adam.ico"),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='ADAM',
)
