import requests
import json
import os

from text_analysis import headers # gotta comment out main() in text_analytics to do this

# Re-run MCP on both
# Summarize Guest
def nlp():
    for filename in os.listdir("lex/pretty_scripts"):
        print(f"Current File: {filename}")
        with open(f"lex/pretty_scripts/{filename}", "r") as f:
            lines = f.readlines()
        separated_speakers = dict()
        for line in lines:
            if ":" in line:
                speaker_sep = line.split(":")
                if speaker_sep[0][1:] in separated_speakers.keys():
                    separated_speakers[speaker_sep[0][1:]] += speaker_sep[1]
                else:
                    separated_speakers[speaker_sep[0][1:]] = speaker_sep[1]
        for speaker, spoken in separated_speakers.items():
            body = {
                "text": spoken,
                "num_phrases": 5
            }
            res = requests.post("https://app.thetextapi.com/text/most_common_phrases", headers=headers, json=body)
            mcp = json.loads(res.text)["most common phrases"]
            with open(f"lex/most_common_phrases/{speaker} in {filename}", "w") as f:
                for entry in mcp:
                    f.write(f"{entry}\n")

nlp()