#Coding challenge 2019
#Author: Glenda Lizbeth Lopez Broca

import sys
from db import session, Solutions

class SolutionQ:

    def sl(self,ld, cols, rd, nq):
        if nq == self.n:
            self.count += 1
            ansStr = [str(value) for value in self.ans]
            newSolution = Solutions(solve=','.join(ansStr))
            session.add(newSolution)
            #print(self.ans)
        valid_poss = self.all & ~(ld | cols | rd)
        while valid_poss != 0:
            current_poss = -valid_poss & valid_poss
            self.ans.append((current_poss & -current_poss).bit_length() - 1)    #store
            valid_poss ^= current_poss
            self.sl((ld | current_poss) >> 1, (cols | current_poss), (rd | current_poss) << 1, nq+1)
            self.ans.pop()
    
    def nqueens(self, n):
        self.n = n
        if n < 8:
            print ("ingrese un numero mayor o igual a 8")
        else:
            
            self.count = 0
            self.ans = []
            self.all =  (1 << n) - 1
            self.sl(0,0,0,0)
            session.commit()
            return self.count

if __name__ == "__main__":
    #n = int(sys.argv[1])
    for n in range(8, 10):
        s = SolutionQ()
        r = s.nqueens(n)
        if r:
            print (n,r)
