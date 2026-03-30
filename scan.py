import requests
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor

init(autoreset=True)

base = "https://website.com"

paths = [
# root/common
"/","/home","/index","/main","/default",
"/robots.txt","/sitemap.xml","/sitemap.txt","/humans.txt",

# env / secrets
"/.env","/.env.local","/.env.dev","/.env.prod","/.env.backup",
"/.env.save",".env",".env.local",".env.dev",".env.prod",
"/config.env","/secrets.env",

# git / vcs
"/.git","/.git/config","/.gitignore","/.git/HEAD",
"/.svn","/.hg",

# apache/nginx
"/.htaccess","/.htpasswd","/server-status","/server-info",

# debug
"/debug","/debug/","/__debug__/","/django-debug-toolbar/",
"/_debug_toolbar","/console","/phpinfo.php","/info.php",

# admin panels
"/admin","/admin/","/admin/login","/admin/dashboard",
"/administrator","/backend","/controlpanel","/cpanel",
"/admin.php","/admin.html","/login","/login.php",
"/auth","/auth/login","/dashboard",

# api
"/api","/api/","/api/v1","/api/v2","/api/docs",
"/api/users","/api/admin",
"/swagger","/swagger.json","/openapi.json","/docs",

# configs
"/config.json","/config.yaml","/config.yml","/config.php",
"/settings.json","/settings.py","/settings.yaml",
"/database.yml","/db.php","/db.sql",

# backups
"/backup.zip","/backup.tar","/backup.tar.gz",
"/site.zip","/www.zip","/html.zip",
"/backup.sql","/dump.sql","/database.sql",
"/backup.old","/backup.bak",

# logs
"/logs","/log","/error.log","/access.log",
"/debug.log","/app.log",

# uploads / files
"/uploads","/upload","/files","/media","/static",
"/images","/img","/assets",

# temp/dev
"/tmp","/temp","/cache","/dev","/test","/staging",
"/old","/backup","/beta","/new","/v1","/v2",

# cms specific
"/wp-admin","/wp-login.php","/wp-content","/wp-config.php",
"/joomla","/drupal","/sites/default","/user/login",

# misc sensitive
"/.bash_history","/.ssh","/.ssh/id_rsa",
"/id_rsa","/authorized_keys",
"/.DS_Store","/web.config",

# interesting endpoints
"/search","/user","/users","/account",
"/profile","/settings","/register",
"/forgot","/reset","/password"
]

headers = {"User-Agent": "Mozilla/5.0"}
seen = set()

def scan(p):
    url = base + p
    try:
        r = requests.get(url, headers=headers, timeout=5, allow_redirects=False)
        code = r.status_code
        length = len(r.text)

        if code == 200 and length in seen:
            return
        seen.add(length)

        if code == 200:
            print(Fore.GREEN + f"[200] {p} | {length}")
        elif code in (301,302):
            print(Fore.CYAN + f"[{code}] {p} -> {r.headers.get('Location')}")
        elif code == 403:
            print(Fore.YELLOW + f"[403] {p}")
        elif code >= 500:
            print(Fore.MAGENTA + f"[{code}] {p}")
    except:
        print(Fore.RED + f"[ERR] {p}")

with ThreadPoolExecutor(max_workers=25) as ex:
    ex.map(scan, paths)
