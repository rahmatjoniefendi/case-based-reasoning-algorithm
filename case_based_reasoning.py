def tentukan_bobot_tingkatan_gejala(tingkatan_gejala):
    bobot = [(b / 100) for b in tingkatan_gejala.values()]
    return bobot

def print_bobot_gejala(tingkatan_gejala_mempengaruhi_penyakit):
    print('PENENTUAN BOBOT GEJALA :')
    for tingkatan, bobot in tingkatan_gejala_mempengaruhi_penyakit.items():
        print('\tGEJALA {}\t:{}%, JADI BOBOT(W) {}\t= {}'.format(
			tingkatan,
			bobot,
			tingkatan,
			bobot / 100)
        )

def print_bobot_gejala_per_penyakit(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                                    tingkatan_gejala_mempengaruhi_penyakit):
    
    print('PENENTUAN BOBOT GEJALA MASING-MASING PENYAKIT :\n\n')

    for penyakit in klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala:
        print('\t' + penyakit + '\n')

        print('\t+---------------------+---------------------+---------------------+')
        print('\t|        GEJALA       |       TINGKATAN     |         BOBOT       |')
        print('\t+---------------------+---------------------+---------------------+')

        for tingkatan in klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala[penyakit]:
            for gejala in klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala[penyakit][tingkatan]:
                print('\t|{}|{}|{}|'.format(str(gejala).ljust(21),
                                            str(tingkatan).ljust(21),
                                            str(tingkatan_gejala_mempengaruhi_penyakit[tingkatan] / 100).ljust(21))
				      )
        print('\t+---------------------+---------------------+---------------------+\n\n')

def tentukan_bobot_gejala_per_penyakit(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala, tingkatan_gejala_mempengaruhi_penyakit):
    bobot_gejala_per_penyakit = {}

    for penyakit in klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala:
        bobot_gejala_per_penyakit[penyakit] = []
        for tingkatan in klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala[penyakit]:
            for gejala in klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala[penyakit][tingkatan]:
                bobot_gejala_per_penyakit[penyakit].append([gejala, tingkatan, tingkatan_gejala_mempengaruhi_penyakit[tingkatan] / 100])
    return bobot_gejala_per_penyakit

def jumlahkan_bobot_suatu_penyakit(penyakit, bobot_gejala_per_penyakit):
    hasil = 0
    for p in bobot_gejala_per_penyakit[penyakit]:
        hasil += p[2]
    return hasil
		
def tentukan_bobot_dan_tingkatan_gejala_dari_fakta(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                                                   tingkatan_gejala_mempengaruhi_penyakit,
                                                   jawaban_pengguna):
    
	bobot_fakta = {}

	for penyakit in klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala:
		for tingkatan in klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala[penyakit]:
			for gejala in jawaban_pengguna:
				if gejala in klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala[penyakit][tingkatan]:
					bobot_fakta[gejala] = [tingkatan, tingkatan_gejala_mempengaruhi_penyakit[tingkatan] / 100]
	return bobot_fakta


def print_fakta(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                tingkatan_gejala_mempengaruhi_penyakit,
                jawaban_pengguna):

    print('FAKTA BARU BERDASARKAN JAWABAN PASIEN/PENGGUNA :\n\n')

    
    print('\t+---------------------+---------------------+---------------------+')
    print('\t|        GEJALA       |       TINGKATAN     |         BOBOT       |')
    print('\t+---------------------+---------------------+---------------------+')

    for gejala, tingkatan_dan_fakta in tentukan_bobot_dan_tingkatan_gejala_dari_fakta(
        klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
        tingkatan_gejala_mempengaruhi_penyakit,
        jawaban_pengguna).items():

        print('\t|{}|{}|{}|'.format(str(gejala).ljust(21),
                                    str(tingkatan_dan_fakta[0]).ljust(21),
                                    str(tingkatan_dan_fakta[1]).ljust(21)))
    print('\t+---------------------+---------------------+---------------------+\n\n')


