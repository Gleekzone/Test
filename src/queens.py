#Coding challenge 2019
#Author: Glenda Lizbeth Lopez Broca
#Problem: NQueens
#Nickname:Gleeks 

#This my python implementation of the algorithm described in the paper by Martin Richards. Ref: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.51.7113&rep=rep1&type=pdf
#The algorithm is very efficient because it takes advantage of bitwise operators.
#I found this blog post. Ref: http://gregtrowbridge.com/a-bitwise-solution-to-the-n-queens-problem-in-javascript/

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
