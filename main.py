from pyscript import display, document

def check_requirements(e):

    registration = document.querySelector("input[name='reg']:checked").value
    medical_clearance = document.querySelector("input[name='med']:checked").value
    grade_level = document.getElementById("grade-level").value
    section = document.getElementById("section").value

    document.getElementById("output").innerHTML = ' '
    document.getElementById("team_photo").innerHTML = ' '

    # Emerald
    if grade_level == "g7" | grade_level == "g8" | grade_level == "g9" |  grade_level == "g10" & section == "e" & registration == "yes" & medical_clearance == "yes":
        display(f"You are part of the", target='output')
        document.getElementById("team_photo").innerHTML = "<img src='green_hornets.jpeg'>"

    # Ruby
    elif grade_level == "g7" | grade_level == "g8" | grade_level == "g9" |  grade_level == "g10" & section == "r" & registration == "yes" & medical_clearance == "yes":
        display(f"You are part of the", target='output')
        document.getElementById("team_photo").innerHTML = "<img src='red_bulldogs.jpeg'>"

    # Sapphire
    elif grade_level == "g7" | grade_level == "g8" | grade_level == "g9" |  grade_level == "g10" & section == "s" & registration == "yes" & medical_clearance == "yes":
        display(f"You are part of the", target='output')
        document.getElementById("team_photo").innerHTML = "<img src='blue_bears.jpeg'>"
    
    # Topaz
    elif grade_level == "g7" | grade_level == "g8" | grade_level == "g9" |  grade_level == "g10" & section == "t" & registration == "yes" & medical_clearance == "yes":
        display(f"You are part of the", target='output')
        document.getElementById("team_photo").innerHTML = "<img src='yellow_tigers.jpeg'>"

    else:
        document.getElementById("team_photo").innerHTML = "You are not qualified to participate in the OBMC Intramurals."
