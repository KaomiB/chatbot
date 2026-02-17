"""
PDF to Markdown ingestion for RAG.
Reads PDFs from a folder, writes Markdown under docs/ (e.g. docs/from_pdf/).
Output is then indexed by the same memory_builder used for hand-written Markdown.
"""
from __future__ import annotations

import sys
from pathlib import Path

from config import DOCS_DIR

# Default: PDFs in project root or a pdfs/ folder; output under docs/from_pdf/
DEFAULT_PDF_DIR = Path(__file__).resolve().parent.parent / "pdfs"
DEFAULT_OUTPUT_DIR = DOCS_DIR / "from_pdf"


def pdf_to_markdown_text(pdf_path: Path) -> str:
    """Extract text from a PDF and return a markdown-friendly string (with ## Page N sections)."""
    try:
        import pymupdf
    except ImportError:
        raise ImportError("Install pymupdf: pip install pymupdf") from None

    parts = []
    with pymupdf.open(pdf_path) as doc:
        for i, page in enumerate(doc):
            text = page.get_text().strip()
            if text:
                parts.append(f"## Page {i + 1}\n\n{text}")
    return "\n\n".join(parts) if parts else ""


def ingest_pdfs(
    pdf_dir: Path | None = None,
    output_dir: Path | None = None,
) -> list[Path]:
    """
    Find all PDFs in pdf_dir, convert to Markdown, write to output_dir.
    Returns list of written .md paths.
    """
    pdf_dir = pdf_dir or DEFAULT_PDF_DIR
    output_dir = output_dir or DEFAULT_OUTPUT_DIR
    pdf_dir = Path(pdf_dir)
    output_dir = Path(output_dir)

    if not pdf_dir.exists():
        print(f"PDF directory does not exist: {pdf_dir}", file=sys.stderr)
        return []

    output_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for pdf_path in sorted(pdf_dir.glob("*.pdf")):
        try:
            md_content = pdf_to_markdown_text(pdf_path)
            out_path = output_dir / f"{pdf_path.stem}.md"
            out_path.write_text(md_content, encoding="utf-8")
            written.append(out_path)
            print(f"Wrote {out_path}")
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}", file=sys.stderr)
    return written


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser(description="Convert PDFs to Markdown under docs/from_pdf/")
    ap.add_argument("--pdf-dir", type=Path, default=DEFAULT_PDF_DIR, help="Folder containing PDFs")
    ap.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Output folder for .md files")
    args = ap.parse_args()
    written = ingest_pdfs(pdf_dir=args.pdf_dir, output_dir=args.output_dir)
    print(f"Converted {len(written)} PDF(s). Run memory_builder to index docs/.")
    sys.exit(0 if written or not (args.pdf_dir.exists()) else 1)


if __name__ == "__main__":
    main()
