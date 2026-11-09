import re
def verficiar_senha(senha):
    if len(senha) < 8:
        return "Erro: Mínimo de 8 caracteres"
    elif not re.search(r'[A-Z]', senha):
        return 'Erro: necessita de pelo menos uma letra maiúscula'
    elif not re.search(r'\d', senha):
        return "Erro: necessita de ao menos um número"