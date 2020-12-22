REQUIRED_FIELDS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]

def get_passports():
    with open('input.txt') as f:
        passport = {} 
        for line in f:
            line = line.strip()
            if not line:
                if passport:
                    yield passport
                passport = {}
            else:
                parts = line.split(" ")
                pairs = [part.split(":") for part in parts]
                passport.update(dict(pairs))
        if passport:
            yield passport


def validate_passport(passport, required_fields=REQUIRED_FIELDS):
    for field in required_fields:
        if field not in passport:
            return False
    return True

def get_valid_passports(passports):
    for passport in passports:
        if validate_passport(passport):
            yield passport

valid_passports = list(get_valid_passports(get_passports()))

print(f"Number of valid passports: {len(valid_passports)}")