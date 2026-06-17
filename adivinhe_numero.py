import random
import time
import os

# ── Cores ANSI ──────────────────────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"

CYAN    = "\033[96m"
YELLOW  = "\033[93m"
GREEN   = "\033[92m"
RED     = "\033[91m"
MAGENTA = "\033[95m"
BLUE    = "\033[94m"
WHITE   = "\033[97m"
GRAY    = "\033[90m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════╗
║                                              ║
║   🎯  ADIVINHE O NÚMERO  🎯                 ║
║                                              ║
╚══════════════════════════════════════════════╝{RESET}
""")

def barra_tentativas(usadas, total):
    preenchido = int((usadas / total) * 20)
    vazio = 20 - preenchido
    cor = GREEN if usadas <= total // 3 else YELLOW if usadas <= total * 2 // 3 else RED
    barra = f"{cor}{'█' * preenchido}{GRAY}{'░' * vazio}{RESET}"
    return f"  [{barra}{cor}] {usadas}/{total}{RESET}"

def escolher_dificuldade():
    clear()
    banner()
    print(f"  {WHITE}Escolha a dificuldade:{RESET}\n")
    print(f"  {GREEN}[1]{RESET}  Fácil   — 1 a 50   · 10 tentativas")
    print(f"  {YELLOW}[2]{RESET}  Médio   — 1 a 100  ·  7 tentativas")
    print(f"  {RED}[3]{RESET}  Difícil — 1 a 200  ·  5 tentativas\n")

    while True:
        opcao = input(f"  {CYAN}➜  {RESET}").strip()
        if opcao == "1":
            return 50,  10, "Fácil"
        if opcao == "2":
            return 100,  7, "Médio"
        if opcao == "3":
            return 200,  5, "Difícil"
        print(f"  {RED}Opção inválida. Digite 1, 2 ou 3.{RESET}")

def dica(chute, numero):
    diff = abs(chute - numero)
    if diff == 0:
        return ""
    if diff <= 5:
        return f"  {MAGENTA}🔥 Muito quente!{RESET}"
    if diff <= 15:
        return f"  {YELLOW}♨  Quente!{RESET}"
    if diff <= 30:
        return f"  {CYAN}🌊 Morno…{RESET}"
    return f"  {BLUE}❄  Frio!{RESET}"

def jogar(limite, max_tentativas, nivel):
    numero = random.randint(1, limite)
    tentativas = 0
    historico = []

    while tentativas < max_tentativas:
        clear()
        banner()
        print(f"  {WHITE}Nível: {BOLD}{nivel}{RESET}   |   "
              f"{WHITE}Range: {BOLD}1 – {limite}{RESET}\n")
        print(f"  Tentativas usadas:")
        print(barra_tentativas(tentativas, max_tentativas))

        if historico:
            print(f"\n  {GRAY}Histórico: {', '.join(str(h) for h in historico)}{RESET}")

        print(f"\n  {WHITE}Qual é o número? {RESET}", end="")
        try:
            entrada = input().strip()
            chute = int(entrada)
        except ValueError:
            print(f"\n  {RED}Digite um número inteiro válido!{RESET}")
            time.sleep(1)
            continue

        if chute < 1 or chute > limite:
            print(f"\n  {RED}O número deve estar entre 1 e {limite}.{RESET}")
            time.sleep(1)
            continue

        tentativas += 1
        historico.append(chute)

        if chute == numero:
            clear()
            banner()
            estrelas = "⭐" * max(1, 4 - tentativas // 2)
            print(f"\n  {GREEN}{BOLD}🎉 ACERTOU! {estrelas}{RESET}")
            print(f"\n  {WHITE}O número era {BOLD}{CYAN}{numero}{RESET}{WHITE}!")
            print(f"  Você acertou em {BOLD}{tentativas}{RESET} tentativa(s).\n")
            pontos = max(10, (max_tentativas - tentativas + 1) * 10)
            print(f"  {YELLOW}✨ Pontuação: {BOLD}{pontos} pts{RESET}\n")
            return True

        print(f"\n  {'⬆  Muito baixo!' if chute < numero else '⬇  Muito alto!'}")
        print(dica(chute, numero))
        time.sleep(1.2)

    # perdeu
    clear()
    banner()
    print(f"\n  {RED}{BOLD}💀 Fim de jogo!{RESET}")
    print(f"\n  {WHITE}O número era {BOLD}{CYAN}{numero}{RESET}{WHITE}.")
    print(f"  Seus chutes: {GRAY}{', '.join(str(h) for h in historico)}{RESET}\n")
    return False

def main():
    vitorias = 0
    partidas = 0

    while True:
        limite, max_tent, nivel = escolher_dificuldade()
        resultado = jogar(limite, max_tent, nivel)
        partidas += 1
        if resultado:
            vitorias += 1

        print(f"  {GRAY}Placar: {vitorias} vitória(s) em {partidas} partida(s){RESET}\n")
        print(f"  {WHITE}Jogar novamente? {CYAN}[s]{RESET}{WHITE}/{RED}[n]{RESET}  ", end="")
        if input().strip().lower() != "s":
            clear()
            banner()
            print(f"  {CYAN}Obrigado por jogar! Até a próxima. 👋{RESET}\n")
            break

if __name__ == "__main__":
    main()