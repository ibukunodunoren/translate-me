from deepgram import Deepgram
import asyncio, json

DEEPGRAM_API_KEY = 'e7be61060c96f293ab1703011527704193cd5406'
PATH_TO_FILE = 'audio-test.m4a'

async def main():
    # Initializes the Deepgram SDK
    dg_client = Deepgram(DEEPGRAM_API_KEY)
    # Creates a websocket connection to Deepgram
    try:
        socket = await dg_client.transcription.live({'punctuate': True})
    except Exception as e:
        print(f'Could not open socket: {e}')
        return
    # Handle sending audio to the socket
    async def process_audio(connection):
        # Open the file
        with open(PATH_TO_FILE, 'rb') as audio:
            # Chunk up the audio to send
            CHUNK_SIZE_BYTES = 8192
            CHUNK_RATE_SEC = 0.001
            chunk = audio.read(CHUNK_SIZE_BYTES)
            while chunk:
                connection.send(chunk)
                await asyncio.sleep(CHUNK_RATE_SEC)
                chunk = audio.read(CHUNK_SIZE_BYTES)
        # Indicate that we've finished sending data
        await connection.finish()

    # Listen for the connection to close
    socket.register_handler(socket.event.CLOSE, lambda c: print(f'Connection closed with code {c}.'))
    # Print incoming transcription objects
    socket.register_handler(socket.event.TRANSCRIPT_RECEIVED, print)

    # Send the audio to the socket
    await process_audio(socket)

asyncio.run(main())



