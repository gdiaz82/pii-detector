import re
import json
from typing import List, Dict

class RegexPIIDetector:
    def __init__(self):
        self.patterns = {
            'email': r'\b[A-Za-z0-9._%-+]+@[A-Za-z0-9._%-+]+\.[A-Za-z]{2,}\b',
            'phone': r'(?:\+\d{1,3}[\s-]?)?(?:\(\d{1,4}\)[\s-]?)?\d{6,14}\b',
            'credit_card': r'(?<!\d)\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}(?!\d)',
            'rut': r'\b\d{1,2}\.?\d{3}\.?\d{3}-[kK0-9]\b',
            'name_context': r'(?:nombre|señor|señora)[:\s]+([A-Za-záéíóúñÑ\s]{2,})',
            'address_context': r'(?:dirección|calle|avenida)[:\s]+([A-Za-z0-9\s,.#-]+)'
        }

    def detect(self, text: str):
        results = []
        
        for pii_type, pattern in self.patterns.items():
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                if 'context' in pii_type and match.lastindex:
                    value = match.group(1).strip()
                    start, end = match.start(1), match.end(1)
                else:
                    value = match.group()
                    start, end = match.start(), match.end()
                
                if value:
                    results.append({
                        'type': pii_type,
                        'value': value,
                        'start': start,
                        'end': end,
                        'method': 'regex'
                    })
        
        return results