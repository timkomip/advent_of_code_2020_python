
class BasicValidation():
    REQUIRED_FIELDS = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]
    def validate(self, passport):
        return all(field in passport for field in self.REQUIRED_FIELDS)

class StrictValidation(BasicValidation):
    def validate(self, passport):
        valid = super().validate(passport)

        byr = passport.get('byr', '')
        valid = valid and self._validate_year(byr, 1920, 2002)

        iyr = passport.get('iyr', '')
        valid = valid and self._validate_year(iyr, 2010, 2020)

        eyr = passport.get('eyr', '')
        valid = valid and self._validate_year(eyr, 2020, 2030)
        
        hgt = passport.get('hgt', '')
        valid = valid and self._validate_height(hgt)

        return valid
    
    def _validate_year(self, value, min, max):
        return value.isnumeric() and min <= int(value) <= max
    
    def _validate_height(self, hgt):
        # TODO
        pass

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


def get_valid_passports(passports, strategy):
    for passport in passports:
        if strategy.validate(passport):
            yield passport

valid_passports = list(get_valid_passports(get_passports(), BasicValidation()))

print(f"Number of valid passports: {len(valid_passports)}")

valid_passports = list(get_valid_passports(get_passports(), StrictValidation()))

print(f"Number of valid passports using strict rules: {len(valid_passports)}")