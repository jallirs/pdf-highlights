import os
import re
import pathlib

from jinja2 import Environment, FileSystemLoader

PATH = pathlib.Path(__file__).resolve().parent / 'templates'
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(str(PATH)),
    trim_blocks=True,
    lstrip_blocks=False
)

template = TEMPLATE_ENVIRONMENT.get_template("markdown_template.md")