from slug import slugify  # type: ignore[import-untyped]


def test_slugify_lowercases_and_replaces_spaces_with_dashes():
    assert slugify("Release Tracker") == "release-tracker"


def test_slugify_strips_outer_whitespace():
    assert slugify("  Payments API  ") == "payments-api"
