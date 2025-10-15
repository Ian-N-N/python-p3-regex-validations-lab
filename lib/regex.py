import re

# Name regex
name_regex = re.compile(r"^[A-Z][a-z]*(?:[ '-][A-Z][a-z]*)*$")

# Phone regex
phone_regex = re.compile(r"^(?:\(\d{3}\)\s?|\d{3}[-.]?)\d{3}[-.]?\d{4}$")

# Email regex
email_regex = re.compile(r"^[a-zA-Z][\w\.]*@[a-zA-Z]+\.[a-zA-Z]{2,}$")

