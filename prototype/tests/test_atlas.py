import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from atlas import CATALOG, RELATIONS, BudgetExceeded, f_exact, f3_residue_heuristic, summarize
from math import factorial

class AtlasTests(unittest.TestCase):
    def test_catalog(self):
        d=json.loads(CATALOG.read_text())
        ids=[x['id'] for x in d['entries']]
        self.assertEqual(len(ids),len(set(ids)))
        by_id={x['id']:x for x in d['entries']}
        self.assertEqual(int(by_id['deck-52']['claims'][0]['value']), factorial(52))

    def test_proved_bounds(self):
        r=json.loads(RELATIONS.read_text())['relations']
        self.assertEqual(len(r),5)
        self.assertTrue(all(x['status']=='proved_bound' for x in r))
        self.assertLess(2048,factorial(52))
        self.assertLess(factorial(52),10**100)
        self.assertGreater(160*(2**160),10**50)

    def test_fgh_small(self):
        self.assertEqual(f_exact(0,3),4)
        self.assertEqual(f_exact(1,3),6)
        self.assertEqual(f_exact(2,3),24)
        self.assertEqual(f_exact(3,2),2048)
        self.assertEqual(summarize('omega',5)['reduction'],'F_5(5)')

    def test_exact_budget(self):
        with self.assertRaises(BudgetExceeded):
            f_exact(3,3,max_bits=10000)

    def test_log_estimation(self):
        # These tests verify only an explicitly heuristic method's stability.
        expected={5:1.69764, 6:2.07062, 50:16.22908, 2048:619.29937}
        for n,v in expected.items():
            d=f3_residue_heuristic(n)
            self.assertEqual(d['status'],'heuristic')
            self.assertAlmostEqual(float(d['residue_estimate']),v,places=4)

if __name__ == '__main__':
    unittest.main()
