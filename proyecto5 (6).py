Regiónes2 = {"01":"Tarapaca","02":"Antofagasta","03":"Atacama","04":"Coquimbo","05":"Valparaiso","06":"OHiggins","07":"Maule","08":"Biobio","09":"La Araucanía",
"10":"Los Lagos","11":"Aysen","12":"Magallanes","13":"Metropolitana","14":"Los Rios","15":"Arica y Parinacota","16":"Ñuble"}
def tara():
        from matplotlib import pyplot
        paca = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12018.4,12092.3,12207.5,12277.3,12356.7,12418.3,12477.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Tarapaca")
        pyplot.bar (paca, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def anto():
        from matplotlib import pyplot
        asta = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8631.4,8699.5,8794.3,8865.9,8932.2,9000.9,9065.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Antofagasta")
        pyplot.bar (asta, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def atac():
        from matplotlib import pyplot
        ama = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7561.6,7709.7,7887.9,7998.2,8131.3,8210.1,8355.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Atacama")
        pyplot.bar (ama, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def coqu():
        from matplotlib import pyplot
        imbo = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5764.8,5879.8,6032.4,6147.9,6247.4,6329.5,6404.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Coquimbo")
        pyplot.bar (imbo, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def valpa():
        from matplotlib import pyplot
        aiso = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7535.4,7661.4,7815.9,7929.7,8047.6,8139.8,8230.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Valparaiso")
        pyplot.bar (aiso, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def ohig():
        from matplotlib import pyplot
        gins = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7506.7,7628.0,7769.9,7869.0,7953.8,8020.7,8078.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región OHiggins")
        pyplot.bar (gins, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def ma():
        from matplotlib import pyplot
        ule = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7535.4,7661.4,7815.9,7929.7,8047.6,8139.8,8230.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Maule")
        pyplot.bar (ule, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def bi():
        from matplotlib import pyplot
        bio = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9999.8,10111.3,10241.2,10334.4,10437.1,10516.1,10596.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Biobio")
        pyplot.bar (bio, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def laara():
        from matplotlib import pyplot
        aria= ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9599.2,9723.4,9864.3,9986.2,10104.3,10215.4,10310.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región La Araucanía")
        pyplot.bar (aria,height=Valores,color=colores,width=0.5)
        pyplot.show ()
def los():
        from matplotlib import pyplot
        gos= ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10537.3,10642.1,10764.9,10845.6,10925.4,11016.0,11092.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Los Lagos")
        pyplot.bar (gos,height=Valores,color=colores,width=0.5)
        pyplot.show ()
def ay():
        from matplotlib import pyplot
        sen= ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7558.5,7776.5,8041.2,8223.9,8358.1,8477.4,8579.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Aysen")
        pyplot.bar (sen,height=Valores,color=colores,width=0.5)
        pyplot.show ()
def maga():
        from matplotlib import pyplot
        llane= ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [17685.9,17747.6,17860.9,17942.2,18005.0,18042.0,18094.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Magallanes")
        pyplot.bar (llane,height=Valores,color=colores,width=0.5)
        pyplot.show ()
def metro():
        from matplotlib import pyplot
        tana= ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9053.8,9202.5,9365.4,9476.5,9583.3,9664.1,9736.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Metropolitana")
        pyplot.bar (tana,height=Valores,color=colores,width=0.5)
        pyplot.show ()
def rios():
        from matplotlib import pyplot
        ri= ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11470.2,11666.6,11910.0,12066.7,12258.7,12428.9,12604.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Los Rios")
        pyplot.bar (ri,height=Valores,color=colores,width=0.5)
        pyplot.show ()
def ari():
        from matplotlib import pyplot
        cota = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10617.2,10728.3,10886.9,10999.6,11151.5,11248.7,11357.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Arica y Parinacota")
        pyplot.bar (cota, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def ñu():
        from matplotlib import pyplot
        ble = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8052.8,8173.0,8283.2,8366.7,8448.2,8513.5,8573.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en la región Ñuble")
        pyplot.bar (ble, height=Valores,color=colores,width=0.5)
        pyplot.show ()

Comunas = {"15101":"Arica","15102":"Camarones","15202":"General Lagos","15201":"Putre","01107":"Alto Hospicio",
"01402":"Camina","01403":"Colchane","01404":"Huara","01101":"Iquique","01405":"Pica","01401":"PozoAlmonte",
"02101":"Antofagasta","02201":"Calama","02302":"MariaElena","02102":"Mejillones","02202":"Ollague",
"02203":"SanPedroDeAtacama","02103":"SierraGorda","02104":"Taltal","02301":"Tocopilla","03302":"Alto del Carmen",
"03102":"Caldera","03201":"Chanaral","03101":"Copiapo","03202":"Diego de Almagro","03303":"Freirina","03304":"Huasco"
,"03103":"Tierra Amarilla","03301":"Vallenar","04103":"Andacollo","04202":"Canela","04302":"Combarbala","04102":"Coquimbo",
"04201":"Illapel","04104":"La Higuera","04101":"La Serena","04203":"Los Vilos","04303":"Monte Patria","04301":"Ovalle",
"04105":"Paiguano","04304":"Punitaqui","04305":"Rio Hurtado","04204":"Salamanca","04106":"Vicuna","05602":"Algarrobo",
"05402":"Cabildo","05502":"Calera","05302":"CalleLarga","05603":"Cartagena","05102":"Casablanca","05702":"Catemu",
"Concon":"05103","ElQuisco":"05604", "ElTabo":"05605", "Hijuelas":"05503","IslaDePascua":"05201","JuanFernandez":"05104",
"05504":"LaCruz","05401":"LaLigua","05802":"Limache","05703":"Llayllay","05301":"LosAndes","05506":"Nogales","05803":"Olmue",
"Panquehue":"05704","Papudo":"05403","Petorca":"05403","Punchuncavi":"05105","Putaendo":"05705","Quillota":"05501","Quilpue":"05801",
"05107":"Quintero","05303":"Rinconada","05601":"SanAntonio","05304":"SanEsteban","05701":"SanFelipe","05706":"SantaMaria",
"05606":"SantoDomingo","05101":"Valpaiso","05804":"VillaAlemana","05804":"ViñaDelMar","05405":"Zapallar","13502":"Alhue",
"13402":"Buin","13403":"Calera de Tango","13102":"Cerrillos","13103":"Cerro Navia","13301":"Colina","13104":"Conchali",
"13503":"Curacavi","13105":"El Bosque","13602":"El Monte","13106":"Estacion Central","13107":"Huechuraba","13108":"Independencia",
"13603":"Isla de Maipo","13109":"La Cisterna","13110":"La Florida","13111":"La Granja","13112":"La Pintana","13113":"La Reina",
"13302":"Lampa","13114":"Las Condes","13115":"Lo Barnechea","13116":"Lo Espejo","13117":"Lo Prado","13118":"Macul","13119":"Maipu",
"13504":"Maria Pinto","13501":"Melipilla","13120":"Nunoa","13604":"Padre Hurtado","13404":"Paine","13121":"Pedro Aguirre Cerda",
"13605":"Penaflor","13122":"Penalolen","13202":"Pirque","13123":"Providencia","13124":"Pudahuel","13201":"Puente Alto",
"13125":"Quilicura","13126":"Quinta Normal","13127":"Recoleta","13128":"Renca","13401":"San Bernardo",
"13129":"San Joaquin","13203":"San Jose de Maipo","13130":"San Miguel","13505":"San Pedro","13131":"San Ramon",
"13101":"Santiago","13601":"Talagante","13303":"Tiltil","13132":"Vitacura","06302":"Chepica","06303":"Chimbarongo",
"06102":"Codegua","06103":"Coinco","06104":"Coltauco","06105":"Donihue","06106":"Graneros",
"06202":"La Estrella","06107":"Las Cabras","06203":"Litueche","06304":"Lolol","06108":"Machali","06109":"Malloa",
"06204":"Marchihue","06110":"Mostazal","06305":"Nancagua","06205":"Navidad","06111":"Olivar","06306":"Palmilla",
"06206":"Paredones","06307":"Peralillo","06112":"Peumo","06113":"Pichidegua","06201":"Pichilemu","06308":"Placilla",
"06309":"Pumanque","06114":"Quinta de Tilcoco","06101":"Rancagua","06115":"Rengo","06116":"Requinoa","06301":"San Fernando",
"06117":"San Vicente","06310":"Santa Cruz","07201":"Cauquenes","07202":"Chanco","07402":"Colbun","07102":"Constitucion","07103":"Curepto",
"07301":"Curico","07104":"Empedrado","07302":"Hualane","07303":"Licanten","07401":"Linares","07403":"Longavi","07105":"Maule",
"07304":"Molina","07404":"Parral","07106":"Pelarco","07203":"Pelluhue","07107":"Pencahue","07305":"Rauco","07405":"Retiro",
"07108":"Rio Claro","07306":"Romeral","07307":"Sagrada Familia","07109":"San Clemente","07406":"San Javier","07110":"San Rafael",
"07101":"Talca","07308":"Teno","07309":"Vichuquen","07407":"Villa Alegre","07408":"Yerbas Buenas","16102":"Bulnes","16101":"Chillan",
"16103":"Chillan Viejo","16202":"Cobquecura","16203":"Coelemu","16302":"Coihueco","16104":"El Carmen","16204":"Ninhue","16303":"Niquen",
"16105":"Pemuco","16106":"Pinto","16205":"Portezuelo","16107":"Quillon","16201":"Quirihue","16206":"Ranquil","16304":"San Fabian","16108":"San Ignacio",
"16305":"San Nicolas","16207":"Treguaco","16109":"Yungay","08314":"Alto Biobio","08302":"Antuco","08202":"Arauco","08303":"Cabrero","08203":"Canete",
"08103":"Chiguayante","08101":"Concepcion","08204":"Contulmo","08102":"Coronel","08205":"Curanilahue","08104":"Florida","08112":"Hualpen","08105":"Hualqui",
"08304":"Laja","08201":"Lebu","08206":"Los Alamos","08301":"Los Angeles","08106":"Lota","08305":"Mulchen","08306":"Nacimiento","08307":"Negrete","08107":"Penco",
"08308":"Quilaco","08309":"Quilleco","08108":"San Pedro de la Paz","08310":"San Rosendo","08311":"Santa Barbara","08109":"Santa Juana","08110":"Talcahuano","08207":"Tirua",
"08111":"Tome","08312":"Tucapel","08313":"Yumbel","09201":"Angol","09102":"Carahue","09121":"Cholchol","09202":"Collipulli","09103":"Cunco","09203":"Curacautin","09104":"Curarrehue",
"09204":"Ercilla","09105":"Freire","09106":"Galvarino","09107":"Gorbea","09108":"Lautaro","09109":"Loncoche","09205":"Lonquimay","09206":"Los Sauces","09207":"Lumaco","09110":"Melipeuco",
"09111":"Nueva Imperial","09112":"Padre Las Casas","09113":"Perquenco","09114":"Pitrufquen","09115":"Pucon","09208":"Puren","09209":"Renaico","09116":"Saavedra","09101":"Temuco","09117":"Teodoro Schmidt",
"09118":"Tolten","09210":"Traiguen","09211":"Victoria","09119":"Vilcun","09120":"Villarrica","14102":"Corral","14202":"Futrono","14201":"La Union","14203":"Lago Ranco","14103":"Lanco","14104":"Los Lagos",
"14105":"Mafil","14106":"Mariquina","14107":"Paillaco","14108":"Panguipulli","14204":"Rio Bueno","14101":"Valdivia","10202":"Ancud","10102":"Calbuco","10201":"Castro","10401":"Chaiten","10203":"Chonchi",
"10103":"Cochamo","10204":"Curaco de Velez","10205":"Dalcahue","10104":"Fresia","10105":"Frutillar","10402":"Futaleufu","10403":"Hualaihue","10107":"Llanquihue","10106":"Los Muermos","10108":"Maullin",
"10301":"Osorno","10404":"Palena","10101":"Puerto Montt","10302":"Puerto Octay","10109":"Puerto Varas","10206":"Puqueldon","10303":"Purranque","10304":"Puyehue","10207":"Queilen","10208":"Quellon",
"10209":"Quemchi","10210":"Quinchao","10305":"Rio Negro","10306":"San Juan de la Costa","10307":"San Pablo","11201":"Aysen","11401":"Chile Chico","11202":"Cisnes","11301":"Cochrane","11101":"Coyhaique",
"11203":"Guaitecas","11102":"Lago Verde","11302":"OHiggins","11402":"Rio Ibañez","11303":"Tortel","12202":"Antartica","12201":"Cabo de Hornos","12102":"Laguna Blanca","12401":"Natales","12301":"Porvenir",
"12302":"Primavera","12101":"Punta Arenas","12103":"Rio Verde","12104":"San Gregorio","12303":"Timaukel","12402":"Torres del Paine"}

AricayParinacota = {"Arica":"15101","Camarones": "15102", "General Lagos": "15202", "Putre": "15201"}
Tarapaca = { "Alto Hospicio":"01107", "Camina":"01402","Colchane":"01403","Huara":"01404",
"Iquique":"01101", "Pica":"01405","PozoAlmonte":"01401"}
Antofagasta ={"Antofagasta":"02101","Calama":"02201","MariaElena":"02302","Mejillones":"02102","Ollague":"02202",
"SanPedroDeAtacama":"02203","SierraGorda":"02103","Taltal":"02104","Tocopilla":"02301"}
Atacama = {"Alto del Carmen":"03302","Caldera":"03102","Chanaral":"03201","Copiapo":"03101","Diego de Almagro":"03202",
"Freirina":"03303","Huasco":"03304","Tierra Amarilla":"03103","Vallenar":"03301"}
Coquimbo ={"Andacollo":"04103","Canela":"04202","Combarbala":"04302","Coquimbo":"04102","Illapel":"04201",
"La Higuera":"04104","La Serena":"04101","Los Vilos":"04203","Monte Patria":"04303","Ovalle":"04301",
"Paiguano":"04105","Punitaqui":"04304","Rio Hurtado":"04305","Salamanca":"04204","Vicuna":"04106"}
Valparaiso = {"Algarrobo":"05602","Cabildo":"05402","Calera":"05502","CalleLarga":"05302","Cartagena":"05603",
"Casablanca":"05102","Catemu":"05702","Concon":"05103","ElQuisco":"05604", "ElTabo":"05605", "Hijuelas":"05503",
"IslaDePascua":"05201","JuanFernandez":"05104","LaCruz":"05504","LaLigua":"05401","Limache":"05802","Llayllay":"05703",
"LosAndes":"05301","Nogales":"05506","Olmue":"05803","Panquehue":"05704","Papudo":"05403","Petorca":"05403",
"Punchuncavi":"05105","Putaendo":"05705","Quillota":"05501","Quilpue":"05801","Quintero":"05107",
"Rinconada":"05303","SanAntonio":"05601","SanEsteban":"05304","SanFelipe":"05701","SantaMaria":"05706",
"SantoDomingo":"05606","Valpaiso":"05101","VillaAlemana":"05804","ViñaDelMar":"05804","Zapallar":"05405"}
Metropolitana = { "Alhue":"13502","Buin":"13402","Calera de Tango":"13403","Cerrillos":"13102","Cerro Navia":"13103",
"Colina":"13301","Conchali":"13104","Curacavi":"13503","El Bosque":"13105","El Monte":"13602","Estacion Central":"13106",
"Huechuraba":"13107","Independencia":"13108","Isla de Maipo":"13603","La Cisterna":"13109","La Florida":"13110","La Granja":"13111",
"La Pintana":"13112","La Reina":"13113","Lampa":"13302","Las Condes":"13114","Lo Barnechea":"13115","Lo Espejo":"13116",
"Lo Prado":"13117","Macul":"13118","Maipu":"13119","Maria Pinto":"13504","Melipilla":"13501","Nunoa":"13120",
"Padre Hurtado":"13604","Paine":"13404","Pedro Aguirre Cerda":"13121","Penaflor":"13605","Penalolen":"13122",
"Pirque":"13202","Providencia":"13123","Pudahuel":"13124","Puente Alto":"13201","Quilicura":"13125",
"Quinta Normal":"13126","Recoleta":"13127","Renca":"13128","San Bernardo":"13401","San Joaquin":"13129",
"San Jose de Maipo":"13203","San Miguel":"13130","San Pedro":"13505","San Ramon":"13131","Santiago":"13101",
"Talagante":"13601","Tiltil":"13303","Vitacura":"13132"}
O_Higgins = {"Chepica":"06302","Chimbarongo":"06303","Codegua":"06102","Coinco":"06103",
"Coltauco":"06104","Donihue":"06105","Graneros":"06106","    La Estrella":"06202","Las Cabras":"06107","Litueche":"06203",
"Lolol":"06304","Machali":"06108","Malloa":"06109","Marchihue":"06204","Mostazal":"06110","Nancagua":"06305","Navidad":"06205",
"Olivar":"06111","Palmilla":"06306","Paredones":"06206","Peralillo":"06307","Peumo":"06112","Pichidegua":"06113","Pichilemu":"06201",
"Placilla":"06308","Pumanque":"06309","Quinta de Tilcoco":"06114","Rancagua":"06101","Rengo":"06115","Requinoa":"06116",
"San Fernando":"06301","San Vicente":"06117","Santa Cruz":"06310"}
Maule = { "Cauquenes":"07201","Chanco":"07202","Colbun":"07402","Constitucion":"07102","Curepto":"07103","Curico":"07301",
"Empedrado":"07104","Hualane":"07302","Licanten":"07303","Linares":"07401","Longavi":"07403","Maule":"07105","Molina":"07304",
"Parral":"07404","Pelarco":"07106","Pelluhue":"07203","Pencahue":"07107","Rauco":"07305","Retiro":"07405","Rio Claro":"07108",
"Romeral":"07306","Sagrada Familia":"07307","San Clemente":"07109","San Javier":"07406","San Rafael":"07110","Talca":"07101",
"Teno":"07308","Vichuquen":"07309","Villa Alegre":"07407","Yerbas Buenas":"07408"}
Ñuble = { "Bulnes":"16102","Chillan":"16101","Chillan Viejo":"16103",
"Cobquecura":"16202","Coelemu":"16203","Coihueco":"16302","El Carmen":"16104","Ninhue":"16204",
"Niquen":"16303","Pemuco":"16105","Pinto":"16106","Portezuelo":"16205","Quillon":"16107","Quirihue":"16201",
"Ranquil":"16206","San Fabian":"16304","San Ignacio":"16108","San Nicolas":"16305","Treguaco":"16207","Yungay":"16109"}
Biobio = {"Alto Biobio":"08314","Antuco":"08302","Arauco":"08202","Cabrero":"08303","Canete":"08203","Chiguayante":"08103",
"Concepcion":"08101","Contulmo":"08204","Coronel":"08102","Curanilahue":"08205","Florida":"08104","Hualpen":"08112","Hualqui":"08105",
"Laja":"08304","Lebu":"08201","Los Alamos":"08206","Los Angeles":"08301","Lota":"08106","Mulchen":"08305","Nacimiento":"08306",
"Negrete":"08307","Penco":"08107","Quilaco":"08308","Quilleco":"08309","San Pedro de la Paz":"08108","San Rosendo":"08310",
"Santa Barbara":"08311","Santa Juana":"08109","Talcahuano":"08110","Tirua":"08207","Tome":"08111","Tucapel":"08312","Yumbel":"08313"}
La_Araucania = {"Angol":"09201","Carahue":"09102","Cholchol":"09121","Collipulli":"09202","Cunco":"09103","Curacautin":"09203",
"Curarrehue":"09104","Ercilla":"09204","Freire":"09105","Galvarino":"09106","Gorbea":"09107","Lautaro":"09108","Loncoche":"09109",
"Lonquimay":"09205","Los Sauces":"09206","Lumaco":"09207","Melipeuco":"09110","Nueva Imperial":"09111","Padre Las Casas":"09112",
"Perquenco":"09113","Pitrufquen":"09114","Pucon":"09115","Puren":"09208","Renaico":"09209","Saavedra":"09116","Temuco":"09101",
"Teodoro Schmidt":"09117","Tolten":"09118","Traiguen":"09210","Victoria":"09211","Vilcun":"09119","Villarrica":"09120"}
Los_Rios =  { "Corral":"14102","Futrono":"14202","La Union":"14201","Lago Ranco":"14203","Lanco":"14103","Los Lagos":"14104",
"Mafil":"14105","Mariquina":"14106","Paillaco":"14107","Panguipulli":"14108","Rio Bueno":"14204","Valdivia":"14101"}
Los_Lagos = { "Ancud":"10202","Calbuco":"10102","Castro":"10201","Chaiten":"10401","Chonchi":"10203","Cochamo":"10103",
"Curaco de Velez":"10204","Dalcahue":"10205","Fresia":"10104","Frutillar":"10105","Futaleufu":"10402","Hualaihue":"10403",
"Llanquihue":"10107","Los Muermos":"10106","Maullin":"10108","Osorno":"10301","Palena":"10404","Puerto Montt":"10101",
"Puerto Octay":"10302","Puerto Varas":"10109","Puqueldon":"10206","Purranque":"10303","Puyehue":"10304","Queilen":"10207",
"Quellon":"10208","Quemchi":"10209","Quinchao":"10210","Rio Negro":"10305","San Juan de la Costa":"10306","San Pablo":"10307"}
Aysen = { "Aysen":"11201","Chile Chico":"11401","Cisnes":"11202","Cochrane":"11301","Coyhaique":"11101","Guaitecas":"11203",
"Lago Verde":"11102","OHiggins":"11302","Rio Ibañez":"11402","Tortel":"11303"}
Magallanes_y_la_Antartica = { "Antartica":"12202","Cabo de Hornos":"12201","Laguna Blanca":"12102","Natales":"12401","Porvenir":"12301",
"Primavera":"12302","Punta Arenas":"12101","Rio Verde":"12103","San Gregorio":"12104","Timaukel":"12303","Torres del Paine":"12402"}
def Arica():
        from matplotlib import pyplot
        Arica = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10607.1,10717.3,10872.9,10985.6,11139.5,11235.2,11340.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Arica")
        pyplot.bar (Arica, height=Valores,color=colores,width=0.5)
        pyplot.show ()


print("1-Ver una región")
print("2-Ver una comuna")
print("3-Ver región con mayor y menor tasa de incidencia")
print("0-Salir")
opción = int(input("Ingrese una opción\n"))

while opción != 0:


    if opción == 1:
        print(Regiónes2,"\n")
        print("0-TERMINAR PROGRAMA")
        r = input("Ingrese una región\n")
        if r == "Tarapaca" or r == "01":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        tara()
                elif ver == "2":
                        print(Tarapaca,"\n","----------°----------")
                opción = 0
        elif r == "Antofagasta" or r == "02":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        anto()
                elif ver == "2":
                        print(Antofagasta,"\n","----------°----------")
                opción = 0
        elif r == "Atacama" or r == "03":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        atac()
                elif ver == "2":
                        print(Atacama,"\n","----------°----------")
                opción = 0
        elif r == "Coquimbo" or r == "04":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        coqu()
                elif ver == "2":
                        print(Coquimbo,"\n","----------°----------")
                opción = 0
        elif r == "Valparaiso" or r == "05":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        valpa()
                elif ver == "2":
                        print(Valparaiso,"\n","----------°----------")
                opción = 0
        elif r == "Ohiggins" or r == "06":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        ohig()
                elif ver == "2":
                        print(O_Higgins,"\n","----------°----------")
                opción = 0     
        elif r == "Maule" or r == "07":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        ma()
                elif ver == "2":
                        print(Maule,"\n","----------°----------")
                opción = 0
                
        elif r == "Biobio" or r == "08":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        bi()
                elif ver == "2":
                        print(Biobio,"\n","----------°----------")
                opción = 0
                
        elif r == "La Araucanía" or r == "09":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        laara()
                elif ver == "2":
                        print(La_Araucania,"\n","----------°----------")
                opción = 0
        elif r == "Los Lagos" or r == "10":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        los()
                elif ver == "2":
                        print(Los_Lagos,"\n","----------°----------")
                opción = 0
        elif r == "Aysen" or r == "11":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        ay()
                elif ver == "2":
                        print(Aysen,"\n","----------°----------")
                opción = 0
        elif r == "Magallanes" or r == "12":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        maga()
                elif ver == "2":
                        print(Magallanes_y_la_Antartica,"\n","----------°----------")
                opción = 0
        elif r == "Metropolitana" or r == "13":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        metro()
                elif ver == "2":
                        print(Metropolitana,"\n","----------°----------")
                opción = 0
        elif r == "Los Rios" or r == "14":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        rios()
                elif ver == "2":
                        print(Los_Rios,"\n","----------°----------")
                opción = 0
        elif r == "Arica y Parinacota" or r == "15":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        ari()
                elif ver == "2":
                        print(AricayParinacota,"\n","----------°----------")
                opción = 0
        elif r == "Ñuble" or r == "16":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        ñu()
                elif ver == "2":
                        print(Ñuble,"\n","----------°----------")
                opción = 0
        elif r == "0":
                opción = 0
        else:
                print("Error, Ingrese región valida\n")
                print(Regiónes2)              

    elif opción == 2:
        print(Comunas)
        print("0-TERMINAR PROGRAMA")
        c = input("Mostrar grafico de\n")
        if c == "Arica" or c == "15101":
                Arica()
                opción = 0 
        elif c == "Camarones" or c == "15102":
                print("grafico de Camarones")
                opción = 0 
        elif c == "General Lagos" or c == "15202":
                print("grafico de General Lagos")
                opción = 0 
        elif c == "Putre" or c == "15201":
                print("mostrar grafico de putre")
                opción = 0 
        elif c == "Alto Hospicio" or c == "01107":
                print("mostrar grafico de Alto Hospicio")
                opción = 0 
        elif c == "Camina" or c == "01402":
                print("mostrar grafico de Camina")
                opción = 0 
        elif c == "Colchane" or c == "01403":
                print("mostrar grafico de Colchane")
                opción = 0 
        elif c == "Huara" or c == "01404":
                print("grafico de huara")
                opción = 0 
        elif c == "Iquique" or c == "01101":
                print("mostrar grafico de iquique")
                opción = 0 
        elif c == "Pica" or c == "01405":
                print("mostrar grafico de pica")
                opción = 0 
        elif c == "Pozo Almonte" or c == "01401":
                print("mostrar grafico de pozo almote")
                opción = 0 
        elif c == "Antofagasta" or c == "02101":
                print("mostrar grafico")
                opción = 0 
        elif c == "Calama" or c == "02201":
                print("mostrar grafico")
                opción = 0 
        elif c == "Maria Elena" or c == "02302":
                print("mostrar grafico")
                opción = 0 
        elif c == "Mejillones" or c == "02102":
                print("mostrar grafico")
                opción = 0 
        elif c == "Ollague" or c == "02202":
                print("mostrar grafico")
                opción = 0 
        elif c == "San Pedro de Atacama" or c == "02203":
                print("mostrar grafico")
                opción = 0 
        elif c == "Sierra Gorda" or c == "02103":
                print("mostrar grafico")
                opción = 0 
        elif c == "Taltal" or  c == "02104":
                print("mostrar grafico")
                opción = 0 
        elif c == "Tocopilla" or c == "02301":
                print("mostrar grafico")
                opción = 0 
        elif c == "Alto del Carmen" or  c == "03302":
                print("mostrar grafico")
                opción = 0 
        elif c == "Caldera" or c == "03102":
                print("mostrar grafico")
                opción = 0 
        elif c == "Chanaral" or c == "03201":
                print("mostar grafico")
                opción = 0 
        elif c == "Copiapo" or c == "03101":
                print("mostrar grafico")
                opción = 0 
        elif c == "Diego de Almagro" or c == "03202":
                print("mostar grafico")
                opción = 0 
        elif c == "Freirina" or c == "03303":
                print("mostrar grafico")
                opción = 0 
        elif c == "Huasco" or c == "03304":
                print("mostrar grafico")
                opción = 0 
        elif c == "Tierra Amarilla" or c == "03103":
                print("mostrar grafico")
                opción = 0 
        elif c == "Vallenar" or  c == "03301":
                print("mostrar grafico")
                opción = 0 
        elif c == "Andacollo" or c == "04103":
                print("mostrar grafico")
                opción = 0 
        elif c == "Canela" or c == "04202":
                print("mostrar grafico")
                opción = 0 
        elif c == "Combarbala" or c == "04302":
                print("mostrar grafico")
                opción = 0 
        elif c == "Coquimbo" or c == "04102":
                print("mostrar grafico")
                opción = 0 
        elif c == "Illapel" or c == "04201":
                print("mostrar grafico")
                opción = 0 
        elif c == "La Higuera" or c == "04104":
                print("mostrar grafico")
                opción = 0 
        elif c == "La Serena" or c == "04101":
                print("mostrar grafico")
                opción = 0 
        elif c == "Los Vilos" or c == "04203":
                print("mostrar grafico")
                opción = 0 
        elif c == "Monte Patria" or c == "04303":
                print("mostrar grafico")
                opción = 0 
        elif c == "Ovalle" or c == "04301":
                print("mostrar grafico")
                opción = 0 
        elif c == "Paiguano" or c == "04105":
                print("mostrar grafico")
                opción = 0 
        elif c == "Punitaqui" or c == "04304":
                print("mostrar grafico")
                opción = 0 
        elif c == "Rio Hurtado" or c == "04305":
                print("mostrar grafico")
                opción = 0 
        elif c == "Salamanca" or c == "04204":
                print("mostrar grafico")
                opción = 0 
        elif c == "Vicuña" or c == "04106":
                print("mostrar grafico")
                opción = 0 
        elif c == "Algarrobo" or c == "05602":
                print("mostrar grafico")
                opción = 0 
        elif c == "Cabildo" or c == "05402":
                print("mostrar grafico")
                opción = 0 
        elif c == "Calera" or c == "05502":
                print("mostrar grafico")
                opción = 0 
        elif c == "Calle Larga" or c == "05302":
                print("mostrar grafico")
                opción = 0 
        elif c == "Cartagena" or c == "05603":
                print("mostrar grafico")
                opción = 0 
        elif c == "Casablanca" or  c == "05102":
                print("mostrar grafico")
                opción = 0 
        elif c == "Catemu" or c == "05702":
                print("mostrar grafico")
                opción = 0 
        elif c == "Concon" or c == "05103":
                print("mostrar grafico")
                opción = 0 
        elif c == "El Quisco" or c == "05604":
                print("mostrar grafico")
                opción = 0 
        elif c == "El Tabo" or c == "05605":
                print("mostrar grafico")
        elif c == "Hijuelas" or c == "05503":
                print("mostrar grafico")
                opción = 0 
        elif c == "Isla de Pascua" or  c == "05201":
                print("mostrar grafico")
                opción = 0 
        elif c == "Juan Fernandez" or c == "05104":
                print("mostrar grafico")
                opción = 0 
        elif c == "La Cruz" or c == "05504":
                print("mostrar grafico")
                opción = 0 
        elif c == "La Ligua" or c == "05401":
                print("mostrar grafico")
                opción = 0 
        elif c == "Limache" or c == "05802":
                print("mostrar grafico")
                opción = 0 
        elif c == "Llaillay" or c == "05703":
                print("mostrar grafico")
                opción = 0 
        elif c == "Los Andes" or c == "05301":
                print("mostrar grafico")
                opción = 0 
        elif c == "Nogales" or c == "05506":
                print("mostrar grafico")
                opción = 0 
        elif c == "Olmue" or c == "05803":
                print("mostrar grafico")
                opción = 0 
        elif c == "Panquehue" or c == "05704":
                print("mostrar grafico")
                opción = 0 
        elif c == "Papudo" or c == "05403":
                print("mostrar grafico")
                opción = 0 
        elif c == "Petorca" or c == "05404":
                print("mostrat grafico")
                opción = 0 
        elif c == "Puchuncavi" or c == "05105":
                print("mostrar grafico")
                opción = 0 
        elif c == "Putaendo" or c == "05705":
                print("mostrar grafico")
                opción = 0 
        elif c == "Quillota" or c == "05501":
                print("mostrar grafico")
                opción = 0 
        elif c == "Quilpue" or c == "05801":
                print("mostrar grafico")
                opción = 0 
        elif c == "Quintero" or c == "05107":
                print("mostrar grafico")
                opción = 0 
        elif c == "Rinconada" or c == "05303":
                print("mostrar grafico")
                opción = 0 
        elif c == "San Antonio" or c == "05601":
                print("mostrar grafico")
                opción = 0 
        elif c == "San Esteban" or c == "05304":
                print("mostrar grafico")
                opción = 0 
        elif c == "San Felipe" or c == "05701":
                print("mostrar grafico")
                opción = 0
        elif c == "Santa Maria" or c == "05706":
                print("mostrar grafico")
                opción = 0
        elif c == "Santo Domingo" or c == "05606":
                print("mostrar grafico")
                opción = 0
        elif c == "Valparaiso" or c == "05101":
                print("mostrar grafico")
                opción = 0
        elif c == "Villa Alemana" or c == "05804":
                print("mostrar grafico")
                opción = 0
        elif c == "Vina del Mar" or c == "05109":
                print("mostrar grafico")
                opción = 0
        elif c == "Zapallar" or c == "05405":
                print("mostrar grafico")
                opción = 0
        elif c == "Alhue" or c == "13502":
                print("mostrar grafico")
                opción = 0
        elif c == "Buin" or c == "13402":
                print("mostrar grafico")
                opción = 0
        elif c == "Calera de Tango" or c == "13403":
                print("mostrar grafico")
                opción = 0
        elif c == "Cerrillos" or c == "13102":
                print("mostrar grafico")
                opción = 0
        elif c == "Cerro Navia" or c == "13103":
                print("mostrar grafico")
                opción = 0
        elif c == "Colina" or c == "13301":
                print("mostrar grafico")
                opción = 0
        elif c == "Conchali" or c == "13104":
                print("mostrar grafico")
                opción = 0
        elif c == "Curacavi" or c == "13503":
                print("mostrar grafico")
                opción = 0
        elif c == "El Bosque" or c == "13105":
                print("mostrar grafico")
                opción = 0
        elif c == "El Monte" or c == "13602":
                print("mostrar grafico")
                opción = 0
        elif c == "Estacion Central" or c == "13106":
                print("mostrar grafico")
                opción = 0
        elif c == "Huechuraba" or c == "13107":
                print("mostrar grafico")
                opción = 0
        elif c == "Independencia" or c == "13108":
                print("mostrar grafico")
                opción = 0
        elif c == "Isla de Maipo" or c == "13603":
                print("mostrar grafico")
                opción = 0
        elif c == "La Cisterna" or c == "13109":
                print("mostrar grafico")
                opción = 0
        elif c == "La Florida" or c == "13110":
                print("mostrar grafico")
                opción = 0
        elif c == "La Granja" or c == "13111":
                print("mostrar grafico")
                opción = 0
        elif c == "La Pintana" or c == "13112":
                print("mostrar grafico")
                opción = 0
        elif c == "La Reina" or c == "13113":
                print("mostrar grafico")
                opción = 0
        elif c == "Lampa" or c == "13302":
                print("mostrar grafico")
                opción = 0
        elif c == "Las Condes" or c == "13114":
                print("mostrar grafico")
                opción = 0
        elif c == "Lo Barnechea" or c == "13115":
                print("mostrar grafico")
                opción = 0
        elif c == "Lo Espejo" or c == "13116":
                print("mostrar grafico")
                opción = 0
        elif c == "Lo Prado" or c == "13117":
                print("mostrar grafico")
                opción = 0
        elif c == "Macul" or c == "13118":
                print("mostrar grafico")
                opción = 0
        elif c == "Maipu" or c == "13119":
                print("mostrar grafico")
                opción = 0
        elif c == "Maria Pinto" or c == "13504":
                print("mostrar grafico")
                opción = 0
        elif c == "Melipilla" or c == "13501":
                print("mostrar grafico")
                opción = 0
        elif c == "Nunoa" or c == "13120":
                print("mostrar grafico")
                opción = 0
        elif c == "Padre Hurtado" or c == "13604":
                print("mostrar grafico")
                opción = 0
        elif c == "Paine" or c == "13404":
                print("mostrar grafico")
                opción = 0
        elif c == "Pedro Aguirre Cerda" or c == "13121":
                print("mostrar grafico")
                opción = 0
        elif c == "Penaflor" or c == "13605":
                print("mostrar grafico")
                opción = 0
        elif c == "Penalolen" or c == "13122":
                print("mostrar grafico")
                opción = 0
        elif c == "Pirque" or c == "13202":
                print("mostrar grafico")
                opción = 0
        elif c == "Providencia" or c == "13123":
                print("mostrar grafico")
                opción = 0
        elif c == "Pudahuel" or c == "13124":
                print("mostrar grafico")
                opción = 0
        elif c == "Puente Alto" or c == "13201":
                print("mostrar grafico")
                opción = 0
        elif c == "Quilicura" or c == "13125":
                print("mostrar grafico")
                opción = 0
        elif c == "Quinta Normal" or c == "13126":
                print("mostrar grafico")
                opción = 0
        elif c == "Recoleta" or c == "13127":
                print("mostrar grafico")
                opción = 0
        elif c == "Renca" or c == "13128":
                print("mostrar grafico")
                opción = 0
        elif c == "San Bernardo" or c == "13401":
                print("mostrar grafico")
                opción= 0
        elif c == "San Joaquin" or c == "13129":
                print("mostrar grafico")
                opción = 0
        elif c == "San Jose de Maipo" or c == "13203":
                print("mostrar grafico")
                opción = 0
        elif c == "San Miguel" or c == "13130":
                print("mostrar grafico")
                opción = 0
        elif c == "San Pedro" or c == "13505":
                print("mostrar grafico")
                opción = 0
        elif c == "San Ramon" or c == "13131":
                print("mostrar grafico")
                opción = 0
        elif c == "Santiago" or c == "13101":
                print("mostrar grafico")
                opción = 0
        elif c == "Talagante" or c == "13601":
                print("mostrar grafico")
                opción = 0
        elif c == "Tiltil" or c == "13303":
                print("mostrar grafico")
                opción = 0
        elif c == "Vitacura" or c == "13132":
                print("mostrar grafico")
                opción = 0
        elif c == "Chepica" or c == "06302":
                print("mostrar grafico")
                opción = 0
        elif c == "Chimbarongo" or c == "06303":
                print("mostrar grafico")
                opción = 0
        elif c == "Codegua" or c == "06102":
                print("mostrar grafico")
                opción = 0
        elif c == "Coinco" or c == "06103":
                print("mostrar grafico")
                opción = 0
        elif c == "Coltauco" or c == "06104":
                print("mostrar grafico")
                opción = 0
        elif c == "Donihue" or c == "06105":
                print("mostrar grafico")
                opción = 0
        elif c == "Graneros" or c == "06106":
                print("mostrar grafico")
                opción = 0
        elif c == "La Estrella" or c == "06202":
                print("mostrar grafico")
                opción = 0
        elif c == "Las Cabras" or c == "06107":
                print("mostrar grafico")
                opción = 0
        elif c == "Litueche" or c == "06203":
                print("mostrar grafico")
                opción = 0
        elif c == "Lolol" or c == "06304":
                print("mostrar grafico")
                opción = 0
        elif c == "Machali" or c == "06108":
                print("mostrar grafico")
                opción = 0
        elif c == "Malloa" or c == "06109":
                print("mostrar grafico")
                opción = 0
        elif c == "Marchihue" or c == "06204":
                print("mostrar grafico")
                opción = 0
        elif c == "Mostazal" or c == "06110":
                print("mostrar grafico")
                opción = 0
        elif c == "Nancagua" or c == "06305":
                print("mostrar grafico")
                opción = 0
        elif c == "Navidad" or c == "06205":
                print("mostrar grafico")
                opción = 0
        elif c == "Olivar" or c == "06111":
                print("mostrar grafico")
                opción = 0
        elif c == "Palmilla" or c == "06306":
                print("mostrar grafico")
                opción = 0
        elif c == "Paredones" or c == "06206":
                print("mostrar grafico")
                opción = 0
        elif c == "Peralillo" or c == "06307":
                print("mostrar grafico")
                opción = 0
        elif c == "Peumo" or c == "06112":
                print("mostrar grafico")
                opción = 0
        elif c == "Pichidegua" or c == "06113":
                print("mostrar grafico")
                opción = 0
        elif c == "Pichilemu" or c == "06201":
                print("mostrar grafico")
                opción = 0
        elif c == "Placilla" or c == "06308":
                print("mostrar grafico")
                opción = 0
        elif c == "Pumanque" or c == "06309":
                print("mostrar grafico")
                opción = 0
        elif c == "Quinta de Tilcoco" or c == "06114":
                print("mostrar grafico")
                opción = 0
        elif c == "Rancagua" or c == "06101":
                print("mostrar grafico")
                opción = 0
        elif c == "Rengo" or c == "06115":
                print("mostrar grafico")
                opción = 0
        elif c == "Requinoa" or c == "06116":
                print("mostrar grafico")
                opción = 0
        elif c == "San Fernando" or c == "06301":
                print("mostrar grafico")
                opción = 0
        elif c == "San Vicente" or c == "06117":
                print("mostrar grafico")
                opción = 0
        elif c == "Santa Cruz" or c == "06310":
                print("mostrar grafico")
                opción = 0
        elif c == "Cauquenes" or c == "07201":
                print("mostrar grafico")
                opción = 0
        elif c == "Chanco" or c == "07202":
                print("mostrar grafico")
                opción = 0
        elif c == "Colbun" or c == "07402":
                print("mostrar grafico")
                opción = 0
        elif c == "Constitucion" or c == "07102":
                print("mostrar grafico")
                opción = 0
        elif c == "Curepto" or c == "07103":
                print("mostrar grafico")
                opción = 0
        elif c == "Curico" or c == "07301":
                print("mostrar grafico")
                opción = 0
        elif c == "Empedrado" or c == "07104":
                print("mostrar grafico")
                opción = 0
        elif c == "Hualane" or c == "07302":
                print("mostrar grafico")
                opción = 0
        elif c == "Licanten" or c == "07303":
                print("mostrar grafico")
                opción = 0
        elif c == "Linares" or c == "07401":
                print("mostrar grafico")
                opción = 0
        elif c == "Longavi" or c == "07403":
                print("mostrar grafico")
                opción = 0
        elif c == "Maule" or c == "07105":
                print("mostrar grafico")
                opción = 0
        elif c == "Molina" or c == "07304":
                print("mostrar grafico")
                opción = 0
        elif c == "Parral" or c == "07404":
                print("mostrar grafico")
                opción = 0
        elif c == "Pelarco" or c == "07106":
                print("mostrar grafico")
                opción = 0
        elif c == "Pelluhue" or c == "07203":
                print("mostrar grafico")
                opción = 0
        elif c == "Pencahue" or c == "07107":
                print("mostrar grafico")
                opción = 0
        elif c == "Rauco" or c == "07305":
                print("mostrar grafico")
                opción = 0
        elif c == "Retiro" or c == "07405":
                print("mostrar grafico")
                opción = 0
        elif c == "Rio Claro" or c == "07108":
                print("mostrar grafico")
                opción = 0
        elif c == "Romeral" or c == "07306":
                print("mostrar grafico")
                opción = 0
        elif c == "Sagrada Familia" or c == "07307":
                print("mostrar grafico")
                opción = 0
        elif c == "San Clemente" or c == "07109":
                print("mostrar grafico")
                opción = 0
        elif c == "San Javier" or c == "07406":
                print("mostrar grafico")
                opción = 0
        elif c == "San Rafael" or c == "07110":
                print("mostrar grafico")
                opción = 0
        elif c == "Talca" or c == "07101":
                print("mostrar grafico")
                opción = 0
        elif c == "Teno" or c == "07308":
                print("mostrar grafico")
                opción = 0
        elif c == "Vichuquen" or c == "07309":
                print("mostrar grafico")
                opción = 0
        elif c == "Villa Alegre" or c == "07407":
                print("mostrar grafico")
                opción = 0
        elif c == "Yerbas Buenas" or c == "07408":
                print("mostrar grafico")
                opción = 0
        elif c == "Bulnes" or c == "16102":
                print("mostrar grafico")
                opción = 0
        elif c == "Chillan" or c == "16101":
                print("mostrar grafico")
                opción = 0
        elif c == "Chillan Viejo" or c == "16103":
                print("mostrar grafico")
                opción = 0
        elif c == "Cobquecura" or c == "16202":
                print("mostrar grafico")
                opción = 0
        elif c == "Coelemu" or c == "16203":
                print("mostrar grafico")
                opción = 0
        elif c == "Coihueco" or c == "16302":
                print("mostrar grafico")
                opción = 0
        elif c == "El Carmen" or c == "16104":
                print("mostrar grafico")
                opción = 0
        elif c == "Ninhue" or c == "16204":
                print("mostrar grafico")
                opción = 0
        elif c == "Niquen" or c == "16303":
                print("mostrar grafico")
                opción = 0
        elif c == "Pemuco" or c == "16105":
                print("mostrar grafico")
                opción = 0
        elif c == "Pinto" or c == "16106":
                print("mostrar grafico")
                opción = 0
        elif c == "Portezuelo" or c == "16205":
                print("mostrar grafico")
                opción = 0
        elif c == "Quillon" or c == "16107":
                print("mostrar grafico")
                opción = 0
        elif c == "Quirihue" or c == "16201":
                print("mostrar grafico")
                opción = 0
        elif c == "Ranquil" or c == "16206":
                print("mostrar grafico")
                opción = 0
        elif c == "San Carlos" or c == "16301":
                print("mostrar grafico")
                opción = 0
        elif c == "San Fabian" or c == "16304":
                print("mostrar grafico")
                opción = 0
        elif c == "San Ignacio" or c == "16108":
                print("mostrar grafico")
                opción = 0
        elif c == "San Nicolas" or c == "16305":
                print("mostrar grafico")
                opción = 0
        elif c == "Treguaco" or c == "16207":
                print("mostrar grafico")
                opción = 0
        elif c == "Yungay" or c == "16109":
                print("mostrar grafico")
                opción = 0
        elif c == "Alto Biobio" or c == "08314":
                print("mostrar grafico")
                opción = 0
        elif c == "Antuco" or c == "08302":
                print("mostrar grafico")
                opción = 0
        elif c == "Arauco" or c == "08202":
                print("mostrar grafico")
                opción = 0
        elif c == "Cabrero" or c == "08303":
                print("mostrar grafico")
                opción = 0
        elif c == "Canete" or c == "08203":
                print("mostrar grafico")
                opción = 0
        elif c == "Chiguayante" or c == "08103":
                print("mostrar grafico")
                opción = 0
        elif c == "Concepcion" or c == "08101":
                print("mostrar grafico")
                opción = 0
        elif c == "Contulmo" or c == "08204":
                print("mostrar grafico")
                opción = 0
        elif c == "Coronel" or c == "08102":
                print("mostrar grafico")
                opción = 0
        elif c == "Curanilahue" or c == "08205":
                print("mostrar grafico")
                opción = 0
        elif c == "Florida" or c == "08104":
                print("mostrar grafico")
                opción = 0
        elif c == "Hualpen" or c == "08112":
                print("mostrar grafico")
                opción = 0
        elif c == "Hualqui" or c == "08105":
                print("mostrar grafico")
                opción = 0
        elif c == "Laja" or c == "08304":
                print("mostrar grafico")
                opción = 0
        elif c == "Lebu" or c == "08201":
                print("mostrar grafico")
                opción = 0
        elif c == "Los Alamos" or c == "08206":
                print("mostrar grafico")
                opción = 0
        elif c == "Los Angeles" or c == "08301":
                print("mostrar grafico")
                opción = 0
        elif c == "Lota" or c == "08106":
                print("mostrar grafico")
                opción = 0
        elif c == "Mulchen" or c == "08305":
                print("mostrar grafico")
                opción = 0
        elif c == "Nacimiento" or c == "08306":
                print("mostrar grafico")
                opción = 0
        elif c == "Negrete" or c == "08307":
                print("mostrar grafico")
                opción = 0
        elif c == "Penco" or c == "08107":
                print("mostrar grafico")
                opción = 0
        elif c == "Quilaco" or c == "08308":
                print("mostrar grafico")
                opción = 0
        elif c == "Quilleco" or c == "08309":
                print("mostrar grafico")
                opción = 0
        elif c == "San Pedro de la Paz" or c == "08108":
                print("mostrar grafico")
                opción = 0
        elif c == "San Rosendo" or c == "08310":
                print("mostrar grafico")
                opción = 0
        elif c == "Santa Barbara" or c == "08311":
                print("mostrar grafico")
                opción = 0
        elif c == "Santa Juana" or c == "08109":
                print("mostrar grafico")
                opción = 0
        elif c == "Talcahuano" or c == "08110":
                print("mostrar grafico")
                opción = 0
        elif c == "Tirua" or c == "08207":
                print("mostrar grafico")
                opción = 0
        elif c == "Tome" or c == "08111":
                print("mostrar grafico")
                opción = 0
        elif c == "Tucapel" or c == "Tucapel":
                print("mostrar grafico")
                opción = 0
        elif c == "Yumbel" or c == "08313":
                print("mostrar grafico")
                opción = 0
        elif c == "Angol" or c == "09201":
                print("mostrar grafico")
                opción = 0
        elif c == "Carahue" or c == "09102":
                print("mostrar grafico")
                opción = 0
        elif c == "Cholchol" or c == "09121":
                print("mostrar grafico")
                opción = 0
        elif c == "Collipulli" or c == "09202":
                print("mostrar grafico")
                opción = 0
        elif c == "Cunco" or c == "09103":
                print("mostrar grafico")
                opción = 0
        elif c == "Curacautin" or c == "09203":
                print("mostrar grafico")
                opción = 0
        elif c == "Curarrehue" or c == "09104":
                print("mostrar grafico")
                opción = 0
        elif c == "Ercilla" or c == "09204":
                print("mostrar grafico")
                opción = 0
        elif c == "Freire" or c == "09105":
                print("mostrar grafico")
                opción = 0
        elif c == "Galvarino" or c == "09106":
                print("mostrar grafico")
                opción = 0
        elif c == "Gorbea" or c == "09107":
                print("mostrar grafico")
                opción = 0
        elif c == "Lautaro" or c == "09108":
                print("mostrar grafico")
                opción = 0
        elif c == "Loncoche" or c == "09109":
                print("mostrar grafico")
                opción = 0
        elif c == "Lonquimay" or c == "09205":
                print("mostrar grafico")
                opción = 0
        elif c == "Los Sauces" or c == "09206":
                print("mostrar grafico")
                opción = 0
        elif c == "Lumaco" or c == "09207":
                print("mostrar grafico")
                opción = 0
        elif c == "Melipeuco" or c == "09110":
                print("mostrar grafico")
                opción = 0
        elif c == "Nueva Imperial" or c == "09111":
                print("mostrar grafico")
                opción = 0
        elif c == "Padre Las Casas" or c == "09112":
                print("mostrar grafico")
                opción = 0
        elif c == "Perquenco" or c == "09113":
                print("mostrar grafico")
                opción = 0
        elif c == "Pitrufquen" or c == "09114":
                print("mostrar grafico")
                opción = 0
        elif c == "Pucon" or c == "09115":
                print("mostrar grafico")
                opción = 0
        elif c == "Puren" or c == "09208":
                print("mostrar grafico")
                opción = 0
        elif c == "Renaico" or c == "09209":
                print("mostrar grafico")
                opción = 0
        elif c == "Saavedra" or c == "09116":
                print("mostrar grafico")
                opción = 0
        elif c == "Temuco" or c == "09101":
                print("mostrar grafico")
                opción = 0
        elif c == "Teodoro Schmidt" or c == "09117":
                print("mostrar grafico")
                opción = 0
        elif c == "Tolten" or c == "09118":
                print("mostrar grafico")
                opción = 0
        elif c == "Traiguen" or c == "09210":
                print("mostrar grafico")
                opción = 0
        elif c == "Victoria" or c == "09211":
                print("mostrar grafico")
                opción = 0
        elif c == "Vilcun" or c == "09119":
                print("mostrar grafico")
                opción = 0
        elif c == "Villarrica" or c == "09120":
                print("mostrar grafico")
                opción = 0
        elif c == "Corral" or c == "Corral":
                print("mostrar grafico")
                opción = 0
        elif c == "Futrono" or c == "14202":
                print("mostrar grafico")
                opción = 0
        elif c == "La Union" or c == "14201":
                print("mostrar grafico")
                opción = 0
        elif c == "Lago Ranco" or c == "14203":
                print("mostrar grafico")
                opción = 0
        elif c == "Lanco" or c == "14103":
                print("mostrar grafico")
                opción = 0
        elif c == "Los Lagos" or c == "14104":
                print("mostrar grafico")
                opción = 0
        elif c == "Mafil" or c == "14105":
                print("mostrar grafico")
                opción = 0
        elif c == "Mariquina" or c == "14106":
                print("mostrar grafico")
                opción = 0
        elif c == "Paillaco" or c == "14107":
                print("mostrar grafico")
                opción = 0
        elif c == "Panguipulli" or c == "14108":
                print("mostrar grafico")
                opción = 0
        elif c == "Rio Bueno" or c == "14204":
                print("mostrar grafico")
                opción = 0
        elif c == "Valdivia" or c == "14101":
                print("mostrar grafico")
                opción = 0
        elif c == "Ancud" or c == "10202":
                print("mostrar grafico")
                opción = 0
        elif c == "Calbuco" or c == "10102":
                print("mostrar grafico")
                opción = 0
        elif c == "Castro" or c == "10201":
                print("mostrar grafico")
                opción = 0
        elif c == "Chaiten" or c == "10401":
                print("mostrar grafico")
                opción = 0
        elif c == "Chonchi" or c == "10203":
                print("mostrar grafico")
                opción = 0
        elif c == "Cochamo" or c == "10103":
                print("mostrar grafico")
                opción = 0
        elif c == "Curaco de Velez" or c == "10204":
                print("mostrar grafico")
                opción = 0
        elif c == "Dalcahue" or c == "10205":
                print("mostrar grafico")
                opción = 0
        elif c == "Fresia" or c == "10104":
                print("mostrar grafico")
                opción = 0
        elif c == "Frutillar" or c == "Frutillar":
                print("mostrar grafico")
                opción = 0
        elif c == "Futaleufu" or c == "10402":
                print("mostrar grafico")
                opción = 0
        elif c == "Hualaihue" or c == "10403":
                print("mostrar grafico")
                opción = 0
        elif c == "Llanquihue" or c == "10107":
                print("mostrar grafico")
                opción = 0
        elif c == "Los Muermos" or c == "10106":
                print("mostrar grafico")
                opción = 0
        elif c == "Maullin" or c == "Maullin":
                print("mostrar grafico")
                opción = 0
        elif c == "Osorno" or c == "10301":
                print("mostrar grafico")
                opción = 0
        elif c == "Palena" or c == "10404":
                print("mostrar grafico")
                opción = 0
        elif c == "Puerto Montt" or c == "10101":
                print("mostrar grafico")
                opción = 0
        elif c == "Puerto Octay" or c == "10302":
                print("mostrar grafico")
                opción = 0
        elif c == "Puerto Varas" or c == "10109":
                print("mostrar grafico")
                opción = 0
        elif c == "Puqueldon" or c == "10206":
                print("mostrar grafico")
                opción = 0
        elif c == "Purranque" or c == "10303":
                print("mostrar grafico")
                opción = 0
        elif c == "Puyehue" or c == "10304":
                print("mostrar grafico")
                opción = 0
        elif c == "Queilen" or c == "10207":
                print("mostrar grafico")
                opción = 0
        elif c == "Quellon" or c == "10208":
                print("mostrar grafico")
                opción = 0
        elif c == "Quemchi" or c == "10209":
                print("mostrar grafico")
                opción = 0
        elif c == "Quinchao" or c == "10210":
                print("mostrar grafico")
                opción = 0
        elif c == "Rio Negro" or c == "10305":
                print("mostrar grafico")
                opción = 0
        elif c == "San Juan de la Costa" or c == "10306":
                print("mostrar grafico")
                opción = 0
        elif c == "San Pablo" or c == "10307":
                print("mostrar grafico")
                opción = 0
        elif c == "Aysen" or c == "11201":
                print("mostrar grafico")
                opción = 0
        elif c == "Chile Chico" or c == "11401":
                print("mostrar grafico")
                opción = 0
        elif c == "Cisnes" or c == "11202":
                print("mostrar grafico")
                opción = 0
        elif c == "Cochrane" or c == "11301":
                print("mostrar grafico")
                opción = 0
        elif c == "Coyhaique" or c == "11101":
                print("mostrar grafico")
                opción = 0
        elif c == "Guaitecas" or c == "11203":
                print("mostrar grafico")
                opción = 0
        elif c == "Lago Verde" or c == "11102":
                print("mostrar grafico")
                opción = 0
        elif c == "OHiggins" or c == "11302":
                print("mostrar grafico")
                opción = 0
        elif c == "Rio Ibañez" or c == "11402":
                print("mostrar grafico")
                opción = 0
        elif c == "Tortel" or c == "11303":
                print("mostrar grafico")
                opción = 0
        elif c == "Antartica" or c == "12202":
                print("mostrar grafico")
                opción = 0
        elif c == "Cabo de Hornos" or c == "12201":
                print("mostrar grafico")
                opción = 0
        elif c == "Laguna Blanca" or c == "12102":
                print("mostrar grafico")
                opción = 0
        elif c == "Natales" or c == "12401":
                print("mostrar grafico")
                opción = 0
        elif c == "Porvenir" or c == "12301":
                print("mostrar grafico")
                opción = 0
        elif c == "Primavera" or c == "12302":
                print("mostrar grafico")
                opción = 0
        elif c == "Punta Arenas" or c == "12101":
                print("mostrar grafico")
                opción = 0
        elif c == "Rio Verde" or c == "12103":
                print("mostrar grafico")
                opción = 0
        elif c == "San Gregorio" or c == "12104":
                print("mostrar grafico")
                opción = 0
        elif c == "Timaukel" or c == "12303":
                print("mostrar grafico")
                opción = 0
        elif c == "Torres del Paine" or c == "12402":
                print("mostrar grafico")
                opción = 0
        elif c == "0":
                opción = 0
        else :
                print("Ingrese una comuna valida")

 
    elif opción == 3:
        print("se mostrara un grafico")
        opción = 0
    
    else:
        opción = int(input("Error, Ingrese una opción valida\n"))

    
