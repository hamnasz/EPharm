class Medicine:
    def __init__(self, id, name, dosage):
        self.id = id
        self.name = name
        self.dosage = dosage

    def __repr__(self):
        return f"<Medicine {self.name}, Dosage: {self.dosage}>"

    # Additional methods for medicine-related operations can be added here
    def update_dosage(self, new_dosage):
        self.dosage = new_dosage

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "dosage": self.dosage
        }