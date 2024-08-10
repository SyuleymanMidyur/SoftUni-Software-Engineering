class DVD:
    def __init__(self, name: str, _id: int, creation_year: int, creation_mount: str, age_restriction: int):
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_mount = creation_mount
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, _id: int, name: str, date: str, age_restriction: int):
        day, mount, year = date.split('.')