from Jugador import Jugador
from Equipo import Equipo
from Liga import Liga

def main():

    # ============================
    # 1. CREACIÓN DE JUGADORES A MANO
    # ============================

    barca_jugadores = [
        Jugador("Marc-André ter Stegen", 1, 0, 0, 1),
        Jugador("Ronald Araújo", 4, 2, 1, 5),
        Jugador("Pau Cubarsí", 2, 0, 0, 3),
        Jugador("Alejandro Balde", 3, 1, 0, 4),
        Jugador("Jules Koundé", 23, 1, 0, 6),
        Jugador("Pedri", 8, 3, 0, 2),
        Jugador("Gavi", 6, 2, 0, 7),
        Jugador("Frenkie de Jong", 21, 1, 0, 1),
        Jugador("Lamine Yamal", 27, 5, 0, 2),
        Jugador("Lewandowski", 9, 14, 0, 3),
        Jugador("Raphinha", 11, 6, 0, 4)
    ]

    # ============================
    # 2. EQUIPO HECHO A MANO
    # ============================

    barca = Equipo(
        nombre="FC Barcelona",
        estadio="Camp Nou",
        fundacion=1899,
        jugadores=barca_jugadores,
        puntos=75,
        partidos_ganados=23,
        partidos_perdidos=5,
        partidos_empatados=6
    )

    # ============================
    # REAL MADRID
    # ============================
    madrid_jugadores = [
        Jugador("Thibaut Courtois", 1, 0, 0, 0),
        Jugador("Dani Carvajal", 2, 1, 0, 5),
        Jugador("Éder Militão", 3, 2, 0, 4),
        Jugador("David Alaba", 4, 1, 0, 3),
        Jugador("Ferland Mendy", 23, 0, 0, 2),
        Jugador("Eduardo Camavinga", 12, 2, 0, 3),
        Jugador("Federico Valverde", 15, 4, 0, 4),
        Jugador("Luka Modrić", 10, 2, 0, 2),
        Jugador("Jude Bellingham", 5, 10, 0, 3),
        Jugador("Vinícius Jr", 7, 12, 0, 5),
        Jugador("Rodrygo", 11, 7, 0, 2)
    ]

    madrid = Equipo(
        nombre="Real Madrid",
        estadio="Santiago Bernabéu",
        fundacion=1902,
        jugadores=madrid_jugadores,
        puntos=78,
        partidos_ganados=24,
        partidos_perdidos=4,
        partidos_empatados=6
    )

    # ============================
    # ATLÉTICO DE MADRID
    # ============================
    atletico_jugadores = [
        Jugador("Jan Oblak", 13, 0, 0, 0),
        Jugador("Nahuel Molina", 16, 1, 0, 4),
        Jugador("José María Giménez", 2, 2, 1, 6),
        Jugador("Mario Hermoso", 22, 1, 0, 3),
        Jugador("Reinildo Mandava", 23, 0, 0, 2),
        Jugador("Koke", 6, 1, 0, 4),
        Jugador("Rodrigo De Paul", 5, 2, 0, 5),
        Jugador("Marcos Llorente", 14, 3, 0, 3),
        Jugador("Antoine Griezmann", 8, 11, 0, 2),
        Jugador("Álvaro Morata", 19, 9, 0, 4),
        Jugador("Ángel Correa", 10, 5, 0, 3)
    ]

    atletico = Equipo(
        nombre="Atlético de Madrid",
        estadio="Cívitas Metropolitano",
        fundacion=1903,
        jugadores=atletico_jugadores,
        puntos=68,
        partidos_ganados=20,
        partidos_perdidos=7,
        partidos_empatados=7
    )

    # ============================
    # REAL SOCIEDAD
    # ============================
    realsociedad_jugadores = [
        Jugador("Álex Remiro", 1, 0, 0, 1),
        Jugador("Hamari Traoré", 18, 0, 0, 3),
        Jugador("Robin Le Normand", 24, 1, 0, 4),
        Jugador("Igor Zubeldia", 5, 1, 0, 3),
        Jugador("Aihen Muñoz", 3, 0, 0, 2),
        Jugador("Martín Zubimendi", 4, 2, 0, 4),
        Jugador("Mikel Merino", 8, 3, 0, 5),
        Jugador("Brais Méndez", 23, 4, 0, 3),
        Jugador("Takefusa Kubo", 14, 6, 0, 2),
        Jugador("Mikel Oyarzabal", 10, 8, 0, 1),
        Jugador("Alexander Sørloth", 9, 7, 0, 3)
    ]

    realsociedad = Equipo(
        nombre="Real Sociedad",
        estadio="Reale Arena",
        fundacion=1909,
        jugadores=realsociedad_jugadores,
        puntos=62,
        partidos_ganados=18,
        partidos_perdidos=9,
        partidos_empatados=7
    )

    # ============================
    # ATHLETIC CLUB
    # ============================
    athletic_jugadores = [
        Jugador("Unai Simón", 1, 0, 0, 1),
        Jugador("Óscar de Marcos", 18, 1, 0, 4),
        Jugador("Dani Vivian", 3, 2, 0, 3),
        Jugador("Aitor Paredes", 4, 0, 0, 2),
        Jugador("Yuri Berchiche", 17, 1, 0, 3),
        Jugador("Oihan Sancet", 8, 5, 0, 2),
        Jugador("Mikel Vesga", 6, 0, 0, 5),
        Jugador("Ander Herrera", 21, 2, 0, 4),
        Jugador("Nico Williams", 10, 7, 0, 3),
        Jugador("Iñaki Williams", 9, 6, 0, 2),
        Jugador("Gorka Guruzeta", 12, 8, 0, 1)
    ]

    athletic = Equipo(
        nombre="Athletic Club",
        estadio="San Mamés",
        fundacion=1898,
        jugadores=athletic_jugadores,
        puntos=60,
        partidos_ganados=17,
        partidos_perdidos=9,
        partidos_empatados=8
    )

    # ============================
    # VILLARREAL
    # ============================
    villarreal_jugadores = [
        Jugador("Filip Jørgensen", 13, 0, 0, 0),
        Jugador("Juan Foyth", 8, 1, 0, 4),
        Jugador("Raúl Albiol", 3, 2, 0, 2),
        Jugador("Aïssa Mandi", 23, 0, 0, 3),
        Jugador("Alberto Moreno", 18, 1, 0, 2),
        Jugador("Dani Parejo", 10, 3, 0, 5),
        Jugador("Étienne Capoue", 6, 1, 0, 4),
        Jugador("Álex Baena", 16, 6, 0, 3),
        Jugador("Ilias Akhomach", 11, 4, 0, 2),
        Jugador("Gerard Moreno", 7, 9, 0, 1),
        Jugador("Alexander Sørloth", 9, 8, 0, 3)
    ]

    villarreal = Equipo(
        nombre="Villarreal CF",
        estadio="Estadio de la Cerámica",
        fundacion=1923,
        jugadores=villarreal_jugadores,
        puntos=58,
        partidos_ganados=16,
        partidos_perdidos=9,
        partidos_empatados=9
    )

    # ============================
    # REAL BETIS
    # ============================
    betis_jugadores = [
        Jugador("Rui Silva", 13, 0, 0, 0),
        Jugador("Héctor Bellerín", 2, 0, 0, 3),
        Jugador("Germán Pezzella", 6, 1, 0, 4),
        Jugador("Chadi Riad", 3, 0, 0, 2),
        Jugador("Abner", 20, 1, 0, 3),
        Jugador("Guido Rodríguez", 21, 2, 0, 5),
        Jugador("William Carvalho", 14, 1, 0, 4),
        Jugador("Isco", 22, 4, 0, 2),
        Jugador("Ayoze Pérez", 10, 5, 0, 3),
        Jugador("Borja Iglesias", 7, 7, 0, 2),
        Jugador("Willian José", 12, 6, 0, 1)
    ]

    betis = Equipo(
        nombre="Real Betis",
        estadio="Benito Villamarín",
        fundacion=1907,
        jugadores=betis_jugadores,
        puntos=55,
        partidos_ganados=15,
        partidos_perdidos=10,
        partidos_empatados=9
    )

    # ============================
    # VALENCIA CF
    # ============================
    valencia_jugadores = [
        Jugador("Giorgi Mamardashvili", 25, 0, 0, 1),
        Jugador("Thierry Correia", 2, 0, 0, 4),
        Jugador("Cristhian Mosquera", 3, 1, 0, 3),
        Jugador("Cenk Özkacar", 15, 0, 0, 2),
        Jugador("José Gayà", 14, 1, 0, 4),
        Jugador("Pepelu", 18, 3, 0, 5),
        Jugador("Javi Guerra", 8, 2, 0, 3),
        Jugador("André Almeida", 10, 2, 0, 4),
        Jugador("Diego López", 16, 4, 0, 2),
        Jugador("Hugo Duro", 19, 8, 0, 3),
        Jugador("Javi Guerra", 9, 5, 0, 2)
    ]

    valencia = Equipo(
        nombre="Valencia CF",
        estadio="Mestalla",
        fundacion=1919,
        jugadores=valencia_jugadores,
        puntos=52,
        partidos_ganados=14,
        partidos_perdidos=11,
        partidos_empatados=9
    )

    # ============================
    # SEVILLA FC
    # ============================
    sevilla_jugadores = [
        Jugador("Ørjan Nyland", 13, 0, 0, 0),
        Jugador("Gonzalo Montiel", 2, 1, 0, 4),
        Jugador("Loïc Badé", 22, 2, 0, 3),
        Jugador("Sergio Ramos", 4, 3, 1, 5),
        Jugador("Marcos Acuña", 19, 0, 0, 3),
        Jugador("Fernando", 6, 1, 0, 6),
        Jugador("Joan Jordán", 8, 2, 0, 4),
        Jugador("Óliver Torres", 21, 1, 0, 2),
        Jugador("Lucas Ocampos", 5, 4, 0, 3),
        Jugador("Youssef En-Nesyri", 15, 9, 0, 2),
        Jugador("Erik Lamela", 17, 3, 0, 1)
    ]

    sevilla = Equipo(
        nombre="Sevilla FC",
        estadio="Ramón Sánchez-Pizjuán",
        fundacion=1890,
        jugadores=sevilla_jugadores,
        puntos=50,
        partidos_ganados=13,
        partidos_perdidos=11,
        partidos_empatados=10
    )

    # ============================
    # GETAFE CF
    # ============================
    getafe_jugadores = [
        Jugador("David Soria", 13, 0, 0, 1),
        Jugador("Damián Suárez", 22, 0, 0, 5),
        Jugador("Omar Alderete", 15, 1, 0, 4),
        Jugador("Gastón Álvarez", 4, 1, 0, 3),
        Jugador("Diego Rico", 16, 0, 0, 3),
        Jugador("Nemanja Maksimović", 20, 2, 0, 5),
        Jugador("Luis Milla", 5, 3, 0, 4),
        Jugador("Mason Greenwood", 12, 7, 0, 2),
        Jugador("Carles Aleñá", 11, 2, 0, 3),
        Jugador("Borja Mayoral", 19, 6, 0, 1),
        Jugador("Enes Ünal", 10, 5, 1, 2)
    ]

    getafe = Equipo(
        nombre="Getafe CF",
        estadio="Coliseum Alfonso Pérez",
        fundacion=1983,
        jugadores=getafe_jugadores,
        puntos=48,
        partidos_ganados=12,
        partidos_perdidos=11,
        partidos_empatados=11
    )

    # ============================
    # OSASUNA
    # ============================
    osasuna_jugadores = [
        Jugador("Sergio Herrera", 1, 0, 0, 0),
        Jugador("Jesús Areso", 12, 0, 0, 4),
        Jugador("Alejandro Catena", 24, 2, 0, 3),
        Jugador("David García", 5, 1, 0, 4),
        Jugador("Juan Cruz", 3, 0, 0, 2),
        Jugador("Lucas Torró", 6, 2, 0, 5),
        Jugador("Jon Moncayola", 7, 1, 0, 3),
        Jugador("Aimar Oroz", 10, 4, 0, 2),
        Jugador("Rubén García", 14, 3, 0, 3),
        Jugador("Ante Budimir", 17, 8, 0, 4),
        Jugador("Chimy Ávila", 9, 5, 0, 2)
    ]

    osasuna = Equipo(
        nombre="CA Osasuna",
        estadio="El Sadar",
        fundacion=1920,
        jugadores=osasuna_jugadores,
        puntos=47,
        partidos_ganados=12,
        partidos_perdidos=12,
        partidos_empatados=10
    )

    # ============================
    # RAYO VALLECANO
    # ============================
    rayo_jugadores = [
        Jugador("Stole Dimitrievski", 1, 0, 0, 1),
        Jugador("Iván Balliu", 20, 0, 0, 5),
        Jugador("Abdul Mumin", 16, 1, 0, 4),
        Jugador("Florian Lejeune", 24, 2, 0, 3),
        Jugador("Pep Chavarría", 3, 0, 0, 2),
        Jugador("Óscar Valentín", 23, 1, 0, 6),
        Jugador("Pathé Ciss", 21, 2, 0, 4),
        Jugador("Isi Palazón", 7, 5, 0, 3),
        Jugador("Álvaro García", 18, 4, 0, 2),
        Jugador("Sergio Camello", 34, 6, 0, 1),
        Jugador("Raúl de Tomás", 9, 7, 0, 3)
    ]

    rayo = Equipo(
        nombre="Rayo Vallecano",
        estadio="Vallecas",
        fundacion=1924,
        jugadores=rayo_jugadores,
        puntos=45,
        partidos_ganados=11,
        partidos_perdidos=12,
        partidos_empatados=11
    )

    # ============================
    # CELTA DE VIGO
    # ============================
    celta_jugadores = [
        Jugador("Vicente Guaita", 13, 0, 0, 0),
        Jugador("Óscar Mingueza", 3, 1, 0, 4),
        Jugador("Carl Starfelt", 2, 1, 0, 3),
        Jugador("Unai Núñez", 4, 0, 0, 2),
        Jugador("Manu Sánchez", 23, 0, 0, 3),
        Jugador("Fran Beltrán", 8, 2, 0, 5),
        Jugador("Luca de la Torre", 14, 1, 0, 3),
        Jugador("Iago Aspas", 10, 9, 0, 2),
        Jugador("Jørgen Strand Larsen", 18, 7, 0, 3),
        Jugador("Borja Iglesias", 7, 5, 0, 2),
        Jugador("Tadeo Allende", 11, 3, 0, 1)
    ]

    celta = Equipo(
        nombre="RC Celta",
        estadio="Balaídos",
        fundacion=1923,
        jugadores=celta_jugadores,
        puntos=43,
        partidos_ganados=11,
        partidos_perdidos=13,
        partidos_empatados=10
    )

    # ============================
    # MALLORCA
    # ============================
    mallorca_jugadores = [
        Jugador("Predrag Rajković", 1, 0, 0, 1),
        Jugador("Pablo Maffeo", 23, 1, 0, 6),
        Jugador("Martin Valjent", 24, 2, 0, 4),
        Jugador("Antonio Raíllo", 21, 1, 0, 3),
        Jugador("Jaume Costa", 11, 0, 0, 2),
        Jugador("Samú Costa", 12, 2, 0, 5),
        Jugador("Sergi Darder", 10, 3, 0, 3),
        Jugador("Dani Rodríguez", 14, 4, 0, 4),
        Jugador("Antonio Sánchez", 18, 1, 0, 2),
        Jugador("Vedat Muriqi", 7, 8, 0, 3),
        Jugador("Cyle Larin", 17, 5, 0, 1)
    ]

    mallorca = Equipo(
        nombre="RCD Mallorca",
        estadio="Son Moix",
        fundacion=1916,
        jugadores=mallorca_jugadores,
        puntos=41,
        partidos_ganados=10,
        partidos_perdidos=13,
        partidos_empatados=11
    )

    # ============================
    # LAS PALMAS
    # ============================
    laspalmas_jugadores = [
        Jugador("Álvaro Valles", 13, 0, 0, 1),
        Jugador("Álex Suárez", 4, 1, 0, 4),
        Jugador("Mika Mármol", 15, 0, 0, 3),
        Jugador("Sergi Cardona", 3, 0, 0, 2),
        Jugador("Julián Araujo", 2, 1, 0, 3),
        Jugador("Máximo Perrone", 20, 2, 0, 4),
        Jugador("Kirian Rodríguez", 5, 3, 0, 5),
        Jugador("Alberto Moleiro", 10, 4, 0, 2),
        Jugador("Munir El Haddadi", 17, 5, 0, 3),
        Jugador("Sandro Ramírez", 9, 6, 0, 2),
        Jugador("Marc Cardona", 18, 4, 0, 1)
    ]

    laspalmas = Equipo(
        nombre="UD Las Palmas",
        estadio="Gran Canaria",
        fundacion=1949,
        jugadores=laspalmas_jugadores,
        puntos=38,
        partidos_ganados=9,
        partidos_perdidos=14,
        partidos_empatados=11
    )

    # ============================
    # ALAVÉS
    # ============================
    alaves_jugadores = [
        Jugador("Antonio Sivera", 1, 0, 0, 0),
        Jugador("Nahuel Tenaglia", 14, 0, 0, 4),
        Jugador("Abdel Abqar", 5, 2, 0, 3),
        Jugador("Rubén Duarte", 3, 0, 0, 2),
        Jugador("Javi López", 27, 1, 0, 3),
        Jugador("Antonio Blanco", 8, 1, 0, 5),
        Jugador("Jon Guridi", 18, 3, 0, 4),
        Jugador("Ander Guevara", 6, 0, 0, 3),
        Jugador("Luis Rioja", 11, 4, 0, 2),
        Jugador("Samu Omorodion", 19, 7, 0, 1),
        Jugador("Kike García", 15, 5, 0, 3)
    ]

    alaves = Equipo(
        nombre="Deportivo Alavés",
        estadio="Mendizorroza",
        fundacion=1921,
        jugadores=alaves_jugadores,
        puntos=36,
        partidos_ganados=9,
        partidos_perdidos=15,
        partidos_empatados=10
    )

    # ============================
    # CREACIÓN DE LA LIGA
    # ============================
    liga = Liga("Liga Española", [
        barca, madrid, atletico, realsociedad, athletic,
        villarreal, betis, valencia, sevilla, getafe,
        osasuna, rayo, celta, mallorca, laspalmas, alaves
    ])

    print(liga)

if __name__ == "__main__":
    main()
