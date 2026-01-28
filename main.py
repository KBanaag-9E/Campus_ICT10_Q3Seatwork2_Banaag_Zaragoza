from pyscript import display, document

registration = document.querySelector("input[name='yes1']:checked").value
medical_clearance = document.querySelector("input[name='yes2']:checked").value
grade_level = document.getElementById("grade-level").value
section = document.getElementById("section").value

def check_requirements(e):

    # Emerald
    if section == "e" & registration == "yes1" & medical_clearance == "yes2":
        display(f"You are part of the", target='output')
        document.getElementById("team_photo").innerHTML = "<img src='green_hornets.jpeg' height='#' width='#'>"

    # Ruby
    elif section == "r" & registration == "yes1" & medical_clearance == "yes2":
        display(f"You are part of the", target='output')
        document.getElementById("team_photo").innerHTML = "<img src='red_bulldogs.jpeg' height='#' width='#'>"

    # Sapphire
    elif section == "s" & registration == "yes1" & medical_clearance == "yes2":
        display(f"You are part of the", target='output')
        document.getElementById("team_photo").innerHTML = "<img src='blue_bears.jpeg' height='#' width='#'>"
    
    # Topaz
    elif section == "t" & registration == "yes1" & medical_clearance == "yes2":
        display(f"You are part of the", target='output')
        document.getElementById("team_photo").innerHTML = "<img src='yellow_tigers.jpeg' height='#' width='#'>"

    else:
        document.getElementById("team_photo").innerHTML = "You are not qualified to participate in the OBMC Intramurals."
