def inicializar_sistemas():
    """Inicializa os sistemas essenciais do rover lunar."""
    sistemas = [
        "Sistema de Navegação",
        "Sistema de Comunicação",
        "Painéis Solares",
        "Sensores Ambientais",
        "Sistema de Locomoção"
    ]

    print("=== Iniciando sequência de boot do Rover Lunar ===")
    for sistema in sistemas:
        print(f"[OK] {sistema} inicializado com sucesso.")

    print("=== Todos os sistemas estão operacionais. Rover pronto para a missão. ===")


if __name__ == "__main__":
    inicializar_sistemas()