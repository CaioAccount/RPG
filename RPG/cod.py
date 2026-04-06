import random
import time

# =========================
# CLASSES
# =========================
class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque
        self.defesa = defesa
        self.defendendo = False
        self.cooldown = 0
        self.xp = 0
        self.nivel = 1

    def atacar(self, alvo):
        dano = self.ataque + random.randint(-3, 3)
        alvo.receber_dano(dano)
        print(f"💥 {self.nome} causou {dano} de dano!")

    def habilidade(self, alvo):
        if self.cooldown > 0:
            print("⏳ Habilidade em recarga!")
            return False
        dano = int(self.ataque * 2)
        alvo.receber_dano(dano)
        self.cooldown = 2
        print(f"🔥 {self.nome} usou habilidade especial ({dano} dano)!")
        return True

    def defender(self):
        self.defendendo = True
        print(f"🛡️ {self.nome} está defendendo!")

    def receber_dano(self, dano):
        if self.defendendo:
            dano = int(dano / 2)
            self.defendendo = False
            print("🛡️ Dano reduzido!")

        dano = max(0, dano - self.defesa)
        self.vida -= dano

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        if self.xp >= 50:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.ataque += 2
        self.defesa += 1
        self.vida_max += 10
        self.vida = self.vida_max
        self.xp = 0
        print(f"⬆️ {self.nome} subiu para o nível {self.nivel}!")

    def reduzir_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1


class Inimigo(Personagem):
    def escolher_acao(self, alvo):
        acao = random.choice(["ataque", "especial", "defesa"])

        if acao == "ataque":
            self.atacar(alvo)
        elif acao == "especial":
            dano = int(self.ataque * 1.5)
            alvo.receber_dano(dano)
            print(f"🔥 {self.nome} usou ataque especial ({dano})!")
        else:
            self.defender()


# =========================
# FUNÇÕES
# =========================

def escolher_classe():
    classes = {
        "guerreiro": (120, 15, 10),
        "mago": (80, 20, 5),
        "arqueiro": (100, 18, 7)
    }

    print("🧙 Escolha sua classe:")
    for c in classes:
        print(f"- {c}")

    while True:
        escolha = input(">>> ").lower()
        if escolha in classes:
            vida, ataque, defesa = classes[escolha]
            return Personagem(escolha.capitalize(), vida, ataque, defesa)
        print("Classe inválida!")


def criar_inimigo():
    inimigos = [
        ("Goblin", 70, 10, 3),
        ("Orc", 100, 14, 5),
        ("Dragão", 150, 20, 8)
    ]

    nome, vida, ataque, defesa = random.choice(inimigos)
    return Inimigo(nome, vida, ataque, defesa)


def mostrar_status(jogador, inimigo):
    print("\n" + "="*30)
    print(f"🧑 {jogador.nome}: {jogador.vida}/{jogador.vida_max} HP")
    print(f"👹 {inimigo.nome}: {inimigo.vida} HP")
    print("="*30)


def turno_jogador(jogador, inimigo):
    print("\n⚔️ Seu turno!")
    print("1 - Atacar")
    print("2 - Defender")
    print("3 - Habilidade")

    escolha = input(">>> ")

    if escolha == "1":
        jogador.atacar(inimigo)
    elif escolha == "2":
        jogador.defender()
    elif escolha == "3":
        jogador.habilidade(inimigo)
    else:
        print("Opção inválida!")


def turno_inimigo(jogador, inimigo):
    print("\n👹 Turno do inimigo...")
    time.sleep(1)
    inimigo.escolher_acao(jogador)


# =========================
# LOOP DE BATALHA
# =========================

def batalha(jogador):
    inimigo = criar_inimigo()
    print(f"\n⚠️ Um {inimigo.nome} apareceu!")

    while jogador.vida > 0 and inimigo.vida > 0:
        mostrar_status(jogador, inimigo)

        turno_jogador(jogador, inimigo)

        if inimigo.vida <= 0:
            print(f"\n🏆 Você derrotou o {inimigo.nome}!")
            jogador.ganhar_xp(20)
            return True

        turno_inimigo(jogador, inimigo)

        if jogador.vida <= 0:
            print("\n💀 Você morreu...")
            return False

        jogador.reduzir_cooldown()


# =========================
# JOGO PRINCIPAL
# =========================

def jogo():
    print("🎮 RPG MELHORADO\n")

    jogador = escolher_classe()
    print(f"\n✅ Você escolheu: {jogador.nome}")

    vitorias = 0

    while True:
        venceu = batalha(jogador)

        if not venceu:
            break

        vitorias += 1

        # cura parcial
        cura = int(jogador.vida_max * 0.3)
        jogador.vida = min(jogador.vida + cura, jogador.vida_max)
        print(f"✨ Você recuperou {cura} de vida!")

        continuar = input("\nContinuar? (s/n): ").lower()
        if continuar != "s":
            break

    print("\n🏁 Fim de jogo!")
    print(f"🏆 Vitórias: {vitorias}")


# Executar
jogo()