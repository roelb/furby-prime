import requests

data = {
        "audioConfig": {
            "audioEncoding": "LINEAR16",
            "effectsProfileId": [
                "small-bluetooth-speaker-class-device"
                ],
            "pitch": 13.2,
            "speakingRate": 0.44
            },
        "input": {
            "text": "Wie vandaag in de auto stapte om op vakantie te gaan, had een grote kans om in de file terecht te komen. Het was tot nu toe de drukste dag op de Europese wegen deze zomer, meldt de ANWB."
            },
        "voice": {
            "languageCode": "nl-NL",
            "name": "nl-NL-Standard-C"
            }
        }


def main():
    r = requests.post("https://texttospeech.googleapis.com/v1beta1/text:synthesize?key=AIzaSyCdnFkbgIYC5tUDGirxlzBWelYoHQRQJYU", json=data)
    print(r.text)

main()
