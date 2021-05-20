import urllib.request
import hashlib
import sys

url = "https://github.com/mateusza2/2020-nlo-inf/raw/master/2021-05-20-sprawdzian/kandydaci.db"
out = "kandydaci.db"
hashes = {
    "sha1":     "d37f3ed5f87fef2ad158c5b133f113c73595228e",
    "md5":      "f18884b5d7a340eca7200640f1eca687"
}

with urllib.request.urlopen(url) as remote_file:
    print(f"Pobieranie pliku z {url}")
    data = remote_file.read()
    print(f"Pobrano: {len(data)}B")

for hash_name, hash_value in hashes.items():
    hash_func = getattr(hashlib, hash_name)
    hash_value_calc = hash_func(data).hexdigest()
    print(f"Sprawdzam {hash_name}: ", end="")
    if hash_value_calc != hash_value:
        print(f"Błąd. {hash_value} vs {hash_value_calc}")
        sys.exit(1)
    print(f"OK {hash_value}")

with open(out, "wb") as local_file:
    print(f"Zapisano: {out}")
    local_file.write(data)

