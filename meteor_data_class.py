class MeteorDataEntry:
    def __init__(self, m_name, m_id, m_nametype, m_recclass,m_mass,m_fall, m_year, m_reclat, m_recclong, m_geoloc, m_states, m_counties ):

        self.name = m_name[0]
        self.id = m_id[1]
        self.nametype = m_nametype[2]
        self.recclass = m_recclass[3]
        self.mass = m_mass[4]
        self.fall = m_fall[5]
        self.year = m_year[6]
        self.reclat = m_reclat[7]
        self.reclong = m_recclong[8]
        self.geolocation = m_geoloc[9]
        self.states = m_states[10]
        self.counties = m_counties[11]
