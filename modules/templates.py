def load_prompt(template_path: str, user_query: str) -> str:
    with open(template_path, 'r') as file:
        template = file.read()
    return template.replace("{query}", user_query)
