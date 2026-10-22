import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from rules import has_eight
class RulesTests(unittest.TestCase):
    def test_every_valid_eight_segment(self):
        for n in (9,13,19):
            for color in (1,2):
                for dy,dx in ((0,1),(1,0),(1,1),(-1,1)):
                    for y in range(1,n+1):
                        for x in range(1,n+1):
                            if not (1<=y+7*dy<=n and 1<=x+7*dx<=n):continue
                            b=[[0]*(n+2) for _ in range(n+2)]
                            for k in range(8):b[y+k*dy][x+k*dx]=color
                            self.assertTrue(has_eight(b,n),(n,y,x,dy,dx,color))
                            b[y+3*dy][x+3*dx]=0
                            self.assertFalse(has_eight(b,n))
    def test_empty_and_border(self):
        b=[[-1]*11 for _ in range(11)]
        self.assertFalse(has_eight(b,9))
if __name__=='__main__':unittest.main()
