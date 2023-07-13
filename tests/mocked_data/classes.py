class RequestsOK:
    @property
    def status_code(self):
        return 200

    @property
    def content(self):
        return b"column_1,column_2\nsomeData1,someData2"


class RequestsNotFound:
    @property
    def status_code(self):
        return 400
