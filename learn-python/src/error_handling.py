def validate_name(name: str) -> str:
    cleaned = name.strip()

    if not cleaned:
        raise ValueError("Name cannot be empty")

    return cleaned


print(validate_name(""))
