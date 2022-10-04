class MeteorDataEntry:
    def __init__(self, meteor_data, name, id, nametype, recclass, mass, fall, year, reclat, reclong, geolocation, states, counties):

        self.name = meteor_data[0]
        self.id = meteor_data[1]
        self.nametype = meteor_data[2]
        self.recclass = meteor_data[3]
        self.mass = meteor_data[4]
        self.fall = meteor_data[5]
        self.year = meteor_data[6]
        self.reclat = meteor_data[7]
        self.reclong = meteor_data[8]
        self.geolocation = meteor_data[9]
        self.states = meteor_data[10]
        self.counties = meteor_data[11]
