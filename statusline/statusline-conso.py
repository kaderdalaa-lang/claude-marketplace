#!/usr/bin/env python3
"""Barre d'état Claude Code : conso 5h et 7 jours, en vert / rouge.

Vert  = tu consommes moins vite que le temps qui passe : tu peux accélérer.
Rouge = tu consommes plus vite que le temps (ou plus de 85 %) : ralentis.
"""
import json, os, subprocess, sys, time

G, R, D, X = "\033[32m", "\033[31m", "\033[2m", "\033[0m"
WINDOWS = (("five_hour", "5h", 5 * 3600), ("seven_day", "7j", 7 * 86400))


def bar(pct, width=8):
    n = round(max(0, min(100, pct)) / 100 * width)
    return "█" * n + "░" * (width - n)


def left(secs):
    secs = max(0, int(secs))
    if secs >= 86400:
        return f"{secs // 86400}j{secs % 86400 // 3600}h"
    if secs >= 3600:
        return f"{secs // 3600}h{secs % 3600 // 60:02d}"
    return f"{secs // 60}min"


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    limits = data.get("rate_limits") or {}
    now = time.time()
    parts, any_red = [], False
    for key, label, span in WINDOWS:
        w = limits.get(key)
        if not w or w.get("used_percentage") is None:
            continue
        used = float(w["used_percentage"])
        reset = float(w.get("resets_at") or now)
        remaining = max(0.0, reset - now)
        elapsed = max(0.0, min(100.0, (span - remaining) / span * 100))
        red = used >= 85 or used > elapsed + 10
        any_red = any_red or red
        color = R if red else G
        parts.append(f"{label} {color}{bar(used)} {used:.0f}%{X} {D}↻{left(remaining)}{X}")
    if parts:
        verdict = f"{R}▼ ralentis{X}" if any_red else f"{G}▲ accélère{X}"
        out = "  ".join(parts) + "  " + verdict
    else:
        out = f"{D}conso : pas encore de donnée (après la 1re réponse){X}"
    badge = os.path.expanduser("~/.claude/hooks/caveman-statusline.sh")
    if os.path.isfile(badge):
        try:
            b = subprocess.run(["bash", badge], input=json.dumps(data), capture_output=True, text=True, timeout=2).stdout.strip()
            if b:
                out = b + "  " + out
        except Exception:
            pass
    print(out)


main()
