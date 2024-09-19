import timeit
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do circuito
V0 = 5  # Tensão da fonte em volts
R = 1000  # Resistência em ohms (1 kΩ)
C = 0.001  # Capacitância em farads (1000 μF)

# Constante de tempo
tau = R * C

# Tempo para simulação
t = np.linspace(0, 5 * tau, 1000)  # 0 a 5 tau

# Carregamento do capacitor
Vc_charge = V0 * (1 - np.exp(-t / tau))  # Tensão no capacitor durante o carregamento
I_charge = (V0 / R) * np.exp(-t / tau)  # Corrente durante o carregamentoimport numpy aimport numpy as np
import matplotlib.pyplot as plt

# Parâmetros do circuito
V0 = 5  # Tensão da fonte em volts
R = 1000  # Resistência em ohms (1 kΩ)
C = 0.001  # Capacitância em farads (1000 μF)

# Constante de tempo
tau = R * C

# Tempo para simulação
t = np.linspace(0, 5 * tau, 1000)  # 0 a 5 tau

# Carregamento do capacitor
Vc_charge = V0 * (1 - np.exp(-t / tau))  # Tensão no capacitor durante o carregamento
I_charge = (V0 / R) * np.exp(-t / tau)  # Corrente durante o carregamento

# Descarregamento do capacitor
Vc_discharge = V0 * np.exp(-t / tau)  # Tensão no capacitor durante a descarga
I_discharge = -(V0 / R) * np.exp(-t / tau)  # Corrente durante a descarga

# Criação do gráfico
plt.figure(figsize=(12, 8))

# Parâmetros do circuito
V0 = 5  # Tensão da fonte em volts
R = 1000  # Resistência em ohms (1 kΩ)
C = 0.001  # Capacitância em farads (1000 μF)

# Constante de tempo
tau = R * C

# Tempo para simulação
t = np.linspace(0, 5 * tau, 1000)  # 0 a 5 tau

# Carregamento do capacitor
Vc_charge = V0 * (1 - np.exp(-t / tau))  # Tensão no capacitor durante o carregamento
I_charge = (V0 / R) * np.exp(-t / tau)  # Corrente durante o carregamento

# Descarregamento do capacitor
Vc_discharge = V0 * np.exp(-t / tau)  # Tensão no capacitor durante a descarga
I_discharge = -(V0 / R) * np.exp(-t / tau)  # Corrente durante a descarga

# Criação do gráfico
plt.figure(figsize=(12, 8))

# Gráfico de carregamento
plt.subplot(2, 1, 1)
plt.plot(t, Vc_charge, label='Tensão (Carregamento)', color='blue')
plt.plot(t, Vc_discharge, label='Tensão (Descarga)', color='red', linestyle='--')
plt.title('Circuito RC - Carregamento e Descarregamento do Capacitor')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.legend()
plt.grid()

# Gráfico de corrente
plt.subplot(2, 1, 2)
plt.plot(t, I_charge, label='Corrente (Carregamento)', color='green')
plt.plot(t, I_discharge, label='Corrente (Descarga)', color='orange', linestyle='--')
plt.xlabel('Tempo (s)')
plt.ylabel('Corrente (A)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
# Gráfico de carregamento
plt.subplot(2, 1, 1)
plt.plot(t, Vc_charge, label='Tensão (Carregamento)', color='blue')
plt.plot(t, Vc_discharge, label='Tensão (Descarga)', color='red', linestyle='--')
plt.title('Circuito RC - Carregamento e Descarregamento do Capacitor')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.legend()
plt.grid()

# Gráfico de corrente
plt.subplot(2, 1, 2)
plt.plot(t, I_charge, label='Corrente (Carregamento)', color='green')
plt.plot(t, I_discharge, label='Corrente (Descarga)', color='orange', linestyle='--')
plt.xlabel('Tempo (s)')
plt.ylabel('Corrente (A)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

def Vc_I_Time_py(n_points=100):
    V0 = 5.0
    R = 1000.0
    C = 0.001
    tau = R * C
    t_max = 5 * tau
    
    result = np.empty(n_points)
    
    step = t_max / (n_points - 1)
    
    for i in range(n_points):
        t = i * step
        exp_val = np.exp(-t / tau)
        result[i] = V0 * V0 * exp_val * exp_val / R
    
    return result



execution_time2 = timeit.timeit(lambda: Vc_I_Time_py(100), number=100)
print(f"Execution time: {execution_time2} seconds")