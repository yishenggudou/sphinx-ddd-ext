"""
sphinx-ddd-ext

some ddd tools for desgin ddd app
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__version__ = "0.1"


def setup(app: Sphinx) -> dict[str, Any]:
    return {"version": __version__, "parallel_read_safe": True}
