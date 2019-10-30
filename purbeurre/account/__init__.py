import re


string = "olivier@mailbidon.com"
regexp = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"

if re.match(regexp, string) is not None:
    print("TRUE")
else:
    print("FALSE")