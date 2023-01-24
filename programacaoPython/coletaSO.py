import psutil

#coleta de informações da memória
memoriaVirtual = psutil.virtual_memory()
print(memoriaVirtual.total/1024/1024)

#coleta de informações da CPU
nucleos = psutil.cpu_count()
print(nucleos)

#coleta de informações do disco rígido
particoes = psutil.disk_partitions()
disco = psutil.disk_usage("/")
print(particoes)
print(disco)

#coleta de informações da rede
conexoes = psutil.net_connections()
print(conexoes)