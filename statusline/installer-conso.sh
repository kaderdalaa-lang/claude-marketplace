#!/bin/bash
# Installe la barre de conso Claude (5h + 7 jours, vert/rouge) dans Claude Code.
set -e
CFG="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
SRC="$(cd "$(dirname "$0")" && pwd)/statusline-conso.py"
command -v python3 >/dev/null || { echo "python3 manquant"; exit 1; }
[ -f "$SRC" ] || { echo "statusline-conso.py doit être dans le même dossier que ce script"; exit 1; }
mkdir -p "$CFG"
cp "$SRC" "$CFG/statusline-conso.py"
python3 - "$CFG" <<'PY'
import json, os, shutil, sys, time
cfg = sys.argv[1]
p = os.path.join(cfg, "settings.json")
d = {}
if os.path.exists(p):
    d = json.load(open(p))
    shutil.copy(p, p + ".bak-" + time.strftime("%Y%m%d-%H%M%S"))
d["statusLine"] = {"type": "command", "command": 'python3 "%s"' % os.path.join(cfg, "statusline-conso.py")}
json.dump(d, open(p, "w"), indent=2)
PY
echo "OK. Relance Claude Code : la barre de conso apparaît sous la zone de saisie."
echo "(Ancien réglage sauvegardé dans $CFG/settings.json.bak-*)"
