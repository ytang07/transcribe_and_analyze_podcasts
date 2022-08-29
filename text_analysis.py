import os
import requests
import json
import time
from config import textapi_key

headers = {
    "apikey": textapi_key,
    "Content-Type": "application/json"
}

def mcp(text: str, filename: str):
    print(f"Number of Characters: {len(text)}")
    sentences = text.split(".")
    print(f"Number of Sentences: {len(sentences)}")
    words = len(text.split(" "))
    print(f"Number of Words: {words}")
    texts = []
    sents = 0
    while sents < len(sentences):
        texts.append(" ".join(sentences[sents:sents+1500 if sents + 1500 < len(sentences) else len(sentences)]))
        sents += 1500
    mcps = []
    for text in texts:
        body = {
            "text": text,
            "num_phrases": 5
        }
        start = time.time()
        res = requests.post(url="https://app.thetextapi.com/text/most_common_phrases", headers=headers, json=body)
        print(f"Time elapsed: {time.time() - start} seconds")
        mcps.append(json.loads(res.text)["most common phrases"])
    print(mcps)
    with open(f"lex/most_common_phrases/{filename}.txt", "w") as file:
        for mcp in mcps:
            for phrase in mcp:
                file.write(phrase+"\n")

def ner(text: str, filename: str):
    print(f"Number of Characters: {len(text)}")
    sentences = text.split(".")
    print(f"Number of Sentences: {len(sentences)}")
    words = len(text.split(" "))
    print(f"Number of Words: {words}")
    texts = []
    sents = 0
    while sents < len(sentences):
        texts.append(" ".join(sentences[sents:sents+1500 if sents + 1500 < len(sentences) else len(sentences)]))
        sents += 1500
    ners = []
    for text in texts:
        body = {
            "text": text
        }
        words = len(text.split(" "))
        print(f"Processing 1500 Sentences, {words} Words")
        start = time.time()
        res = requests.post(url="https://app.thetextapi.com/text/ner", headers=headers, json=body)
        print(f"Time elapsed: {time.time() - start} seconds")
        ners.append(json.loads(res.text)["ner"])
    with open(f"lex/ner/{filename}.txt", "w") as file:
        for ner in ners:
            for phrase in ner:
                for word in phrase:
                    file.write(word+" ")
                file.write("\n")

def summarize(text: str, filename: str):
    print(f"Title: {filename}")
    print(f"Number of Characters: {len(text)}")
    sentences = text.split(".")
    print(f"Number of Sentences: {len(sentences)}")
    words = len(text.split(" "))
    print(f"Number of Words: {words}")
    texts = []
    sents = 0
    while sents < len(sentences):
        texts.append(" ".join(sentences[sents:sents+1500 if sents + 1500 < len(sentences) else len(sentences)]))
        sents += 1500
    summaries = []
    for text in texts:
        body = {
            "text": text
        }
        start = time.time()
        res = requests.post(url="https://app.thetextapi.com/text/summarize", headers=headers, json=body)
        print(f"Time elapsed: {time.time() - start} seconds")
        summaries.append(json.loads(res.text)["summary"])
    # print(summaries)
    with open(f"lex/summarize/{filename}.txt", "w") as file:
        for summary in summaries:
            file.write(summary)

def main():
    for filename in os.listdir("lex/transcripts_unenhanced"):
        with open(f"lex/transcripts_unenhanced/{filename}", "r") as file:
            transcript = json.load(file)
        text = transcript["results"]["channels"][0]["alternatives"][0]["transcript"]
        # mcp(text, filename[:-5])
        # ner(text, filename[:-5])
        summarize(text, filename[:-5])

main()