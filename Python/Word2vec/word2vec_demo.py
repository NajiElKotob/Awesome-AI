# ============================================================
# Word2Vec (Skip-gram) from scratch – learning & demo version
# Only needs NumPy:  pip install numpy
# Run:               python word2vec_demo.py
# ============================================================

import numpy as np

np.random.seed(42)  # same results every run (good for demos)

# ------------------------------------------------------------
# 1) A tiny corpus
#    Words that appear in similar contexts should end up with
#    similar vectors (e.g. "king"/"queen", "cat"/"dog").
# ------------------------------------------------------------
corpus = [
    "the king rules the kingdom",
    "the queen rules the kingdom",
    "the king is a man",
    "the queen is a woman",
    "the cat drinks milk",
    "the dog drinks milk",
    "the cat chases the mouse",
    "the dog chases the cat",
    "a man and a woman walk",
    "the prince is a young man",
    "the princess is a young woman",
]

# Split each sentence into words (tokens)
sentences = [s.lower().split() for s in corpus]

# ------------------------------------------------------------
# 2) Build the vocabulary: give every unique word an ID number
# ------------------------------------------------------------
vocab = sorted(set(w for s in sentences for w in s))
word2id = {w: i for i, w in enumerate(vocab)}   # "king" -> 7
id2word = {i: w for w, i in word2id.items()}    # 7 -> "king"
V = len(vocab)                                  # vocabulary size
print(f"Vocabulary size: {V}")

# ------------------------------------------------------------
# 3) Create training pairs (center word, context word)
#    Skip-gram idea: from the CENTER word, predict the words
#    around it inside a small WINDOW.
#    "the king rules" with window=2 gives:
#    (king, the), (king, rules), ...
# ------------------------------------------------------------
WINDOW = 2
pairs = []
for s in sentences:
    for i, center in enumerate(s):
        for j in range(max(0, i - WINDOW), min(len(s), i + WINDOW + 1)):
            if i != j:  # skip the word itself
                pairs.append((word2id[center], word2id[s[j]]))
print(f"Training pairs: {len(pairs)}")

# ------------------------------------------------------------
# 4) The model = just two weight matrices
#    W_in : the word vectors we actually want (V x D)
#    W_out: helper weights used to predict context words (D x V)
#    D = embedding size (how many numbers describe each word)
# ------------------------------------------------------------
D = 10
W_in = np.random.randn(V, D) * 0.1
W_out = np.random.randn(D, V) * 0.1

def softmax(x):
    # Turns raw scores into probabilities that sum to 1
    e = np.exp(x - np.max(x))  # subtract max for numerical safety
    return e / e.sum()

# ------------------------------------------------------------
# 5) Training loop
#    For each pair: look up the center vector, score every word
#    in the vocab, compare with the true context word, and nudge
#    the weights to make the right answer more likely.
# ------------------------------------------------------------
EPOCHS = 300
LR = 0.05  # learning rate = size of each nudge

for epoch in range(EPOCHS):
    total_loss = 0
    np.random.shuffle(pairs)
    for center, context in pairs:
        h = W_in[center]            # forward: center word's vector (D,)
        scores = h @ W_out          # one score per vocab word (V,)
        probs = softmax(scores)     # probability of each word being context

        total_loss += -np.log(probs[context] + 1e-9)  # low prob on true word = high loss

        # backward: error = predicted probs minus the "correct answer"
        err = probs.copy()
        err[context] -= 1

        grad_W_out = np.outer(h, err)  # how W_out should change
        grad_h = W_out @ err           # how the center vector should change

        W_out -= LR * grad_W_out
        W_in[center] -= LR * grad_h

    if epoch % 50 == 0 or epoch == EPOCHS - 1:
        print(f"Epoch {epoch:3d} | loss = {total_loss / len(pairs):.4f}")

# ------------------------------------------------------------
# 6) Use the learned vectors
#    Cosine similarity: 1 = same direction (very similar),
#    0 = unrelated, -1 = opposite.
# ------------------------------------------------------------
def cosine(a, b):
    return a @ b / (np.linalg.norm(a) * np.linalg.norm(b))

def most_similar(word, top_n=3):
    v = W_in[word2id[word]]
    sims = [(id2word[i], cosine(v, W_in[i])) for i in range(V) if id2word[i] != word]
    return sorted(sims, key=lambda x: -x[1])[:top_n]

print("\n--- Most similar words ---")
for w in ["king", "cat", "man", "milk"]:
    result = ", ".join(f"{x} ({s:.2f})" for x, s in most_similar(w))
    print(f"{w:6s} -> {result}")

print("\n--- Vector for 'king' (first 5 of 10 numbers) ---")
print(np.round(W_in[word2id["king"]][:5], 3))
