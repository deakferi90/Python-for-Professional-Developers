def slugify(name):
    cleaned_name = name.strip().lower()
    return cleaned_name.replace(" ", "-")


numberValue = 1

print(f"{numberValue} Python for Professional")


print(slugify("  Python for Professional Developers  "))
