import unittest
from app import create_app, db
from app.models.medicine import Medicine

class MedicineModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_medicine_creation(self):
        medicine = Medicine(name='Aspirin', dosage='500mg')
        db.session.add(medicine)
        db.session.commit()
        self.assertEqual(medicine.name, 'Aspirin')
        self.assertEqual(medicine.dosage, '500mg')

    def test_medicine_str(self):
        medicine = Medicine(name='Ibuprofen', dosage='200mg')
        self.assertEqual(str(medicine), 'Ibuprofen')

if __name__ == '__main__':
    unittest.main()