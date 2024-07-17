def generate_invitations(template, attendees):
    def replace_placeholder(text, placeholder, value):
        return text.replace(placeholder, str(value) if value is not None else "N/A")

    if not isinstance(template, str):
        print("Invalid input type for template")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Invalid input type for attendees")
        return
    
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        personal_invitation = template
        personal_invitation = replace_placeholder(personal_invitation, "{name}", attendee.get("name"))
        personal_invitation = replace_placeholder(personal_invitation, "{event_title}", attendee.get("event_title"))
        personal_invitation = replace_placeholder(personal_invitation, "{event_date}", attendee.get("event_date"))
        personal_invitation = replace_placeholder(personal_invitation, "{event_location}", attendee.get("event_location"))
        
        filename = f"output_{index}.txt"

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(personal_invitation)