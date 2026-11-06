import math

# --- 1-есеп ---
# 79 символдан тұратын алфавит үшін 2^k >= N шарты бойынша ең аз бит санын табу
N = 79
k = math.ceil(math.log2(N))

print("1-есептің шешімі:")
print(f"N = {N} үшін ең аз қажетті бит саны (k): {k} бит\n")

# --- 2-есеп ---
# Префикстік код бойынша хабарды декодтау
code_table = {
    '0': 'A',
    '10': 'B',
    '110': 'C',
    '111': 'D'
}

encoded_message = "10110111010"

decoded_message = []
current_code = ""

for bit in encoded_message:
    current_code += bit
    if current_code in code_table:
        decoded_message.append(code_table[current_code])
        current_code = ""

result = "".join(decoded_message)

print("2-есептің шешімі:")
print(f"Кодталған хабар: {encoded_message}")
print(f"Декодталған нәтиже: {result}")