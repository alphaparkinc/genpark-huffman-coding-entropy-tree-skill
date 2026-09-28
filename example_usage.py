from client import HuffmanCoder

def main():
    sample = "autonomous_agent_matrix_genpark"
    entropy = HuffmanCoder.calculate_entropy(sample)
    bits, tree = HuffmanCoder.encode(sample)
    decoded = HuffmanCoder.decode(bits, tree)
    print(f"Entropy: {entropy:.3f} bits/symbol")
    print(f"Compressed {len(sample)*8} bits into {len(bits)} bits.")
    print("Decoded matches original:", decoded == sample)

if __name__ == "__main__":
    main()
