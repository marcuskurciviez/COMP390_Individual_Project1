class MeteorDataEntry:

    #commenting this out just to see if something else works
    #def __init__(self,m_data, m_name, m_id, m_nametype, m_recclass,m_mass,m_fall, m_year, m_reclat, m_recclong, m_geoloc, m_states, m_counties):
    def __init__(self,m_data):

        self.name = m_data[0]
        self.id = m_data[1]
        self.nametype = m_data[2]
        self.recclass = m_data[3]
        self.mass = m_data[4]
        self.fall = m_data[5]
        self.year = m_data[6]
        self.reclat = m_data[7]
        self.reclong = m_data[8]
        self.geolocation = m_data[9]
        self.states = m_data[10]
        self.counties = m_data[11]
