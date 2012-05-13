"Context processors for adding current sections and placements in the context."

import re

from .conf import SECTION_CONTEXT_KEY, PLACEMENTS_CONTEXT_KEY
from .models import retrieve_all_sections, Placement


def current_placements(request):
    "Match current section to request path and get related placements."
    current = None
    placements = Placement.objects.none()
    sections = retrieve_all_sections()
    for section in sections:
        pattern = re.compile(section.pattern)
        if pattern.search(request.path):
            current = section
            break
    if current:
        placements = Placement.objects.filter(sections=current).select_related('size')
    return {SECTION_CONTEXT_KEY: current, PLACEMENTS_CONTEXT_KEY: placements}
