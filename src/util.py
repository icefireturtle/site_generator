def props_to_html(props):
    if props == None:
        return ""
    dict_string = ""
    for key, value in props.items():
        dict_string += f' {key}="{value}"'
    return dict_string