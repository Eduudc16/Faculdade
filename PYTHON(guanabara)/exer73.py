times =("Flamengo","Palmeiras","Cruzeiro",
    "Bahia","Botafogo","Mirassol","São Paulo",
    "Fluminense","Red Bull Bragantino",
    "Ceará","Atlético Mineiro",
    "Internacional","Grêmio",
    "Corinthians","Santos","Vasco da Gama",
    "Vitória","Juventude"
)

ordem = sorted(times)

print(times[0:5])
print(times[13:])
print(ordem)
print(f'o time do Grêmio está {times.index ("Grêmio")} na posição')