def cari_hasil(bobot_dan_tingkatan_gejala_dari_fakta, bobot_gejala_per_penyakit, gejala_user, digit=6):
    indeks_gejala_yang_sama = []
    kesamaan = []
    hasil = []
    bobot = []
    pykt = []
    
    penyakit_dan_bobot = {}

    print('PERHITUNGAN SIMILARITAS :\n\n')
    
    i = 0
    for penyakit in bobot_gejala_per_penyakit:
        indeks_gejala_yang_sama.append([])
        kesamaan.append([])
        bobot.append([])
        
        print('\tGEJALA YANG SAMA DAN TIDAK SAMA ANTARA FAKTA BARU DENGAN GEJALA PENYAKIT : ' +str(penyakit) + ' ADALAH : \n\n')
        
        for p in bobot_gejala_per_penyakit[penyakit]:
            if p[0] in bobot_dan_tingkatan_gejala_dari_fakta:
                print('\t\t' +str(p[0]) + ' - SAMA')
                
                index = 1
                indeks_gejala_yang_sama[i].append(index)
                
                kesamaan[i].append(index * p[2])
                bobot[i].append(p[2])
                
            else:
                print('\t\t' +str(p[0]) + ' - TIDAK SAMA')
                index = 0
                indeks_gejala_yang_sama[i].append(index)
                
                kesamaan[i].append(index * p[2])
                bobot[i].append(p[2])

        pykt.append(penyakit)
        
        hasil.append(sum(kesamaan[i]) / jumlahkan_bobot_suatu_penyakit(penyakit, bobot_gejala_per_penyakit))
        print('\n')
        i += 1
    
    for p in range(len(bobot)):
        penyakit_dan_bobot[str(pykt[p])] = hasil[p]
        print('\t' + str(pykt[p]) + '\n')
        print('\t\t', end='')
        
        for indeks, b in zip(indeks_gejala_yang_sama[p], bobot[p]):
            print('\t( {} * {} )'.format(indeks, b), end=' + ')

        print(' = {} '.format(hasil[p]))
        print('\tSimiliarity {} = ---------------------------------------------------------------------------'.format(str(p+1)))

        print('\t\t\t' + ' + '.join([str(k) for k in bobot[p]]))
        print('\n\n\n')
    
    probabilitas_penyakit_terurut = dict(sorted(penyakit_dan_bobot.items(), key=lambda x : x[1], reverse=True))

    print('KESIMPULAN :\n\n')

    print('\tGEJALA : {}\n\n'.format(', '.join([g for g in gejala_user])))
    
    print('\t+---------------------+--------------------+---------------------+')
    print('\t|       PENYAKIT      |    SIMILARITAS(%)  |      SIMILARITAS    |')
    print('\t+---------------------+--------------------+---------------------+')
    
    for key, item in probabilitas_penyakit_terurut.items():
        nilai_similiarity_dlm_persen = round(item, digit) * 100
        
        print('\t|{}|{}|{}|'.format(str(key).ljust(21),
                                    (str(nilai_similiarity_dlm_persen) + '%') .ljust(20),
                                    str(item).ljust(21)))
    print('\t+---------------------+--------------------+---------------------+')

