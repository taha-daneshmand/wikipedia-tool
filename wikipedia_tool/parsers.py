#!/usr/bin/env python
import re
from typing import List, Dict, Optional

class Section:
    """
    Represents a section of a Wikipedia article.

    Attributes:
        title (str): The title of the section.
        content (str): The raw content of the section.
        subsections (List[Section]): A list of subsections within the section.
    """
    def __init__(self, title: str, content: str, subsections: Optional[List["Section"]] = None) -> None:
        self.title = title
        self.content = content
        self.subsections = subsections if subsections is not None else []

    def __repr__(self) -> str:
        return f"Section(title={self.title!r}, content_length={len(self.content)}, subsections={len(self.subsections)})"


def parse_sections(wikitext: str) -> List[Section]:
    """
    Parse the wikitext of a Wikipedia page into a hierarchical structure of sections.

    The function identifies section headings based on equal signs (e.g., == Section ==)
    and organizes content accordingly into a tree of Section objects.

    Args:
        wikitext (str): The raw wikitext of a Wikipedia article.

    Returns:
        List[Section]: A list of top-level Section objects representing the article's sections.
    """
    heading_pattern = re.compile(r'^(={2,6})\s*(.*?)\s*\1\s*$', re.MULTILINE)
    headings = list(heading_pattern.finditer(wikitext))
    sections = []
    if not headings:
        sections.append(Section(title="Introduction", content=wikitext.strip()))
        return sections

    stack = []
    last_index = 0
    for match in headings:
        level = len(match.group(1))
        title = match.group(2)
        start_index = match.start()
        if last_index < start_index:
            content = wikitext[last_index:start_index].strip()
            if stack:
                stack[-1][1].subsections.append(Section(title="", content=content))
            else:
                sections.append(Section(title="Introduction", content=content))
        current_section = Section(title=title, content="")
        current_section.start_index = match.end()
        while stack and stack[-1][0] >= level:
            _, sec = stack.pop()
            sec.content = wikitext[sec.start_index:match.start()].strip()
        if stack:
            stack[-1][1].subsections.append(current_section)
        else:
            sections.append(current_section)
        stack.append((level, current_section))
        last_index = match.end()
    if last_index < len(wikitext):
        remaining = wikitext[last_index:].strip()
        if stack:
            stack[-1][1].content += "\n" + remaining
        else:
            sections.append(Section(title="Introduction", content=remaining))
    for _, sec in stack:
        if hasattr(sec, "start_index"):
            del sec.start_index
    return sections


def parse_infobox(wikitext: str) -> Dict[str, str]:
    """
    Extract and parse the infobox from the wikitext of a Wikipedia page.

    The function identifies an infobox template and extracts key-value pairs contained within it.
    It returns a dictionary where keys are the infobox parameter names and values are their corresponding values.

    Args:
        wikitext (str): The raw wikitext of a Wikipedia article.

    Returns:
        Dict[str, str]: A dictionary of infobox parameters and their values.
    """
    infobox_pattern = re.compile(r'\{\{Infobox(.*?)\n\}\}', re.DOTALL | re.IGNORECASE)
    match = infobox_pattern.search(wikitext)
    if not match:
        return {}
    infobox_content = match.group(1)
    param_pattern = re.compile(r'\|\s*(\w+)\s*=\s*(.*?)\n(?=\||$)', re.DOTALL)
    params = {}
    for param_match in param_pattern.finditer(infobox_content):
        key = param_match.group(1).strip()
        value = param_match.group(2).strip()
        params[key] = value
    return params


def parse_links(wikitext: str) -> List[str]:
    """
    Extract all internal wiki links from the wikitext.

    The function searches for patterns like [[Link]] or [[Link|Display Text]]
    and returns a list of link targets.

    Args:
        wikitext (str): The raw wikitext of a Wikipedia article.

    Returns:
        List[str]: A list of internal link targets.
    """
    link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
    return [match.group(1).strip() for match in link_pattern.finditer(wikitext)]


def clean_wikitext(wikitext: str) -> str:
    """
    Clean the wikitext by removing basic markup elements and return plain text.

    This function removes templates, file links, and wiki formatting symbols,
    providing a rough plain text version of the content.

    Args:
        wikitext (str): The raw wikitext of a Wikipedia article.

    Returns:
        str: The cleaned plain text.
    """
    text = re.sub(r'\{\{.*?\}\}', '', wikitext, flags=re.DOTALL)
    text = re.sub(r'\[\[File:[^\]]+\]\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\[\[(?:[^\]|]+\|)?([^\]]+)\]\]', r'\1', text)
    text = re.sub(r"'''(.*?)'''", r'\1', text)
    text = re.sub(r"''(.*?)''", r'\1', text)
    return text.strip()


def parse_references(wikitext: str) -> List[str]:
    """
    Extract references from the wikitext of a Wikipedia page.

    The function searches for <ref>...</ref> tags and returns a list of reference contents.

    Args:
        wikitext (str): The raw wikitext of a Wikipedia article.

    Returns:
        List[str]: A list of references extracted from the text.
    """
    ref_pattern = re.compile(r'<ref[^>]*>(.*?)</ref>', re.DOTALL | re.IGNORECASE)
    return [ref.strip() for ref in ref_pattern.findall(wikitext)]


def parse_templates(wikitext: str) -> List[str]:
    """
    Extract all templates from the wikitext.

    Templates are identified by {{...}} syntax. This function returns a list of template contents.

    Args:
        wikitext (str): The raw wikitext of a Wikipedia article.

    Returns:
        List[str]: A list of template contents.
    """
    template_pattern = re.compile(r'\{\{(.*?)\}\}', re.DOTALL)
    return [tpl.strip() for tpl in template_pattern.findall(wikitext)]
