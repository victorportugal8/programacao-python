import web, psutil

urls = ('/', 'Index')

class Index:
    def GET(self):
        memoriaVirtual = psutil.virtual_memory()
        memoriaSwap = psutil.swap_memory()
        cpuTempo = psutil.cpu_times()
        cpuNucleos = psutil.cpu_count()
        particoes = psutil.disk_partitions()
        disco = psutil.disk_usage("/")
        bateria = psutil.sensors_battery()
        return "SESSAO DA MEMORIA\n" + "Memoria total = " + str(memoriaVirtual.total / 1024 / 1024) + "\nMemoria livre = " + str(memoriaVirtual.free / 1024 / 1024) + "\nMemoria usada = " + str(memoriaVirtual.used / 1024 / 1024) + "\n___________________________________\n" + "\nSESSAO DA MEMORIA(SWAP)" + "\nMemoria total = " + str(memoriaSwap.total / 1024 / 1024) + "\nMemoria livre = " + str(memoriaSwap.free / 1024 / 1024) + "\nMemoria usada = " + str(memoriaSwap.used / 1024 / 1024) + "\n___________________________________\n" + "\nSESSAO DA CPU(TEMPO)" + "\Tempo gasto por processos normais = " + str(cpuTempo.user) + "\nTempo gasto por processos no modo kernel = " + str(cpuTempo.system) + "\nTempo gasto 'fazendo nada' (ocioso) = " + str(cpuTempo.idle) + "\n___________________________________\n" + "\nSESSAO DA CPU(NUCLEOS)" + "\nQuantidade de nucleos da CPU = " + str(cpuNucleos) + "\n___________________________________\n" + "\nSESSAO DAS PARTICOES\n" + str(particoes) + "\n___________________________________\n" + "\nSESSAO DO DISCO RIGIDO" + "\nEspaco total em disco = " + str(disco.total) + "\nEspaco livre em disco = " + str(disco.free) + "\nEspaco usado em disco = " + str(disco.used) + "\n___________________________________\n" + "\nSESSAO DA BATERIA(APENAS PARA NOTEBOOKS)" + "\nPorcentagem = " + str(bateria.percent) + "\nTempo restante de uso = " + str(bateria.secsleft)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()