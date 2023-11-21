import difflib

router_names = ['sa-lab-4431a', 'sa-lab-2921c']  # Replace with router names obtained from inventory

for router_name in router_names:
    show_version_A = f"show_version_{router_name}_A.txt"
    show_version_B = f"show_version_{router_name}_B.txt"
    show_run_A = f"show_run_{router_name}_A.txt"
    show_run_B = f"show_run_{router_name}_B.txt"

    with open(show_version_A) as f:
        show_version_A_lines = f.readlines()
    with open(show_version_B) as f:
        show_version_B_lines = f.readlines()
    diff_show_version = difflib.HtmlDiff().make_file(show_version_A_lines, show_version_B_lines)

    with open(show_run_A) as f:
        show_run_A_lines = f.readlines()
    with open(show_run_B) as f:
        show_run_B_lines = f.readlines()
    diff_show_run = difflib.HtmlDiff().make_file(show_run_A_lines, show_run_B_lines)

    # Generate HTML reports or perform other comparison logic as needed
    # For example:
    with open(f"{router_name}_show_version_diff.html", "w") as f:
        f.write(diff_show_version)
    with open(f"{router_name}_show_run_diff.html", "w") as f:
        f.write(diff_show_run)

print("All comparison tasks completed successfully! Have a wonderful day!")
