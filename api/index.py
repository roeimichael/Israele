"""Vercel Python entrypoint. Re-exports the FastAPI app so a single serverless
function (this file) can serve every /api/* route plus /sitemap.xml — see the
top-level vercel.json rewrites. Replaces the old Railway-hosted backend.
"""
import sys
from pathlib import Path

# Repo root isn't on sys.path by default inside Vercel's function runtime;
# add it so `backend` (a plain package, not installed) is importable.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.main import app  # noqa: E402
