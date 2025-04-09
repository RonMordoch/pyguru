from enum import StrEnum


class ElementType(StrEnum):
    EXCEL = 'excel'
    TEXT = 'text'
    FORM = 'form'
    ATTACHMENTS = 'attachments'
    SAMPLES = 'samples'
    PLATE = 'plate'
    STEPS = 'steps'
    EQUIPMENT = 'equipment'
    SKETCH = 'sketch'
    COMPOUND = 'compound'
    REACTION = 'reaction'
    PDF = 'pdf'
