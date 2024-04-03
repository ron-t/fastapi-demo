import string
import itertools


def seed_kv_data() -> dict:
    return {"key0": {"0": 0}}


def generate_csv_data(numrows: int, numcols: int) -> str:
    # numcols doesn't produce more columns beyond 26
    rows = range(1, numrows + 1)
    cols = list(itertools.islice(string.ascii_uppercase, numcols))

    data = [None] * len(rows)
    for row in rows:
        data[row - 1] = ",".join([f"{col}{row}" for col in cols])

    return "\n".join(data)
