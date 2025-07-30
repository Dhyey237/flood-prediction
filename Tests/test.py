import unittest
from app.predictor import predict_risk

class TestFloodRisk(unittest.TestCase):
    def test_high_risk(self):
        self.assertEqual(predict_risk(1.0, 0.9), "High")

    def test_low_risk(self):
        self.assertEqual(predict_risk(0.1, 0.1), "Low")

if __name__ == '__main__':
    unittest.main()
