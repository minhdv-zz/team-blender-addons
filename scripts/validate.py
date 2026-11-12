#!/usr/bin/env python3
"""Validate community contributions to team-blender-addons. Exit code 1 if anything blocks merging.

Each folder in addons/ must:
  - contain __init__.py (legacy addon) or blender_manifest.toml (extension)
  - contain a license file (LICENSE, LICENSE.md, LICENSE.txt, COPYING)
  - name its author: bl_info['author'] in __init__.py, or maintainer = "..." in blender_manifest.toml
  - have no file over 25 MB
  - contain no obvious secrets
Warnings (a human must look): compiled binaries (.dll, .pyd, .so, .exe) and bundled installers.
"""
import ast
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADDONS = os.path.join(ROOT, "addons")
MAX_FILE_BYTES = 25 * 1024 * 1024
BINARY_EXT = {".dll", ".pyd", ".so", ".dylib", ".exe", ".msi", ".bat", ".cmd"}
LICENSE_NAMES = {"license", "license.md", "license.txt", "copying", "copying.md", "copying.txt"}
SECRET_PATTERNS = [
    (r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----", "private key"),
    (r"\bghp_[A-Za-z0-9]{30,}\b", "GitHub token"),
    (r"\bgithub_pat_[A-Za-z0-9_]{30,}\b", "GitHub token"),
    (r"\bsk-[A-Za-z0-9_\-]{32,}\b", "API key (sk-...)"),
    (r"\bAKIA[0-9A-Z]{16}\b", "AWS access key"),
    (r"\bAIza[0-9A-Za-z_\-]{35}\b", "Google API key"),
    (r"(?i)\b(?:password|passwd|secret|api[_-]?key|token)\s*[:=]\s*['\"][^'\"\s]{12,}['\"]", "hard-coded credential"),
]
TEXT_EXT = {".py", ".md", ".txt", ".json", ".toml", ".cfg", ".ini", ".yml", ".yaml", ".xml"}

errors, warnings = [], []


def err(m):
    errors.append(m)
    print("::error::" + m)


def warn(m):
    warnings.append(m)
    print("::warning::" + m)


def find_author(base):
    init = os.path.join(base, "__init__.py")
    if os.path.isfile(init):
        try:
            with open(init, encoding="utf-8", errors="replace") as f:
                tree = ast.parse(f.read())
            for node in tree.body:
                if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "bl_info" for t in node.targets):
                    info = ast.literal_eval(node.value)
                    if str(info.get("author", "")).strip():
                        return True
        except Exception:  # noqa: BLE001
            pass
    mf = os.path.join(base, "blender_manifest.toml")
    if os.path.isfile(mf):
        with open(mf, encoding="utf-8", errors="replace") as f:
            if re.search(r'(?m)^(?:maintainer|author)\s*=\s*"[^"]+"', f.read()):
                return True
    return False


def check(name):
    base = os.path.join(ADDONS, name)
    rel = f"addons/{name}"
    if not re.match(r"^[A-Za-z0-9][A-Za-z0-9_\-]{1,63}$", name):
        err(f"{rel}: folder name must be 2-64 chars of letters, digits, '-' or '_'")
    if not (os.path.isfile(os.path.join(base, "__init__.py")) or os.path.isfile(os.path.join(base, "blender_manifest.toml"))):
        err(f"{rel}: needs __init__.py or blender_manifest.toml at the top of the folder")
    if not find_author(base):
        err(f"{rel}: name the author so everyone knows whose addon this is (bl_info 'author' or maintainer in blender_manifest.toml)")
    if not any(f.lower() in LICENSE_NAMES for f in os.listdir(base)):
        err(f"{rel}: add the addon's license file (LICENSE). Only freely redistributable addons are accepted")
    for dp, dn, fn in os.walk(base):
        dn[:] = [d for d in dn if d not in (".git", "__pycache__")]
        for f in fn:
            full = os.path.join(dp, f)
            r = os.path.relpath(full, ROOT).replace(os.sep, "/")
            ext = os.path.splitext(f)[1].lower()
            size = os.path.getsize(full)
            if size > MAX_FILE_BYTES:
                err(f"{r}: {size / 1e6:.1f} MB is over the {MAX_FILE_BYTES // 1024 // 1024} MB limit")
            if ext in BINARY_EXT:
                warn(f"{r}: compiled/binary file, the reviewer must verify where it comes from")
            if ext in TEXT_EXT and size <= MAX_FILE_BYTES:
                with open(full, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
                for pat, label in SECRET_PATTERNS:
                    if re.search(pat, text):
                        err(f"{r}: looks like it contains a {label}. Remove it before merging")


def main():
    if not os.path.isdir(ADDONS):
        err("addons/ folder not found")
    else:
        for name in sorted(os.listdir(ADDONS)):
            if os.path.isdir(os.path.join(ADDONS, name)):
                check(name)
    print(f"\nvalidate: {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
