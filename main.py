from pyscript import display, document

registration = document.querySelector("input[name='yes1']:checked").value
medical_clearance = document.querySelector("input[name='yes2']:checked").value
grade_level = document.getElementById("grade-level").value
section = document.getElementById("section").value

if grade_level == "g7" & section == "e" & registration == "yes1" & medical_clearance == "yes2": # 7-Emerald
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
elif grade_level == "g8" & section == "e" & registration == "yes1" & medical_clearance == "yes2": # 8-Emerald
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
elif grade_level == "g9" & section == "e" & registration == "yes1" & medical_clearance == "yes2": # 9-Emerald
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
elif grade_level == "g10" & section == "e" & registration == "yes1" & medical_clearance == "yes2": # 10-Emerald
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"

elif grade_level == "g7" & section == "r" & registration == "yes1" & medical_clearance == "yes2": # 7-Ruby
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
elif grade_level == "g8" & section == "r" & registration == "yes1" & medical_clearance == "yes2": # 8-Ruby
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
elif grade_level == "g9" & section == "r" & registration == "yes1" & medical_clearance == "yes2": # 9-Ruby
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
elif grade_level == "g10" & section == "r" & registration == "yes1" & medical_clearance == "yes2": # 10-Ruby
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"

elif grade_level == "g7" & section == "s" & registration == "yes1" & medical_clearance == "yes2": # 7-Sapphire
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
elif grade_level == "g8" & section == "s" & registration == "yes1" & medical_clearance == "yes2": # 8-Sapphire
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
elif grade_level == "g9" & section == "s" & registration == "yes1" & medical_clearance == "yes2": # 9-Sapphire
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
elif grade_level == "g10" & section == "s" & registration == "yes1" & medical_clearance == "yes2": # 10-Sapphire
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"

elif grade_level == "g7" & section == "t" & registration == "yes1" & medical_clearance == "yes2": # 7-Topaz
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
elif grade_level == "g8" & section == "t" & registration == "yes1" & medical_clearance == "yes2": # 8-Topaz
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
elif grade_level == "g9" & section == "t" & registration == "yes1" & medical_clearance == "yes2": # 9-Topaz
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
elif grade_level == "g10" & section == "t" & registration == "yes1" & medical_clearance == "yes2": # 10-Topaz
    document.getElementById("idname").innerHTML = "<img src='#' height='#' width='#'>"
else:
    document.getElementById("idname").innerHTML = "You are not qualified to participate in the OBMC Intramurals."