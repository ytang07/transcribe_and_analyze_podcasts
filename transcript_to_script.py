import json
import os

# create transcripts
def create_transcripts():
    for filename in os.listdir("lex/transcripts_unenhanced"):
        # if "Joe Rogan" in filename or "Bishop Robert Barron" in filename:
        #     continue
        with open(f"lex/transcripts_unenhanced/{filename}", "r") as file:
            transcript = json.load(file)
        paragraphs = transcript["results"]["channels"][0]["alternatives"][0]["paragraphs"]
        # words = transcript["results"]["channels"][0]["alternatives"][0]["words"]
        print(paragraphs['transcript'])
        with open(f"lex/pretty_scripts/{filename[:-5]}.txt", "w") as f:
            for line in paragraphs['transcript']:
                f.write(line)
# create_transcripts()

# separate transcripts by speaker
# label speakers by printing first lines by the speaker
# coalesce them into one file
def assign_speakers():
    for filename in os.listdir("lex/pretty_scripts"):
        print(f"Current File: {filename}")
        with open(f"lex/pretty_scripts/{filename}", "r") as f:
            lines = f.readlines()
        spoken = []
        names = []
        for line in lines:
            if line.startswith("Speaker "):
                if line[0:9] in spoken:
                    continue
                print(line)
                name = input("Who is the Speaker?")
                if len(name) <= 1:
                    continue
                spoken.append(line[:9])
                names.append(name)
        print(spoken)
        print(names)
        filedata = "\n".join(lines)
        print(filedata)
        for speaker, name in zip(spoken, names):
            filedata = filedata.replace(speaker, name)
        with open(f"lex/pretty_scripts/{filename}", "w") as f:
            f.write(filedata)

# assign_speakers()