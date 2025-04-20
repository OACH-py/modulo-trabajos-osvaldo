grados = float(input("Ingresa los grados decimales: "))
g = int(grados)
m_d = (grados - g) * 60
m = int(m_d)
seg = (m_d - m) * 60
print(f"{g}° {m}' {seg:.2f}''")