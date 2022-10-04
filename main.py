from meteor_data_class import *


def main():
    with open('meteorite_landings_data.txt', 'r') as table:

#variables set up as empty arrays
        list = []
        mass_of_meteor = []
        date_of_meteor = []



        for item in table:
            stripped = item.strip('\n')
            line_split = stripped.split('\t')
            list.append(MeteorDataEntry(line_split))


        for i in list:
            if i.m_mass.isnumeric():
                if int(i.m_mass) > 2900000:
                    mass_of_meteor.append(i)


        name_label = 'NAME'
        mass_label = 'MASS (g)'
        print(f'{name_label:<24}{mass_label:<20}')
        print('============================================')



        for i in mass_of_meteor:
            print(f'{i.m_name:<24}{i.m_mass:<20}')

        for i in list:
            if i.m_year.isnumeric():
                if int(i.m_year) >= 2013:
                    date_of_meteor.append(i)



        name_label = 'NAME'
        year_label = 'YEAR'
        print(f'{name_label:<24}{year_label:<20}')
        print('============================================')
        for i in date_of_meteor:
            print(f'{i.m_name:<24}{i.m_year:<20}')



if __name__ == '__main__':
    main()

