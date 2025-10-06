import re

# Matches proper names like:
# - John Cena
# - Anya Taylor-Joy
# - D'Angelo
# Does NOT match:
# - john cena
# - John   Cena
# - J0hn C3na
name_regex = re.compile(
    r"^[A-Z][a-z]*(?:['-]?[A-Z]?[a-z]+)*(?: [A-Z][a-z]*(?:['-]?[A-Z]?[a-z]+)*)?$"
)


# Matches valid phone formats:
# - 5555555555
# - 555-555-5555
# - (555) 555-5555
# Does NOT match:
# - 555555555 (too short)
# - 555--555--5555
# - aaaaaaaaaa
phone_regex = re.compile(
    r"^(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
)

# Matches valid email formats:
# - johncena@wwe.com
# - john.cena@wwe.com
# - john.cena123@wwe.com
# Does NOT match:
# - 123john.cena@wwe.com
# - johncena.com
# - john$cena@wwe.com
# - johncena@
email_regex = re.compile(
    r"^[A-Za-z][A-Za-z0-9\.]*@[A-Za-z]+\.[A-Za-z]{2,}$"
)
