#!/usr/bin/env python3
"""The World in One Page — Saturday Edition (21 November 2026).

Small entry script: verifies the entry files are present, prints the
entry summary, and can serve the front page locally for inspection.

Usage:
    python3 main.py            # check files + print summary
    python3 main.py --serve    # serve this directory on http://127.0.0.1:8132
"""
import argparse
import http.server
import socketserver
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = ["frontpage.html", "entry.png", "README.md", "SOURCES.md",
         "LICENSE", ".makefun/owner.json", "tools/render.py", "main.py"]


def check():
    missing = [f for f in FILES if not (ROOT / f).exists()]
    size = (ROOT / "entry.png").stat().st_size if (ROOT / "entry.png").exists() else 0
    print("The World in One Page — Saturday Edition")
    print("Competition: news-image-20261121 (make.fun)")
    print("Date covered: Saturday 21 November 2026")
    print(f"Stories: 50 (16 drawn, 34 briefs) across 7 regions")
    if missing:
        print("MISSING:", ", ".join(missing))
        return 1
    print(f"All {len(FILES)} entry files present; entry.png = {size} bytes")
    return 0


def serve():
    os.chdir(ROOT)
    with socketserver.TCPServer(("127.0.0.1", 8132),
                                http.server.SimpleHTTPRequestHandler) as httpd:
        print("Serving at http://127.0.0.1:8132/frontpage.html")
        httpd.serve_forever()


if __name__ == "__main__":
    import os
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true")
    args = ap.parse_args()
    raise SystemExit(serve() if args.serve else check())
