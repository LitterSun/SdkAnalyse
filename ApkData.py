class ApkData:
    def __init__(self, name, downloadUrl, categoryName):
        self.name = name
        self.downloadUrl = downloadUrl
        self.categoryName = categoryName


def as_payload(dct):
    return ApkData(dct['name'], dct['downloadUrl'], dct['categoryName'])
