def get_formatted_name(f_name, l_name, m_name=""):
    if m_name:
        return f"{f_name.title()} {m_name.title()} {l_name.title()}"
    else:
        return f"{f_name.title()} {l_name.title()}"
