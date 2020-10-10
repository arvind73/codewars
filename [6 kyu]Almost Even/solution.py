def split_integer(num, parts):
    quo, rem = divmod(num, parts)
    if rem == 0:
        return [quo] * parts
    return [quo if a > rem else quo + 1 for a in range(parts, 0, -1)]