def hitung_kesamaan_fakta_baru_dengan_penyakit(bobot_dan_tingkatan_gejala_dari_fakta, bobot_gejala_per_penyakit):
	indeks_gejala_yang_sama = []
	kesamaan = []
	bobot = []
	hasil = []
	pykt = []
	i = 0
	for penyakit in bobot_gejala_per_penyakit:
		indeks_gejala_yang_sama.append([])
		kesamaan.append([])
		bobot.append([])
		pykt.append([])

		for p in bobot_gejala_per_penyakit[penyakit]:
			if p[0] in bobot_dan_tingkatan_gejala_dari_fakta:
				print('GEJALA YANG SAMA DARI JAWABAN USER DENGAN GEJALA PENYAKIT : ' +str(penyakit) + ' ADALAH ' + str(p[0]))

				index = 1
				indeks_gejala_yang_sama[i].append(index)

				kesamaan[i].append(index * p[2])
				bobot[i].append(p[2])
				pykt.append(penyakit)
			else:
				index = 0
				indeks_gejala_yang_sama[i].append(index)

				kesamaan[i].append(index * p[2])
				bobot[i].append(p[2])
				pykt.append(penyakit)

		hasil.append(sum(kesamaan[i]) / jumlahkan_bobot_suatu_penyakit(penyakit, bobot_gejala_per_penyakit))
		print(sum(kesamaan[i]) / jumlahkan_bobot_suatu_penyakit(penyakit, bobot_gejala_per_penyakit))

		print('\n')
		i += 1

	print('PENYAKIT : ' + str(pykt))
	print()
	print('INDEKS YANG SAMA : ' + str(indeks_gejala_yang_sama))
	print()
	print('KESAMAAN: ' + str(kesamaan))
	print()
	print('BOBOT: ' + str(bobot))
	print()
	print('HASIL: ' + str(hasil))
	print()

	return kesamaan

def demo_1():

    tingkatan_gejala_mempengaruhi_penyakit = {
        'RINGAN' : 30, # 30%
        'SEDANG' : 55, # 55%
        'BERAT'  : 80  # 80%
    }

    klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala = {
        'P1' : {
            'RINGAN' : ['G1', 'G2', 'G3'],

            'SEDANG' : ['G4', 'G5'],

            'BERAT' : ['G6']
	    },

        'P2' : {
            'RINGAN' : ['G1', 'G3'],

            'SEDANG' : ['G5', 'G7'],

            'BERAT' : ['G8', 'G9']
	    },

        'P3' : {
            'RINGAN' : ['G1', 'G2', 'G3'],

            'SEDANG' : ['G5', 'G7'],

            'BERAT' : ['G10', 'G11', 'G12']
        }
    }

    jawaban_pengguna = [
        'G1',
        'G2',
        'G3',
        'G5',
        'G6',
        'G7',
        'G9',
        'G12'
    ]

    print('+-----------------------------------------------------------------------+')
    print('|                     PROSES CASE BASED REASONING                       |')
    print('+-----------------------------------------------------------------------+')
    
    print_bobot_gejala(tingkatan_gejala_mempengaruhi_penyakit)

    print('\n')

    ####################################################################################

    print_bobot_gejala_per_penyakit(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                                    tingkatan_gejala_mempengaruhi_penyakit)

    ####################################################################################

    print_fakta(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                tingkatan_gejala_mempengaruhi_penyakit,
                jawaban_pengguna)

    ####################################################################################

    bgpp = tentukan_bobot_gejala_per_penyakit(
        klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
        tingkatan_gejala_mempengaruhi_penyakit)


    btgf = tentukan_bobot_dan_tingkatan_gejala_dari_fakta(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                                                   tingkatan_gejala_mempengaruhi_penyakit,
                                                   jawaban_pengguna)

    cari_hasil(btgf, bgpp, jawaban_pengguna, digit=10000000000)

