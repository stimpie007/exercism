def proverb(*objs, qualifier=""):
    lines = [f"For want of a {w} the {l} was lost." for w, l in zip(objs, objs[1:])]
    qual = "" if not (objs and qualifier) else f"{qualifier} "
    return [] if not objs else lines + [f"And all for the want of a {qual}{objs[0]}."]
