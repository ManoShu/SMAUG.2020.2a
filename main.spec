# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


arquivos = [
    ('back_3.png', '.'),
    ('creditos.txt', '.'),
    ('Explosion2.wav', '.'),
    ('meteorBrown_med3.png', '.'),
    ('musica_loop.ogg', '.'),
    ('Pickup_Coin11.wav', '.'),
    ('Pickup_Coin12.wav', '.'),
    ('slugan_idle.png', '.'),
    ('ufoGreen.png', '.'),
]

a = Analysis(['main.py'],
             pathex=['C:\\Users\\ManoShuZero\\PycharmProjects\\SMAUG.2020.2a'],
             binaries=[],
             datas=arquivos,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='slugan_1_5',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
