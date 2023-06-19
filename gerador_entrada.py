import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_test_cases(num_cases, max_sequence_length, max_pedra_length):
    test_cases = []
    for _ in range(num_cases):
        sequence_length = random.randint(1, max_sequence_length)
        pedra_length = random.randint(sequence_length, max_pedra_length)

        # Gera a sequência de habilidades
        sequence = generate_random_string(sequence_length)

        # Gera a pedra
        pedra = generate_random_string(pedra_length)

        # Insere a sequência de habilidades em algumas pedras
        if random.random() < 0.6:  # 60% de chance de inserção da sequência
            start_index = random.randint(0, pedra_length - sequence_length)
            end_index = start_index + sequence_length
            pedra = pedra[:start_index] + sequence + pedra[end_index:]

        # Inverte a sequência de habilidades em algumas pedras
        if random.random() < 0.3:  # 30% de chance de inversão da sequência
            sequence = sequence[::-1]  # Inverte a sequência
            start_index = random.randint(0, pedra_length - sequence_length)
            end_index = start_index + sequence_length
            pedra = pedra[:start_index] + sequence + pedra[end_index:]

        # Concatena as strings da pedra e coloca a sequência no fim da string
        if random.random() < 0.1:  # 10% de chance de concatenação invertida
            pedra = pedra[::-1]  # Inverte a pedra
            pedra += sequence

        test_cases.append((sequence, pedra))
    return test_cases

def write_test_cases_to_file(test_cases, filename):
    with open(filename, 'w') as file:
        file.write(f"{len(test_cases)}\n")
        for sequence, pedra in test_cases:
            file.write(f"{sequence} {pedra}\n")

# Configurações para gerar entradas aleatórias
max_sequence_length = 100
max_pedra_length = 10000
num_files = 10

# Gera e salva os casos de teste em arquivos separados
for i in range(num_files):
    num_cases = 100
    test_cases = generate_test_cases(num_cases, max_sequence_length, max_pedra_length)
    filename = f"input_{i + 1}.txt"
    write_test_cases_to_file(test_cases, filename)
    print(f"Arquivo {filename} gerado com {num_cases} casos de teste.")

print("Todos os arquivos foram gerados.")
