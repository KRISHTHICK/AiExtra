from collections import Counter
import re

def detect_common_patterns(elements):
    style_counts = Counter([el['style'] for el in elements])
    font_sizes = Counter([el.get('font_size') for el in elements if el.get('font_size')])

    patterns = {
        'most_common_style': style_counts.most_common(1)[0],
        'common_font_size': font_sizes.most_common(1)[0],
        'box_like_values': [el['text'] for el in elements if re.search(r'\d+\.\d+', el['text'])],
    }
    return patterns
