import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
            a1=np.array(a)
            a2=np.array(b)
            if a1.shape[1] != a2.shape[0]:
                return -1
            c=a1 @ a2

            return c.tolist()