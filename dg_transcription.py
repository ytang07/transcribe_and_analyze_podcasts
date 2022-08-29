from deepgram import Deepgram
import asyncio, json, os

from config import dg_key
dg = Deepgram(dg_key)

options = {
    "diarize": True,
    "punctuate": True,
    "paragraphs": True,
    "model": 'general',
    "tier": 'enhanced'
}

async def main():
    podcasts = os.listdir("./lex/audio")
    for podcast in podcasts:
        if "Bishop Robert Barron" in podcast:
            continue
        print(podcast)
        with open(f"lex/audio/{podcast}", "rb") as audio:
            source = {"buffer": audio, "mimetype":'audio/mp3'}
            res = await dg.transcription.prerecorded(source, options)
            with open(f"lex/transcripts/{podcast[:-4]}.json", "w") as transcript:
                # print(transcript)
                json.dump(res, transcript)
    return

asyncio.run(main())