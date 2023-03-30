import io
from google.cloud import speech_v1p1beta1 as speech

from medical_text_tagger import extract_medical_data

# Replace with the path to your service account key file
key_file = 'mediscribe-379816-3a2504d7400b.json'

# Initialize the Speech-to-Text client with your credentials
client = speech.SpeechClient.from_service_account_json(key_file)


def print_audio_transcript_and_extracted_entities(file_name='Notes_1.mp3'):
    # Load the audio file into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()

    # Configure the request
    config = speech.types.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=44100,
        language_code='en-US',
        enable_automatic_punctuation=True,
        use_enhanced=True,
        model='phone_call',
        speech_contexts=[
            speech.types.SpeechContext(
                phrases=['medical terms', 'medical jargon'],
                boost=10
            )
        ],
        enable_speaker_diarization=True
    )

    audio = speech.types.RecognitionAudio(content=content, uri=None)

    # Call the Speech-to-Text API
    response = client.recognize(config=config, audio=audio)

    transcripts = ''
    # Print the results
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        transcripts += result.alternatives[0].transcript

        print('Confidence: {}'.format(result.alternatives[0].confidence))

    extract_medical_data.print_entities(transcripts)


def print_audio_transcript_entities_json(file_name='Notes_1.mp3'):
    # Load the audio file into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()

    # Configure the request
    config = speech.types.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=44100,
        language_code='en-US',
        enable_automatic_punctuation=True,
        use_enhanced=True,
        model='phone_call',
        speech_contexts=[
            speech.types.SpeechContext(
                phrases=['medical terms', 'medical jargon'],
                boost=10
            )
        ],
        enable_speaker_diarization=True
    )

    audio = speech.types.RecognitionAudio(content=content, uri=None)

    # Call the Speech-to-Text API
    response = client.recognize(config=config, audio=audio)

    transcripts = ''
    # Print the results
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        transcripts += result.alternatives[0].transcript

        print('Confidence: {}'.format(result.alternatives[0].confidence))
        print('\n')

    print( extract_medical_data.extract_entities(transcripts) )


if __name__ == '__main__':
    # print_audio_transcript_entities_json('Notes_1.mp3')
    # print_audio_transcript_entities_json('Notes_2.mp3')
    print_audio_transcript_entities_json('Notes_4.mp3')
    print_audio_transcript_entities_json('Notes_5.mp3')