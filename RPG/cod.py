import random

# Classes do jogador
classes = {
    "guerreiro": {"vida": 120, "ataque": 15, "defesa": 10},
    "mago": {"vida": 80, "ataque": 20, "defesa": 5},
    "arqueiro": {"vida": 100, "ataque": 18, "defesa": 7}
}

def escolher_classe():
    print("🧙 Escolha sua classe:")
    for c in classes:
        print(f"- {c}")
    
    while True:
        escolha = input(">>> ").lower()
        if escolha in classes:
            return escolha, classes[escolha].copy()
        print("Classe inválida!")

def criar_inimigo():
    inimigos = [
        {"nome": "Goblin", "vida": 70, "ataque": 10},
        {"nome": "Orc", "vida": 100, "ataque": 14},
        {"nome": "Dragão", "vida": 150, "ataque": 20}
    ]
    return random.choice(inimigos).copy()

def mostrar_status(jogador, inimigo):
    print("\n" + "="*30)
    print(f"🧑 Você: {jogador['vida']} HP")
    print(f"👹 {inimigo['nome']}: {inimigo['vida']} HP")
    print("="*30)

def turno_jogador(jogador, inimigo):
    print("\n⚔️ Seu turno!")
    print("1 - Atacar")
    print("2 - Defender")
    print("3 - Habilidade especial")
    
    escolha = input(">>> ")
    
    if escolha == "1":
        dano = jogador["ataque"] + random.randint(-3, 3)
        inimigo["vida"] -= dano
        print(f"💥 Você causou {dano} de dano!")
    
    elif escolha == "2":
        jogador["defendendo"] = True
        print("🛡️ Você está defendendo!")
    
    elif escolha == "3":
        dano = jogador["ataque"] * 2
        inimigo["vida"] -= dano
        print(f"🔥 ATAQUE ESPECIAL! {dano} de dano!")
    
    else:
        print("Opção inválida!")

def turno_inimigo(jogador, inimigo):
    print("\n👹 Turno do inimigo...")
    
    dano = inimigo["ataque"] + random.randint(-2, 2)
    
    if jogador.get("defendendo"):
        dano = int(dano / 2)
        jogador["defendendo"] = False
        print("🛡️ Você reduziu o dano!")
    
    jogador["vida"] -= dano
    print(f"💢 O {inimigo['nome']} causou {dano} de dano!")

def batalha(jogador):
    inimigo = criar_inimigo()
    print(f"\n⚠️ Um {inimigo['nome']} apareceu!")
    
    while jogador["vida"] > 0 and inimigo["vida"] > 0:
        mostrar_status(jogador, inimigo)
        turno_jogador(jogador, inimigo)
        
        if inimigo["vida"] <= 0:
            print(f"\n🏆 Você derrotou o {inimigo['nome']}!")
            return True
        
        turno_inimigo(jogador, inimigo)
        
        if jogador["vida"] <= 0:
            print("\n💀 Você morreu...")
            return False

def jogo():
    print("🎮 RPG DE TURNO\n")
    
    classe_nome, jogador = escolher_classe()
    print(f"\n✅ Você escolheu: {classe_nome.upper()}")
    
    vitorias = 0
    
    while True:
        venceu = batalha(jogador)
        
        if not venceu:
            break
        
        vitorias += 1
        jogador["vida"] += 20
        print(f"✨ Você recuperou vida! ({jogador['vida']} HP)")
        
        continuar = input("\nContinuar lutando? (s/n): ").lower()
        if continuar != "s":
            break
    
    print("\n🏁 Fim de jogo!")
    print(f"🏆 Vitórias: {vitorias}")

# Rodar jogo
jogo()