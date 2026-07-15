#!/usr/bin/env python3
"""Patch upstream Typst template TOC styling during CI."""
from pathlib import Path

path = Path("typst_template/src/layout/frontmatter.typ")
text = path.read_text()

patched = """// Table of contents.
#let render_table_of_contents(depth: 1) = {
  pagebreak()
  {
    show outline.entry.where(level: 1): it => {
      v(1.2em, weak: true)
      strong(it)
    }
    outline(
      title: strong("Contents"),
      depth: depth,
      indent: auto,
    )
  }
}"""

plain = """// Table of contents.
#let render_table_of_contents(depth: 1) = {
  pagebreak()
  outline(
    title: strong("Contents"),
    depth: depth,
    indent: auto,
  )
}"""

legacy = """// Table of contents.
#let render_table_of_contents(depth: 1) = {
  pagebreak()
  {
    show outline.entry.where(level: 1): set text(weight: "bold")
    show outline.entry.where(level: 1): set block(above: 1em)
    outline(
      title: strong("Contents"),
      depth: depth,
      indent: auto,
    )
  }
}"""

if patched in text:
    print("TOC styling already patched")
elif plain in text:
    path.write_text(text.replace(plain, patched))
    print("Applied TOC styling patch to upstream template")
elif legacy in text:
    path.write_text(text.replace(legacy, patched))
    print("Upgraded legacy TOC styling patch")
else:
    raise SystemExit("Could not find render_table_of_contents block to patch")
