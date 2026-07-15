#!/usr/bin/env python3
"""Copy the template myst-imports.typ over MyST's generated file and recompile."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PATCH_DIR = ROOT / ".github" / "typst_patches"
TEMPLATE_DIR = ROOT / "typst_template"
TEMPLATE_IMPORTS = PATCH_DIR / "myst-imports.typ"
TEMPLATE_SUBPAR = PATCH_DIR / "subpar.typ"
if not TEMPLATE_IMPORTS.is_file():
    TEMPLATE_IMPORTS = TEMPLATE_DIR / "myst-imports.typ"
if not TEMPLATE_SUBPAR.is_file():
    TEMPLATE_SUBPAR = TEMPLATE_DIR / "subpar.typ"
BUILD_TEMP = ROOT / "_build" / "temp"
OUTPUT_PDF = ROOT / "exports" / "thesis.pdf"


def latest_export_dir() -> Path:
    candidates = sorted(BUILD_TEMP.glob("myst*"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not candidates:
        raise SystemExit(f"No MyST export directory found under {BUILD_TEMP}")
    return candidates[0]


def main() -> int:
    for path in (TEMPLATE_IMPORTS, TEMPLATE_SUBPAR):
        if not path.is_file():
            raise SystemExit(f"Missing template file: {path}")

    export_dir = latest_export_dir()
    for src in (TEMPLATE_IMPORTS, TEMPLATE_SUBPAR):
        target = export_dir / src.name
        target.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"Patched {target}")

    thesis_typ = export_dir / "thesis.typ"
    if not thesis_typ.is_file():
        raise SystemExit(f"Missing thesis entrypoint: {thesis_typ}")

    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["typst", "compile", str(thesis_typ), str(OUTPUT_PDF)],
        cwd=export_dir,
        check=True,
    )
    print(f"Recompiled {OUTPUT_PDF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
