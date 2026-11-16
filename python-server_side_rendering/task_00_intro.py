#!/usr/bin/python3

def generate_invitations(template, attendees):
    """Generates invitation files from template and list of attendees."""

    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: attendees must be a list.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        placeholders = [
            "name",
            "event_title",
            "event_date",
            "event_location"
        ]

        for key in placeholders:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            invitation = invitation.replace(
                "{" + key + "}",
                str(value)
            )

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing {filename}: {e}")
