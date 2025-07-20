import subprocess

def executarComandoSeguro(comandoInteiro: str) -> str:
    if 'rm' in comandoInteiro:
        return 'Comando proibido'

    saidaDoComando = subprocess.run(str(comandoInteiro), shell=True)
    return str(saidaDoComando)


def TEMPLATE_DE_NOTIFICACAO(mensagemDaNotificacao: str) -> str:
    return f'''notify-send \
      --urgency=critical \
      --expire-time=10000 \
      --icon=dialog-warning \
      "{mensagemDaNotificacao}"
    '''


print(TEMPLATE_DE_NOTIFICACAO('teste'))
