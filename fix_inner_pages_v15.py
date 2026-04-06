import re

src_path = "/Users/admin/Desktop/ayurhealth copy/index.html"
script_path = "/tmp/build_pages_v2.py"

with open(src_path, "r") as f:
    src_html = f.read()

# Refine footer extraction in the build script
# Currently it uses index, let's make it more robust
with open(script_path, "r") as f:
    script = f.read()

# Update the footer extraction logic in the script to include the sticky widgets
new_footer_logic = """
# Extract footer including sticky widgets
footer_idx = html.find('<!-- ===== FOOTER ===== -->')
# We take from the footer tag until just before the closing </body> or </html>
footer = html[footer_idx:] if footer_idx != -1 else ""
"""

script = re.sub(r'footer_idx = html\.find\(\'<!-- ===== FOOTER ===== -->\'\)\nfooter = html\[footer_idx:\] if footer_idx != -1 else ""', 
                new_footer_logic, script)

with open(script_path, "w") as f:
    f.write(script)

print("Updated build_pages_v2.py to include sticky widgets.")