def demo_2():

    tingkatan_gejala_mempengaruhi_penyakit = {
        'RINGAN' : 35, # 35%
        'SEDANG' : 60, # 60%
        'BERAT'  : 85  # 85%
    }

    klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala = {
        
        'P1 (DBD)' : {
            
            'RINGAN' : ['G4', 'G15', 'G6', 'G12'],

            'SEDANG' : ['G9', 'G18'],

            'BERAT' :  ['G19', 'G3']
	    },

        'P2 (MALARIA)' : {
            
            'RINGAN' : ['G2', 'G4', 'G6', 'G10', 'G11'],

            'SEDANG' : ['G5', 'G7', 'G8'],

            'BERAT' :  ['G16', 'G3']
	    },

        'P3 (CHIKUNGUYA)' : {
            
            'RINGAN' : ['G4', 'G6', 'G11'],

            'SEDANG' : ['G1', 'G13', 'G14'],

            'BERAT' :  ['G16', 'G17']
        }
    }

    jawaban_pengguna = [
        'G1',
        'G3',
        'G5',
        'G6',
        'G8',
        'G10',
        'G11',
	    'G12',
        'G15',
	    'G16'
    ]

    print('+-----------------------------------------------------------------------+')
    print('|                     PROSES CASE BASED REASONING                       |')
    print('+-----------------------------------------------------------------------+')
    
    print_bobot_gejala(tingkatan_gejala_mempengaruhi_penyakit)

    print('\n')

    ####################################################################################

    print_bobot_gejala_per_penyakit(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                                    tingkatan_gejala_mempengaruhi_penyakit)

    ####################################################################################

    print_fakta(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                tingkatan_gejala_mempengaruhi_penyakit,
                jawaban_pengguna)

    ####################################################################################

    bgpp = tentukan_bobot_gejala_per_penyakit(
        klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
        tingkatan_gejala_mempengaruhi_penyakit)


    btgf = tentukan_bobot_dan_tingkatan_gejala_dari_fakta(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                                                   tingkatan_gejala_mempengaruhi_penyakit,
                                                   jawaban_pengguna)

    cari_hasil(btgf, bgpp, jawaban_pengguna, digit=6)

def demo_3():

    tingkatan_gejala_mempengaruhi_penyakit = {
        'RINGAN' : 35, # 35%
        'SEDANG' : 60, # 60%
        'BERAT'  : 85  # 85%
    }

    klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala = {
        
        'P1 (INTERTRIGO)' : {
            
            'RINGAN' : ['G5', 'G11'],

            'SEDANG' : ['G12', 'G15'],

            'BERAT' :  ['G6', 'G17']
	    },

        'P2 (MILIARIA)' : {
            
            'RINGAN' : ['G1', 'G3', 'G13', 'G16'],

            'SEDANG' : ['G2', 'G20'],

            'BERAT' :  ['G4', 'G14']
	    },

        'P3 (SEBOREA)' : {
            
            'RINGAN' : ['G18'],

            'SEDANG' : ['G19', 'G22'],

            'BERAT' :  ['G7']
        },

        'P4 (EKSIM)' : {
            
            'RINGAN' : ['G5', 'G9'],

            'SEDANG' : ['G8', 'G21'],

            'BERAT' :  ['G6', 'G10', 'G17']
        }
    }

    jawaban_pengguna = [
        'G1',
        'G2',
        'G3',
        'G5',
        'G8',
        'G9',
        'G11',
        'G12',
        'G13',
        'G15',
        'G16',
        'G17',
        'G20',
        'G21'
    ]

    print('+-----------------------------------------------------------------------+')
    print('|                     PROSES CASE BASED REASONING                       |')
    print('+-----------------------------------------------------------------------+')
    
    print_bobot_gejala(tingkatan_gejala_mempengaruhi_penyakit)

    print('\n')

    ####################################################################################

    print_bobot_gejala_per_penyakit(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                                    tingkatan_gejala_mempengaruhi_penyakit)

    ####################################################################################

    print_fakta(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                tingkatan_gejala_mempengaruhi_penyakit,
                jawaban_pengguna)

    ####################################################################################

    bgpp = tentukan_bobot_gejala_per_penyakit(
        klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
        tingkatan_gejala_mempengaruhi_penyakit)


    btgf = tentukan_bobot_dan_tingkatan_gejala_dari_fakta(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                                                   tingkatan_gejala_mempengaruhi_penyakit,
                                                   jawaban_pengguna)

    cari_hasil(btgf, bgpp, jawaban_pengguna, digit=6)    

