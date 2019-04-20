class ApkData:
    def __init__(self, name, downloadUrl):
        self.name = name
        self.downloadUrl = downloadUrl


def as_payload(dct):
    return ApkData(dct['name'], dct['downloadUrl'])
