import json
import os

def divide_times():
    times = {}
    for filename in os.listdir("lex/transcripts_unenhanced"):
        print(f"Current filename: {filename}")
        with open(f"lex/transcripts_unenhanced/{filename}", "r") as file:
            transcript = json.load(file)
        paragraphs = transcript["results"]["channels"][0]["alternatives"][0]["paragraphs"]["paragraphs"]
        speaker_times = {}
        assigned_speakers = {}
        for paragraph in paragraphs:
            len_spoken = paragraph["end"]-paragraph["start"]
            speaker = paragraph["speaker"]
            if speaker in assigned_speakers:
                speaker = assigned_speakers[speaker]
            else:
                print(paragraph)
                name = input("Who is the speaker?")
                assigned_speakers[speaker] = name
                speaker = name
            if speaker in speaker_times:
                speaker_times[speaker] += len_spoken
            else:
                speaker_times[speaker] = len_spoken
        times[filename] = speaker_times
    with open("./lex/time_speaking.json", "w") as f:
        json.dump(times, f)

divide_times()

def words_said():
    word_split = {}
    for filename in os.listdir("lex/pretty_scripts"):
        print(f"Current filename: {filename}")
        with open(f"lex/pretty_scripts/{filename}", "r") as file:
            lines = file.readlines()
        cur_speaker = None
        file_word_split = {}
        for line in lines:
            if ":" in line:
                sep = line.split(":")
                cur_speaker = sep[0]
                if cur_speaker in file_word_split:
                    file_word_split[cur_speaker] += len(sep[1])
                else:
                    file_word_split[cur_speaker] = len(sep[1])
        word_split[filename] = file_word_split
    with open("./lex/word_split.json", "w") as f:
        json.dump(word_split, f)

words_said()