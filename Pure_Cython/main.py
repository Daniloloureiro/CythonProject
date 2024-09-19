from main import circuito_RC
from main import Vc_I_Time_cy
import timeit
circuito_RC()



execution_time2 = timeit.timeit(lambda: Vc_I_Time_cy(100), number=100)
print(f"Execution time: {execution_time2} seconds")