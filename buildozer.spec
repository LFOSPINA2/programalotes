[app]
title = Gestion de Lotes
package.name = gestionlotes
package.domain = org.tuchorizo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xlsx,ttf,json
presplash.filename = %(source.dir)s/logo.png
android.presplash_color = #fee7be
version = 1.0
requirements = python3,kivy,openpyxl,google-api-python-client,oauth2client,pyopenssl,certifi,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
