# String and Slicing


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value

print(repr(to_str(b"foo")))
print(repr(to_str("bar")))


key = "my_var"
value = 1.234


old_way = "%-10s = %.2f" % (key, value)

new_way= "%(key)-10s = %(value).2f" %{
    "key": key,
    "value": value
}


new_template = (
    "Today's soup is {soup}, "
    "buy one get two {oyster} oysters, "
    "and our special entrée is {special}."
)
new_formatted = new_template.format(
    soup="lentil",
    oyster="kumamoto",
    special="schnitzel",
)


# Understand the Difference Between repr and str when Printing Objects

# __repr__ is similar to ToString()