def demo_4():
    
    tingkatan_gejala_mempengaruhi_penyakit = {
        'RINGAN' : 25, # 25%
        'SEDANG' : 55, # 55%
        'BERAT'  : 85  # 85%
    }

    klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala = {
        
        'P1 (MALARIA TROPICA)' : {
            
            'RINGAN' : ['G3', 'G8', 'G9'],

            'SEDANG' : ['G4', 'G10', 'G11'],

            'BERAT' :  ['G6', 'G12']
	    },

        'P2 (MALARIA TERTIANA)' : {
            
            'RINGAN' : ['G2', 'G8'],

            'SEDANG' : ['G7', 'G11'],

            'BERAT' :  ['G1', 'G12']
	    },

        'P3 (MALARIA QUARTANA)' : {
            
            'RINGAN' : ['G2', 'G8'],

            'SEDANG' : ['G7', 'G11'],

            'BERAT' :  ['G5', 'G12']
        }
    }

    jawaban_pengguna = [
        'G1',
        'G2',
        'G3',

        'G6',
        'G7',
        'G8',
        'G9',
        
        'G11',
        'G12'
    ]

    print('+-----------------------------------------------------------------------+')
    print('|                     PROSES CASE BASED REASONING                       |')
    print('+-----------------------------------------------------------------------+')
    
    print_bobot_gejala(tingkatan_gejala_mempengaruhi_penyakit)

    print('\n')

    ####################################################################################

    print_bobot_gejala_per_penyakit(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                                    tingkatan_gejala_mempengaruhi_penyakit)

    ####################################################################################

    print_fakta(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                tingkatan_gejala_mempengaruhi_penyakit,
                jawaban_pengguna)

    ####################################################################################

    bgpp = tentukan_bobot_gejala_per_penyakit(
        klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
        tingkatan_gejala_mempengaruhi_penyakit)


    btgf = tentukan_bobot_dan_tingkatan_gejala_dari_fakta(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                                                   tingkatan_gejala_mempengaruhi_penyakit,
                                                   jawaban_pengguna)

    cari_hasil(btgf, bgpp, jawaban_pengguna, digit=6)

def demo_5():

    tingkatan_gejala_mempengaruhi_penyakit = {
        'RINGAN' : 30, # 30%
        'SEDANG' : 60, # 60%
        'BERAT'  : 80  # 80%
    }

    klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala = {
        
        'P1 (GASTRITIS)' : {
            
            'RINGAN' : ['G1', 'G9', 'G11'],

            'SEDANG' : ['G2', 'G6'],

            'BERAT' :  ['G8']
	    },

        'P2 (DISPEPSIA)' : {
            
            'RINGAN' : ['G1', 'G9', 'G11', 'G14'],

            'SEDANG' : ['G2'],

            'BERAT' :  ['G3']
	    },

        'P3 (GERD)' : {
            
            'RINGAN' : ['G1'],

            'SEDANG' : ['G2', 'G5'],

            'BERAT' :  ['G3', 'G4']
        },

        'P4 (TUKAK LAMBUNG)' : {
            
            'RINGAN' : ['G1'],

            'SEDANG' : ['G2', 'G13'],

            'BERAT' :  ['G3', 'G7', 'G12', 'G10']
        },
    }

    jawaban_pengguna = [
        'G1',
        'G2',
        'G3',
        'G5'
    ]

    print('+-----------------------------------------------------------------------+')
    print('|                     PROSES CASE BASED REASONING                       |')
    print('+-----------------------------------------------------------------------+')
    
    print_bobot_gejala(tingkatan_gejala_mempengaruhi_penyakit)

    print('\n')

    ####################################################################################

    print_bobot_gejala_per_penyakit(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                                    tingkatan_gejala_mempengaruhi_penyakit)

    ####################################################################################

    print_fakta(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                tingkatan_gejala_mempengaruhi_penyakit,
                jawaban_pengguna)

    ####################################################################################

    bgpp = tentukan_bobot_gejala_per_penyakit(
        klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
        tingkatan_gejala_mempengaruhi_penyakit)


    btgf = tentukan_bobot_dan_tingkatan_gejala_dari_fakta(klasifikasi_gejala_penyakit_berdasarkan_tingkatan_gejala,
                                                   tingkatan_gejala_mempengaruhi_penyakit,
                                                   jawaban_pengguna)

    cari_hasil(btgf, bgpp, jawaban_pengguna, digit=6)
    
if __name__ == '__main__':
    demo_5()