import matplotlib.pyplot as plt
import json

# plot speaking times bar charts
def vis_time():
    with open("./lex/time_speaking.json", "r") as f:
        time_dict = json.load(f)
    labels = []
    lex = []
    guest = []
    for podcast in time_dict.values():
        for entry in podcast:
            if "Lex" in entry:
                lex.append(podcast[entry])
            else:
                guest.append(podcast[entry])
                labels.append(entry)
    print(labels)
    print(lex)
    print(guest)
    width = 0.3
    fig, ax = plt.subplots()
    ax.bar(labels, lex, width, label="Lex")
    ax.bar(labels, guest, width, bottom=lex, label="Guest")
    ax.set_ylabel("Time Spent Speaking")
    ax.set_title("Lex vs Guests Speaking Time")
    ax.legend()
    plt.xticks(rotation=45, ha="right")
    fig.tight_layout()
    plt.savefig("./lex/time_speaking.png", pad_inches=1)
    plt.show()

vis_time()

# plot graph for words said
def vis_words():
    with open("./lex/word_split.json", "r") as f:
        time_dict = json.load(f)
    labels = []
    lex = []
    guest = []
    for podcast in time_dict.values():
        for entry in podcast:
            if "Lex" in entry:
                lex.append(podcast[entry])
            else:
                guest.append(podcast[entry])
                labels.append(entry)
    print(labels)
    print(lex)
    print(guest)
    width = 0.3
    fig, ax = plt.subplots()
    ax.bar(labels, lex, width, label="Lex")
    ax.bar(labels, guest, width, bottom=lex, label="Guest")
    ax.set_ylabel("Words Said")
    ax.set_title("Lex vs Guests Number of Words Said")
    ax.legend()
    plt.xticks(rotation=45, ha="right")
    fig.tight_layout()
    plt.savefig("./lex/words_said.png", pad_inches=1)
    plt.show()

vis_words()