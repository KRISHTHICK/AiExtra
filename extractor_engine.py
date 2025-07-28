def extract_data(elements, approved_pattern):
    extracted = []
    for el in elements:
        if el['style'] == approved_pattern['most_common_style'][0]:
            extracted.append(el)
        elif el['text'] in approved_pattern['box_like_values']:
            extracted.append(el)
    return extracted
