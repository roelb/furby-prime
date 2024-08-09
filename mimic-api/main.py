import requests
hallo = "http://192.168.8.242:59125/api/tts?text=hallo&voice=nl/nathalie_low&noiseScale=0.667&noiseW=0.8&lengthScale=1&ssml=false&audioTarget=server"
een = "http://192.168.8.242:59125/api/tts?text=een&voice=nl/nathalie_low&noiseScale=0.667&noiseW=0.8&lengthScale=1&ssml=false&audioTarget=server"
twee = "http://192.168.8.242:59125/api/tts?text=twee&voice=nl/nathalie_low&noiseScale=0.667&noiseW=0.8&lengthScale=1&ssml=false&audioTarget=server"
drie = "http://192.168.8.242:59125/api/tts?text=drie&voice=nl/nathalie_low&noiseScale=0.667&noiseW=0.8&lengthScale=1&ssml=false&audioTarget=server"
deel1 = "http://192.168.8.242:59125/api/tts?text=Een regenboog is een gekleurde cirkelboog die aan de hemel waargenomen kan worden als de, laagstaande,&voice=nl/nathalie_low&noiseScale=0.667&noiseW=0.8&lengthScale=1&ssml=false&audioTarget=server"
deel2 = "http://192.168.8.242:59125/api/tts?text=die aan de hemel waargenomen kan worden als de, laagstaande,&voice=nl/nathalie_low&noiseScale=0.667&noiseW=0.8&lengthScale=1&ssml=false&audioTarget=server"
deel3 = "http://192.168.8.242:59125/api/tts?text=zon tegen een nevel van waterdruppeltjes aan schijnt en de zon zich achter de waarnemer bevindt. Het is een optisch effect dat wordt veroorzaakt door de breking en weerspiegeling van licht in de waterdruppels.&voice=nl/nathalie_low&noiseScale=0.667&noiseW=0.8&lengthScale=1&ssml=false&audioTarget=server"
req = "http://192.168.8.242:59125/api/tts?text=Een regenboog is een gekleurde cirkelboog die aan de hemel waargenomen kan worden als de, laagstaande, zon tegen een nevel van waterdruppeltjes aan schijnt en de zon zich achter de waarnemer bevindt. Het is een optisch effect dat wordt veroorzaakt door de breking en weerspiegeling van licht in de waterdruppels.&voice=nl/nathalie_low&noiseScale=0.667&noiseW=0.8&lengthScale=1&ssml=false&audioTarget=server"

import grequests

class Test:
    def __init__(self):
        self.urls = [
            deel1,
            deel2,
            deel3,
            #req,
        ]

    def exception(self, request, exception):
        print("Problem: {}: {}".format(request.url, exception))

    def async(self):
        results = grequests.map((grequests.get(u) for u in self.urls), exception_handler=self.exception, size=5)
        print(results)


def main():
    test = Test()
    test.async()

if __name__ == "__main__":
    main()

