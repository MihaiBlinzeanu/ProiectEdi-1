#!/usr/bin/env python3
"""AIASSIST RAG — CLI unificat pentru interogarea cursurilor."""

import sys
sys.stdout.reconfigure(encoding="utf-8")

import os
import argparse

PYTHON = sys.executable
SCRIPTS = os.path.join(os.path.dirname(__file__), "scripts")


def main():
    parser = argparse.ArgumentParser(
        description="AIASSIST RAG — Întreabă cursurile tale"
    )
    sub = parser.add_subparsers(dest="command")

    ask = sub.add_parser("ask", help="Pune o întrebare (RAG)")
    ask.add_argument("query", nargs="+", help="Întrebarea ta")

    search = sub.add_parser("search", help="Caută fragmente relevante")
    search.add_argument("query", nargs="+", help="Termenii de căutare")

    ingest = sub.add_parser("ingest", help="Parsează PDF-urile din inbox/")
    reindex = sub.add_parser("reindex", help="Re-indexează embeddings (după ingest)")

    args = parser.parse_args()

    if args.command == "ask":
        query = " ".join(args.query)
        script = os.path.join(SCRIPTS, "generate.py")
        os.execv(PYTHON, [PYTHON, script, query])

    elif args.command == "search":
        query = " ".join(args.query)
        script = os.path.join(SCRIPTS, "search.py")
        os.execv(PYTHON, [PYTHON, script, query])

    elif args.command == "ingest":
        script = os.path.join(SCRIPTS, "ingest.py")
        os.execv(PYTHON, [PYTHON, script])

    elif args.command == "reindex":
        script = os.path.join(SCRIPTS, "chunk_embed.py")
        os.execv(PYTHON, [PYTHON, script])

    else:
        parser.print_help()


if __name__ == "__main__":
    main()