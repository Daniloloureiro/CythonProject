from main import circuito_RC
from main import Vc_I_Time
import timeit
circuito_RC()

execution_time = timeit.timeit(Vc_I_Time, number=10000000)
print(execution_time)