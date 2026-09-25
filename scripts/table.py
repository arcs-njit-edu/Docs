
import os
import re

import pandas as pd

DOCS_DIR = "docs"
TABLES_DIR = os.path.join(DOCS_DIR, "assets", "tables", "trainings")

LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
SKIP_PREFIXES = ("../", "./", "/", "#", "http://", "https://", "mailto:")


def _resolve_link(match, depth):
    target = match.group(1)
    if target.startswith(SKIP_PREFIXES):
        return match.group(0)
    path = target.split("#", 1)[0]
    if not os.path.exists(os.path.join(DOCS_DIR, path)):
        return match.group(0)
    return "](" + "../" * depth + target + ")"


def _fix_cell(s, depth):
    if not isinstance(s, str):
        return s
    s = LINK_RE.sub(lambda m: _resolve_link(m, depth), s)
    s = re.sub(r'(\()([^)]*?)index\.md', r'\1\2', s)
    s = re.sub(r'(\b6_[\w\-.]+)\.md\b', r'\1', s)
    s = s.replace('(//', '(/')
    return s


def render(csv_name, depth):
    df = pd.read_csv(os.path.join(TABLES_DIR, csv_name), keep_default_na=False)
    df = df.map(lambda s: _fix_cell(s, depth))
    return df.to_markdown(index=False)
