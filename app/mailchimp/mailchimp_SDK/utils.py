def parse_mailchimp_contacts(members: list) -> list:
    filtered = []

    for member in members:
        email = member.get("email_address")
        merge = member.get("merge_fields", {})
        first_name = merge.get("FNAME")
        last_name = merge.get("LNAME")

        if email and first_name and last_name:
            filtered.append({
                "first_name": first_name,
                "last_name": last_name,
                "email": email
            })

    return filtered