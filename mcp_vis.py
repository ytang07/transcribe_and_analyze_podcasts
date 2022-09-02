import matplotlib.pyplot as plt
import os

lex_mcp_files = []
for file in os.listdir("./lex/most_common_phrases"):
    if file.startswith("Lex Fridman in "):
        lex_mcp_files.append(file)


known = {"beautiful": 0, "poetic": 0, "fascinating": 0, "loving": 0}
subjects = {"people": 0, "things": 0}
for filename in lex_mcp_files:
    with open(f"./lex/most_common_phrases/{filename}", "r") as f:
        text = f.read()
    lines = text.split("\n")[:-1]
    for line in lines:
        for word in known.keys():
            if word in line:
                known[word] += 1
        for word in subjects.keys():
            if word in line:
                subjects[word] += 1

print(known)
print(subjects)

labelname_known = "Words Known For"
labelname_subject = "Subject of Discussion"
title_known = "Lex's Adjectives"
title_subject = "Subject of Podcast"
def plot_dict(data: dict, labelname, title, filename):
    x = data.keys()
    y = data.values()
    width = 0.3
    fig, ax = plt.subplots()
    ax.bar(x, y, width, label=labelname)
    ax.set_ylabel("Number of Appearances")
    ax.set_title(title)
    ax.legend()
    plt.xticks(rotation=45, ha="right")
    fig.tight_layout()
    plt.savefig(f"./lex/{filename}.png", pad_inches=1)
    plt.show()

plot_dict(known, labelname_known, title_known, "popular_adjectives")
plot_dict(subjects, labelname_subject, title_subject, "subject_of_discussion")