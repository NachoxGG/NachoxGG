# ESTA ES UNA LISTA DE LA REGIONES CON SU CODIGO 
Regiónes2 = {"01":"Tarapaca","02":"Antofagasta","03":"Atacama","04":"Coquimbo","05":"Valparaiso","06":"OHiggins","07":"Maule","08":"Biobio","09":"La Araucanía",
"10":"Los Lagos","11":"Aysen","12":"Magallanes","13":"Metropolitana","14":"Los Rios","15":"Arica y Parinacota","16":"Ñuble"}
 
# ESTOS SON LOS GRAFICOS DE LAS REGIONES   (1-130)
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

# ESTAS SON LAS COMUNAS DE CADA REGION Y SU CODIGO 
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

# ESTA LISTAS SON DE LAS REGIONES CON SU COMUNA  
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
# ESTOS SON LOS GRAFICOS DE LAS COMUNAS (247-3023)
def arica():                                               
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10607.1,10717.3,10872.9,10985.6,11139.5,11235.2,11340.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Arica")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def camarones():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [4947.3,4947.3,5028.4,5028.4,5028.4,5109.5,5190.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Camarones")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def generallagos():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9753.1,9753.1,9753.1,9876.5,9876.5,10000.0,10617.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en General Lagos")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def putre():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6998.0,7117.3,7395.6,7514.9,7514.9,7594.4,7634.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Putre")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()       
def altohospicio():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10907.8,10972.4,11093.9,11160.1,11240.9,11304.7,11377.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Alto Hospicio")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def camina():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [14109.1,14400.0,14690.9,14909.1,14836.4,1981.8,14981.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Camina")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def colchane():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8907.1,8907.1,8907.1,8907.1,9096.7,9096.7,9096.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Colchane")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def huara():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [13866.7,14000.0,14200.0,14266.7,14300.0,14366.7,14366.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Huara")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def iquique():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12092.4,12168.0,12272.7,12344.3,12424.4,12483.5,12537.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Iquique")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pica():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [15710.0,15861.0,16079.2,16129.6,16230.3,16364.6,16431.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pica")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pozoalmonte():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12273.,612348.4,12503.6,12572.6,12641.6,12676.1,12727.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pozo Almonte")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def antofagasta():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8558.8,8623.4,8707.5,8771.6,8825.9,8895.6,8949.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Antofagasta")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def calama():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8625.8,8702.0,8810.7,8890.6,8984.1,9049.8,9134.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Calama")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def mariaelena():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9260.3,9304.4,9627.2,9656.6,9685.9,9818.0,9862.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Maria Elena")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def mejillones():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12405.3,12493.2,12608.3,12669.2,12682.7,12709.8,12723.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Mejillones")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def ollague():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11149.8,11149.8,11149.8,11149.8,11149.8,11149.8,11846.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Ollague")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanpedrodeatacama():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8405.2,8462.7,8635.2,8779.0,8961.1,9076.1,9239.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Pedro de Atacama")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sierragorda():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8934.7,8992.0,9163.8,9163.8,9221.1,9278.4,9392.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Sierra Gorda")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def taltal():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5967.6,6033.5,6062.8,6092.1,6150.7,6267.8,6363.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Taltal")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def tocopilla():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6496.0,6570.7,6652.7,6731.0,6780.9,6809.4,6841.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Tocopilla")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def altodelcarmen():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [3840.1,4119.4,4206.7,4293.9,4311.4,4346.3,4451.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Alto del Carmen")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def caldera():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6867.1,6939.2,7129.6,7248.0,7371.6,7433.3,7546.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Caldera")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def chanaral():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6100.0,6206.3,6343.1,6411.4,6586.1,6707.7,6966.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Chanaral")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def copiapo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7787.3,7937.5,8119.2,8228.1,8378.3,8462.1,8626.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Copiapo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def diegodealmagro():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7626.4,7758.7,7912.0,8051.3,8239.3,8385.6,8587.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Diego de Almagro")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def freirina():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7707.3,7876.6,8058.8,8163.0,8267.2,8280.2,8358.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Freirina")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def huasco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6329.9,6525.2,6702.8,6818.2,6933.6,7004.6,7093.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Huasco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def tierraamarilla():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8503.4,8706.0,8873.7,8943.5,8985.5,9041.4,9104.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Tierra Amarilla")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def vallenar():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7642.7,7777.7,7963.7,8091.7,8179.4,8251.3,8342.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Vallenar")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def andacollo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [4087.9,4113.3,4240.5,4376.2,4478.0,4537.4,4588.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Andacollo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def canela():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [4347.4,4378.8,4441.7,4462.6,4494.0,4567.4,4588.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Canela")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def combarbala():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [4256.7,4371.9,4494.4,4624.0,4724.9,4847.3,4919.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Combarbala")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def coquimbo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5611.2,5707.4,5833.3,5929.1,6009.3,6076.7,6139.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Coquimbo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def illapel():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5643.1,5804.7,6009.0,6176.6,6399.2,6551.6,6725.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Illapel")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lahiguera():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7280.9,7415.7,7618.0,7662.9,7752.8,7887.6,8112.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en La Higuera")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def laserena():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5720.3,5822.4,5957.4,6057.5,6149.7,6220.2,6293.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en La Serena")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def losvilos():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7037.7,7123.3,7183.2,7285.9,7354.3,7422.8,7469.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Los Vilos")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def montepatria():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5008.1,5131.1,5263.3,5370.9,5441.6,5543.1,5632.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Monte Patria")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def ovalle():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6642.3,6780.8,6991.1,7139.5,7275.6,7373.7,7437.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Ovalle")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def paiguano():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5112.3,5625.7,6181.8,6566.8,6823.5,6823.5,6909.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Paiguano")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def punitaqui():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6716.0,6847.5,7085.9,7266.7,7340.7,7455.8,7496.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Punitaqui")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def riohurtado():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [4597.4,4620.3,4711.8,4780.4,4826.2,4940.5,5054.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Rio Hurtado")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def salamanca():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5235.3,5372.7,5499.8,5599.5,5685.3,5743.7,5819.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Salamanca")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def vicuña():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [4949.4,5164.6,5460.5,5662.2,5823.6,5978.3,6153.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Vicuña")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def algarrobo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6445.2,6517.7,6642.9,6728.6,6853.8,6932.9,7012.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Algarrobo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def cabildo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6194.6,6339.8,6489.9,6615.7,6727.0,6823.8,6954.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cabildo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def calera():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8230.9,8354.0,8557.4,8689.9,8846.6,8986.6,9081.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Calera")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def callelarga():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6807.4,7038.0,7226.1,7377.7,7480.9,7541.6,7596.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Calle Larga")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def cartagena():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7142.0,7315.5,7698.1,7974.1,8206.8,8309.3,8400.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cartagena")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def casablanca():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7123.8,7240.3,7408.3,7494.0,7555.7,7610.6,7682.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Casablanca")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def catemu():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6244.7,6507.6,6764.0,6856.0,7020.3,7184.6,7427.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Catemu")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def concon():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6661.7,6792.5,6897.1,6990.8,7062.7,7108.5,7171.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Concon")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def elquisco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6211.3,6572.0,6865.1,7079.2,7254.0,7327.2,7428.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en El Quisco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def eltabo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7351.1,7609.2,7881.2,8257.8,8501.9,8885.5,9115.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en El Tabo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def hijuelas():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6518.7,6612.9,6691.4,6796.2,6853.8,6879.9,6995.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Hijuelas")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def isladepascua():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [120.8,120.8,120.8,120.8,108.7,108.7,120.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Isla de Pascua")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def juanfernandez():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [96.8,96.8,96.8,96.8,96.8,96.8,96.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Juan Fernandez")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lacruz():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6382.1,6508.4,6678.3,6769.1,6844.1,6966.5,7029.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en La Cruz")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def laligua():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7019.3,7165.0,7379.6,7530.7,7660.5,7766.5,7909.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en La Ligua")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def limache():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7260.0,7372.2,7534.4,7636.5,7742.7,7820.8,7916.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Limache")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def llaillay():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6165.9,6369.4,6652.1,6927.2,7191.0,7432.3,7643.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Llaillay")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def losandes():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7165.2,7404.6,7630.7,7805.5,7931.8,8018.4,8105.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Los Andes")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def nogales():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6849.7,7003.0,7126.4,7275.4,7398.9,7586.2,7637.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Nogales")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def olmue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6254.5,6342.8,6540.0,6649.0,6768.4,6830.7,6882.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Olmue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def panquehue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6052.7,6170.6,6314.7,6498.1,6707.7,6812.5,6838.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Panquehue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def papudo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7256.9,7273.0,7305.3,7385.9,7579.4,7708.4,7772.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Papudo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def petorca():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5086.2,5228.3,5323.0,5502.9,5626.1,5768.1,5948.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Petorca")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def puchuncavi():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6053.5,6173.1,6327.5,6526.8,6681.3,6805.8,6845.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Puchuncavi")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def putaendo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5446.3,5593.7,5797.7,5899.7,5984.7,6126.4,6205.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Putaendo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quillota():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7487.8,7580.0,7710.2,7802.4,7926.5,7995.1,8083.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quillota")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quilpue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6871.4,6975.5,7107.8,7210.7,7314.8,7407.0,7467.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quilpue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quintero():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6829.9,6943.4,7009.8,7103.9,7173.1,7242.3,7305.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quintero")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def rinconada():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5442.6,5691.2,5975.3,6161.8,6312.7,6419.2,6525.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Rinconada")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanantonio():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7344.9,7472.0,7683.9,7817.2,7986.7,8147.9,8268.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Antonio")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanesteban():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5566.1,5701.7,5880.9,5968.1,6195.8,6292.7,6399.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Esteban")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanfelipe():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6631.6,6841.2,7097.5,7224.5,7396.9,7484.4,7585.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Felipe")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def santamaria():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6733.1,6916.4,7142.4,7282.9,7496.8,7594.6,7765.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Santa Maria")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def santodomingo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5991.3,6150.5,6251.0,6326.5,6401.9,6510.8,6603.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Santo Domingo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def valparaiso():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9462.1,9583.4,9712.0,9812.4,9916.6,9993.0,10084.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Valparaiso")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def villaalemana():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7233.5,7337.6,7474.7,7580.9,7692.2,7786.9,7886.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Villa Alemana")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def viñadelmar():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7882.5,7974.4,8081.4,8156.7,8250.2,8324.4,8398.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Viña del Mar")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def zapallar():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6204.7,6329.7,6467.4,6579.9,6717.5,6767.6,6855.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en zapallar")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def alhue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9588.1,9736.7,9871.7,9939.2,10033.8,10087.8,10141.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Alhue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def buin():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8500.5,8748.6,8892.7,9061.4,9153.5,9252.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Buin")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def caleradetango():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7228.7,7330.4,7460.1,7551.3,7649.4,7793.2,7908.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Calera de Tango")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def Cerrillos():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8394.0,8536.8,8686.3,8801.0,8906.7,9000.0,9075.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cerrillos")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def cerronavia():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11411.9,11567.1,11776.9,11907.5,12043.7,12130.7,12211.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cerro Navia")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def colina():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7250.8,7428.8,7610.6,7739.3,7872.3,7966.0,8045.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Colina")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def conchali():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9523.3,9651.9,9812.9,9901.9,9996.0,10046.3,10113.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Conchali")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def curacavi():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8855.3,9022.8,9305.5,9440.0,9574.5,9651.4,9769.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Curacavi")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def elbosque():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11068.0,11225.6,11425.0,11558.1,11697.7,11794.2,11897.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en El Bosque")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def elmonte():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8964.4,9099.3,9234.3,9344.2,9446.7,9504.2,9566.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en El Monte")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def estacioncentral():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7909.9,8052.1,8188.9,8288.0,8396.4,8460.2,8518.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Estacion Central")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def huechuraba():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7869.2,8010.5,8158.9,8275.3,8382.8,8445.9,8523.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Huechuraba")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def independencia():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9425.3,9526.6,9646.3,9734.3,9814.5,9872.9,9922.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Independencia")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def islademaipo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9148.4,9282.8,9417.2,9479.5,9586.5,9651.2,9706.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Isla de Maipo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lacisterna():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9094.5,9238.9,9424.1,9547.6,9629.2,9720.8,9790.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en La Cisterna")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def laflorida():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [	9457.0,9617.0,9787.7,9908.0,10032.5,10124.7,10208.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en La Florida")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lagranja():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12577.8,12756.5,12976.8,13122.9,13255.9,13353.0,13447.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en La Granja")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lapintana():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12560.3,12722.4,12926.8,13061.5,13198.8,13288.1,13368.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en La Pintana")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lareina():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6216.3,6343.0,6479.7,6561.5,6657.2,6732.0,6817.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en La Reina")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lampa():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7386.2,7510.8,7703.8,7807.1,7907.1,7978.8,8023.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lampa")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lascondes():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5128.5,5208.0,5308.1,5367.0,5432.1,5473.8,5523.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Las Condes")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lobarnechea():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6862.7,6961.9,7120.6,7199.6,7289.1,7351.1,7412.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lo Barnechea")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def loespejo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6862.7,6961.9,7120.6,7199.6,7289.1,7351.1,7412.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lo Espejo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def loprado():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11981.5,12183.6,12391.4,12589.7,12725.7,12819.6,12935.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lo Prado")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def macul():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9171.5,9307.4,9481.2,9590.4,9713.7,9781.3,9845.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Macul")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def maipu():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7188.8,7319.0,7467.8,7564.4,7670.9,7738.4,7810.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Maipu")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def mariapinto():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9111.6,9205.4,9466.7,9553.8,9674.4,9774.9,9962.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Maria Pinto")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def melipilla():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7801.6,7953.4,8099.6,8179.4,8271.9,8341.1,8418.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Melipilla")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def nuñoa():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6059.7,6154.9,6270.4,6341.5,6409.1,6457.0,6512.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Nuñoa")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def padrehurtado():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9320.9,9535.2,9784.6,9949.0,10100.0,10237.5,10298.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Padre Hurtado")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def paine():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7884.9,8037.1,8206.3,8319.8,8449.1,8544.6,8629.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Paine")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pedroaguirrecerda():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10573.9,10772.4,11034.9,11164.8,11325.3,11428.3,11549.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pedro Aguirre Cerda")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def penaflor():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7881.6,8043.9,8247.7,8364.5,8478.3,8592.1,8683.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Penaflor")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def penalolen():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10677.4,10838.5,11013.6,11161.6,11308.6,11419.5,11533.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Penalolen")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pirque():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9736.1,9916.9,10120.6,10258.6,10380.2,10508.3,10583.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pirque")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def providencia():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5532.2,5631.1,5744.6,5816.2,5866.3,5922.7,5955.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Providencia")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pudahuel():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10106.3,10267.1,10414.8,10532.9,10643.2,10732.8,10803.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pudahuel")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def puentealto():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10166.0,10309.7,10491.3,10624.3,10753.7,10855.2,10935.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Puente Alto")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quilicura():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7891.4,8022.2,8140.7,8227.5,8302.5,8368.5,8421.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quilicura")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quintanormal():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10595.6,10771.6,10969.6,11128.7,11233.6,11329.6,11401.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quinta Normal")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def recoleta():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9128.0,9237.4,9358.9,9446.8,9535.2,9593.6,9663.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Recoleta")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def renca():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [13568.8,13775.8,14062.4,14244.0,14430.5,14538.0,14651.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Renca")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanbernardo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9462.8,9645.0,9822.7,9946.4,10068.8,10162.3,10242.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Bernardo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanjoaquin():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11621.0,11814.3,12039.4,12181.5,12317.7,12436.6,12505.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Joaquin")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanjosedemaipo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8801.8,9064.6,9257.7,9375.7,9488.3,9590.2,9649.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Jose de Maipo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanmiguel():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10509.6,10678.0,10844.1,10966.6,11077.8,11169.5,11248.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Miguel")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanpedro():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7596.4,7646.6,7730.3,7772.1,7847.4,7872.5,7964.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Pedro")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanramon():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11700.4,11827.5,11992.8,12076.1,12169.7,12233.3,12301.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Ramon")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def santiago():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7829.1,7969.2,8110.0,8196.0,8276.5,8330.4,8379.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Santiago")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def talagante():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [881.1,5988.7,6066.9,6146.3,6206.2,6258.7,6308.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Talagante")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def tiltil():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7342.7,7505.7,7673.3,7766.4,7896.8,7934.1,7985.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Tiltil")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def vitacura():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [4835.0,4903.2,4972.4,5021.0,5070.6,5110.9,5160.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Vitacura")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def chepica():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6518.1,6612.2,6819.5,6995.3,7139.7,7221.4,7259.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Chepica")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def chimbarongo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5406.4,5517.8,5621.3,5711.5,5838.8,5897.2,5947.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Chimbarongo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def codegua():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7172.2,7271.6,7427.6,7541.1,7590.8,7619.2,7668.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Codegua")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def Coinco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6550.9,6716.9,6755.2,6895.7,6959.5,6959.5,6972.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Coinco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def coltauco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6579.5,6706.5,6762.9,6791.1,6833.5,6885.2,6913.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Coltauco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def donihue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7396.5,7524.2,7630.0,7731.3,7845.8,7894.3,7907.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Donihue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def graneros():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7903.2,8059.4,8303.2,8448.4,8527.8,8607.3,8694.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Graneros")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def laestrella():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5330.8,5330.8,5427.1,5523.4,5587.7,5748.2,5973.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en La Estrella")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lascabras():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8594.7,8673.2,8789.1,8863.9,8976.0,9091.9,9177.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Las Cabras")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def litueche():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7420.5,7583.1,7790.1,7923.1,7997.0,8233.6,8277.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Litueche")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lolol():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [3649.3,3759.1,3841.4,3923.7,3978.6,4033.5,4074.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lolol")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def machali():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5878.5,5973.7,6117.2,6214.0,6275.8,6340.9,6404.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Machali")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def malloa():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7434.9,7526.7,7639.6,7696.1,7802.0,7851.4,7893.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Malloa")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def marchihue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6210.7,6328.6,6433.4,6499.0,6538.3,6564.5,6577.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Marchihue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def mostazal():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6459.8,6649.2,6911.4,7031.5,7206.3,7293.7,7421.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Mostazal")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def nancagua():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7089.5,7199.2,7246.2,7314.1,7345.5,7408.2,7512.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Nancagua")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def navidad():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5721.3,6097.9,6300.7,6546.9,6662.8,6720.7,6764.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Navidad")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def olivar():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9217.7,9306.6,9443.4,9525.4,9573.3,9621.2,9621.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Olivar")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def palmilla():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6414.0,6429.1,6519.3,6632.1,6662.2,6692.2,6707.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Palmilla")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def paredones():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6835.7,6898.7,7056.2,7119.2,7213.7,7229.5,7245.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Paredones")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def peralillo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7537.5,7677.9,7791.6,7878.5,8005.6,8052.4,8126.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Peralillo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def peumo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7983.4,8152.1,8373.9,8484.8,8552.3,8624.6,8658.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Peumo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pichidegua():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [    5815.9,5899.8,5989.3,6089.9,6173.8,6369.5,6414.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pichidegua")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pichilemu():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7627.7,7725.9,7933.2,7998.7,8151.5,8249.7,8282.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pichilemu")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def placilla():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6173.9,6343.8,6485.4,6683.7,6796.9,6796.9,6796.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Isla de Placilla")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pumanque():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores =[5649.6,5728.9,5822.6,5930.7,6024.4,6118.0,6197.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pumanque")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quintadetilcoco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8483.1,8618.4,8780.6,8886.5,8980.4,9044.9,9109.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quinta de Tilcoco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def rancagua():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8483.1,8618.4,8780.6,8886.5,8980.4,9044.9,9109.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Rancagua")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def rengo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8223.2,8377.0,8507.3,8609.3,8681.5,8733.3,8802.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Rengo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def requinoa():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7260.2,7401.8,7503.9,7592.8,7638.9,7717.9,7780.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Requinoa")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanfernando():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8238.6,8302.2,8423.0,8512.0,8579.4,8635.3,8677.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Fernando")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanvicente():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7649.6,7783.9,7904.5,7981.5,8070.4,8145.5,8188.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Vicente")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def santacruz():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5754.8,5840.0,6003.0,6080.9,6149.0,6200.1,6260.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Santa Cruz")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def cauquenes():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5069.9,5162.8,5271.5,5400.6,5495.8,5622.6,5745.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cauquenes")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def chanco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5122.7,5176.3,5369.2,5497.8,5551.4,5658.6,5680.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Chanco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def colbun():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8978.5,9244.4,9461.6,9638.8,9780.6,9980.1,10090.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Colbun")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def constitucion():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8737.2,8866.3,9005.3,9104.6,9241.7,9376.7,9533.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Constitucion")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def curepto():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6248.7,6418.4,6482.1,6598.8,6704.9,6800.3,6832.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Curepto")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def curico():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11373.5,11477.4,11591.1,11687.0,11747.5,11812.3,11842.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Curico")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def empedrado():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7394.2,7536.9,7608.2,7774.6,7798.4,7845.9,7964.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Empedrado")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def hualane():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7161.0,7219.7,7258.9,7356.7,7434.9,7523.0,7620.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Hualane")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def licanten():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8499.1,8542.0,8613.5,8627.8,8728.0,8799.5,8956.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Licanten")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def linares():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8241.6,8355.3,8514.6,8622.5,8739.2,8845.1,8924.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Linares")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def longavi():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9771.4,9975.6,10253.0,10362.7,10466.3,10548.6,10576.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Longavi")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def maule():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7796.7,7918.3,8035.0,8125.0,8223.3,8303.3,8353.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Maule")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def molina():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9265.1,9397.6,9520.1,9622.5,9712.9,9789.2,9911.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Molina")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def parral():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8007.8,8266.0,8488.2,8667.8,8791.3,8964.2,9089.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Parral")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pelarco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8477.4,8664.5,8884.7,9016.8,9071.9,9115.9,9126.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pelarco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pelluhue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6784.5,7031.6,7192.3,7451.8,7587.7,7909.0,8020.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pelluhue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pencahue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8266.5,8487.4,8603.7,8778.0,8824.6,8929.2,8929.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pencahue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def rauco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11086.4,11166.4,11282.0,11344.2,11442.0,11522.0,11593.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Rauco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def retiro():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6938.4,7038.1,7156.8,7394.0,7531.7,7683.5,7835.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Retiro")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def rioclaro():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9028.7,9150.7,9171.0,9238.8,9252.4,9279.5,9435.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Rio Claro")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def romeral():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11144.1,11311.1,11502.8,11583.2,11614.1,11682.1,11756.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Romeral")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sagradafamilia():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6990.6,7119.0,7252.6,7334.7,7442.6,7524.8,7545.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Sagrada Familia")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanclemente():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8692.6,8822.3,9059.9,9224.1,9364.5,9461.7,9563.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Clemente")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanjavier():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9358.8,9453.8,9597.4,9668.2,9743.0,9807.7,9850.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Javier")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanrafael():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10121.5,10382.6,10613.5,10814.3,11025.2,11165.8,11416.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Rafael")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def talca():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8016.9,8145.8,8272.1,8376.0,8451.2,8542.4,8621.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Talca")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def teno():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9218.8,9400.3,9624.0,9753.6,9863.9,9990.3,10022.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Teno")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def vichuquen():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8103.2,8194.5,8308.6,8354.3,8331.4,8399.9,8468.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Vichuquen")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def villaalegre():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6966.7,7086.6,7212.2,7315.0,7429.2,7480.6,7600.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Villa Alegre")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def yerbasbuenas():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8666.7,8807.3,9010.4,9182.3,9312.5,9453.1,9531.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Yerbas Buenas")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def bulnes():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8714.1,8802.6,8886.6,8948.6,9063.6,9099.0,9156.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Bulnes")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def chillan():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8908.8,8987.3,9080.5,9154.0,9226.0,9285.4,9347.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Chillan")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def chillanviejo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7535.4,7612.3,7695.0,7745.3,7798.5,7863.5,7896.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Chillan Viejo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def cobquecura():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [4265.4,4284.4,4379.1,4492.9,4530.8,4549.8,4625.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cobquecura")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def coelemu():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6108.6,6233.3,6292.7,6334.2,6369.8,6399.5,6417.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Coelemu")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def coihueco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7894.3,8063.4,8211.5,8334.8,8398.2,8486.3,8567.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Coihueco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def elcarmen():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5367.3,5415.9,5505.1,5586.2,5651.0,5691.6,5691.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en El Carmen")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def ninhue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7240.5,7536.0,7794.6,7776.1,7794.6,7887.0,7997.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Ninhue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def niquen():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9198.6,9259.1,9336.9,9457.9,9587.6,9622.2,9648.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Niquen")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pemuco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7269.4,7431.4,7616.6,7744.0,7894.4,8056.5,8230.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pemuco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pinto():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5740.7,5841.8,5934.3,6001.7,6085.9,6153.2,262.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pinto")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def portezuelo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5587.0,5668.0,5931.2,6012.1,6093.1,6234.8,6356.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Portezuelo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quillon():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7024.6,7099.1,7242.9,7333.4,7397.3,7493.2,7546.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quillon")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quirihue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6471.5,6602.7,6676.5,6709.3,6791.3,6881.6,6963.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quirihue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def ranquil():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6851.9,7075.5,7107.5,7123.5,7187.4,7251.2,7267.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Ranquil")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sancarlos():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9000.6,9288.6,9464.6,9610.3,9750.8,9848.5,9949.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Carlos")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanfabian():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6553.5,6811.3,6940.3,7069.2,7176.6,7198.1,7219.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Fabian")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanignacio():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6737.2,6863.6,6995.9,7032.0,7098.2,7176.4,7188.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Ignacio")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sannicolas():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9045.3,9185.0,9250.7,9423.3,9521.9,9546.5,9571.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Nicolas")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def treguaco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8093.4,8128.5,8286.5,8321.6,8374.3,8409.4,8462.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Treguaco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def yungay():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6227.1,6350.8,6458.4,6555.2,6646.6,6673.5,6678.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Yungay")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def altobiobio():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [13741.7,13948.3,14066.4,14258.3,14346.9,14524.0,14583.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Alto Biobio")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def antuco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7849.5,8012.1,8128.2,8197.9,8267.5,8383.7,8430.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Antuco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def arauco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11732.5,11846.2,11954.8,12086.7,12205.6,12288.3,2368.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Arauco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def cabrero():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8953.6,9035.0,9171.7,9275.8,9340.9,9393.0,9428.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cabrero")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def canete():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9102.0,9245.2,9369.5,9445.2,9547.9,9631.7,9685.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Canete")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def chiguayante():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9732.4,9833.3,9981.4,10068.0,10155.7,10209.5,10266.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Chiguayante")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def concepcion():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores =[9495.9,9620.2,9698.4,9779.0,9843.3,9908.4,9973.0]
        colores =["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Concepcion")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def contulmo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7788.3,7851.5,7883.1,7914.7,7930.5,7930.5,8041.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Contulmo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def coronel():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11454.4,11545.0,11634.0,11722.3,11856.6,11941.6,12058.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Coronel")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def curanilahue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10961.3,11088.2,11235.7,11395.0,11501.2,	11637.0,11701.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Curanilahue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def florida():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7828.7,7913.2,8031.4,8175.0,8360.8,8495.9,	8597.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Florida")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def hualpen():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10612.4,10724.5,10839.6,10926.0,11041.1,	11112.0,11190.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Hualpen")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def hualqui():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9908.0,9992.0,10114.1,10186.6,10251.5,10301.1,10369.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Hualqui")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def laja():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9596.6,9730.7,9977.8,10086.7,10208.2,10292.0,10388.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Laja")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lebu():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7166.1,7428.0,7597.8,7786.0,8018.5,8177.1,8357.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lebu")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def losalamos():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9256.8,9372.2,9540.9,9629.7,9754.0,9851.7,10011.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Los Alamos")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def losangeles():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10464.7,10627.6,10797.0,10913.7,11010.7,11088.5,11164.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Los Angeles")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lota():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12358.5,12443.7,12592.3,12649.2,12747.5,12795.6,12841.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lota")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def mulchen():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11565.3,11671.7,11803.7,11910.1,12042.1,12135.6,12245.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Mulchen")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def nacimiento():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9279.3,9411.7,9644.3,9801.7,9934.2,	10098.8,10209.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Nacimiento")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def negrete():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12359.8,12522.8,12618.7,12628.2,12705.0,	12791.3,12935.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Negrete")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def penco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10899.4,10983.7,11069.9,11148.1,11228.3,	11278.5,11344.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Penco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quilaco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8686.3,8782.0,8901.7,8949.5,8973.4,8997.4,9069.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quilaco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quilleco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9699.0,9788.7,9838.5,9918.3,9928.2,9978.1,10037.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quilleco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanpedrodelapaz():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9092.2,9199.8,9264.9,9360.8,9454.0,9537.0,9589.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Pedro de la Paz")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanrosendo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8003.3,8003.3,8031.0,8114.1,8141.8,8224.9,8363.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Rosendo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def santabarbara():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9683.4,9875.3,9916.4,9957.5,10012.3,	10046.6,10053.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Santa Barbara")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def santajuana():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9094.0,9242.8,9486.4,9628.5,9905.9,10257.8,10521.7]       
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Santa Juana")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def talcahuano():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10144.3,10219.5,10350.2,10431.7,10507.4,10561.1,10630.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Talcahuano")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def tirua():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9529.0,9665.1,9846.6,9991.8,10345.8,	10518.2,10663.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Tirua")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def tome():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8762.3,8867.9,8942.8,9009.2,9079.0,9159.0,9245.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Tome")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def tucapel():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6530.7,6603.1,6668.9,6767.5,6866.2,6912.2,6964.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Tucapel")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def yumbel():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8151.1,8268.6,8485.5,8661.7,8846.9,8923.7,9032.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Yumbel")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def angol():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10062.8,10134.1,10184.1,10241.2,10342.9,10394.6,10439.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Angol")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def carahue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9499.3,9632.7,9793.6,9966.3,10056.5,	10123.2,10174.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Carahue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def cholchol():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8443.4,8597.4,8751.3,8864.8,8921.5,	9034.9,9099.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cholchol")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def collipulli():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11913.0,12161.5,12280.1,12524.9,12666.4,	12807.9,12926.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Collipulli")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def cunco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8524.0,8679.0,8872.9,9055.7,9111.0,	9127.7,9133.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cunco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def curacautin():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6403.3,6568.4,6634.4,6766.4,6931.5,	7025.0,7096.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Curacautin")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def curarrehue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9907.7,10215.3,10535.8,10663.9,10881.8,	11022.8,11253.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Curarrehue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def ercilla():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [14211.4,14471.5,14684.3,14767.1,15003.5,	15074.5,15180.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Ercilla")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def freire():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9203.8,9404.2,9537.8,9655.7,9820.8,	9868.0,9911.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Freire")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def galvarino():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [16836.9,17058.5,17296.0,17470.1,17731.3,	18024.2,18372.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Galvarino")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def gorbea():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8370.7,8483.0,8628.2,8766.8,8931.9,	8964.9,9077.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Gorbea")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lautaro():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10185.0,10297.9,10376.5,10486.9,10646.4,	10756.9,10872.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lautaro")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def loncoche():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7983.3,8108.7,8274.4,8456.3,8569.5,	8690.7,8787.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Loncoche")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lonquimay():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6706.5,6896.6,7213.3,7349.1,7584.4,	7774.5,7955.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lonquimay")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lossauces():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10695.8,10935.2,11241.2,11467.3,11693.5,	11813.2,11946.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Los Sauces")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lumaco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10636.8,10726.4,10766.2,10806.0,10865.7,	10885.6,10965.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lumaco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def melipeuco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7613.7,7757.4,7917.0,7933.0,8044.7,	8044.7,8044.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Melipeuco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def nuevaimperial():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8896.6,8994.3,9065.3,9154.2,9195.6,	9314.0,9352.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Nueva Imperial")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def padrelascasas():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10675.9,10790.4,10920.7,11019.4,11085.1,11159.4,11213.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Padre Las Casas")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def perquenco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [13941.6,14024.6,14176.9,14301.5,14412.3,	14481.5,14550.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Perquenco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pitrufquen():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9376.9,9583.8,9714.1,9890.4,10005.4,	10108.8,10174.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pitrufquen")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def pucon():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8780.5,9206.9,9401.7,9572.9,9754.2,	9969.1,10137.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Pucon")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def puren():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7819.2,7893.0,7901.2,7942.2,7958.6,	7975.1,7983.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Puren")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def renaico():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [15295.9,15369.7,15535.9,15655.9,15757.4,	15969.7,15997.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Renaico")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def saavedra():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11357.8,11568.8,11779.9,11967.5,12108.2,	12256.7,12319.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Saavedra")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def temuco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9738.5,9830.3,9901.9,9980.5,10052.5,	10114.2,10168.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Temuco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def teodoroschmidt():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7063.2,7303.9,7506.7,7855.1,8000.8,	8317.5,8374.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Teodoro Schmidt")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def tolten():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10263.6,10512.2,10800.6,10989.6,11158.6,	11317.8,11447.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Tolten")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def traiguen():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9231.6,9366.3,9485.3,9568.2,9666.6,	9780.5,9837.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Traiguen")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def victoria():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9352.4,9428.5,9479.2,9546.9,9611.8,	9671.0,9702.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Victoria")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def vilcun():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10365.3,10514.9,10612.4,10761.9,10833.4,	10914.6,11015.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Vilcun")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def villarrica():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8241.5,8492.0,8730.5,8967.4,9231.3,	9424.2,9612.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Villarrica")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def corral():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12337.1,12428.9,12502.3,12612.4,12685.9,	12777.7,12869.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Corral")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def futrono():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [14389.6,14835.2,15143.2,15411.8,15837.8,	16230.9,16683.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Futrono")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def launion():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11869.6,12021.3,12130.1,12286.9,12405.8,	12491.8,12572.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en La Union")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lagoranco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [13039.3,13700.0,14030.3,14584.1,14972.8,	15575.2,15993.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lago Ranco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lanco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11930.7,12196.9,12446.2,12627.5,12791.8,	13001.4,13154.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lanco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def loslagos():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [15162.3,15664.3,15986.0,16166.3,16565.9,	16736.5,16882.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Los Lagos")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def mafil():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [13790.8,13980.2,14196.8,14535.1,14778.7,	14887.0,15062.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Mafil")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def mariquina():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [13238.7,13363.4,13436.6,13608.6,13673.1,	13789.2,13862.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Mariquina")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def paillaco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10698.1,11015.5,11179.0,11380.9,11539.6,	11731.9,11861.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Paillaco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def panguipulli():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11439.0,11908.5,12191.9,12614.3,12964.4,	13453.4,13847.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Panguipulli")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def riobueno():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9837.5,9995.4,10050.1,10195.9,10302.2,	10441.9,10545.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Rio Bueno")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def valdivia():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11014.6,11185.5,11306.5,11442.3,11553.7,	11654.4,11725.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Valdivia")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def ancud():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9918.0,10040.5,10108.8,10179.5,10243.1,	10290.2,10313.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Ancud")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def calbuco():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12290.4,12500.0,12603.4,12649.7,12682.3,	12693.2,12742.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Calbuco")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def castro():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9158.3,9284.3,9412.5,9504.9,9633.0,	9742.3,9788.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Castro")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def chaiten():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [3466.1,3764.9,3904.4,3984.1,4043.8,	4163.3,4163.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Chaiten")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def chonchi():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11009.8,11122.2,11209.6,11259.6,11284.6,	11403.2,11453.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Chonchi")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def cochamo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10209.7,10234.6,10234.6,10259.6,10284.6,	10284.6,10284.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cochamo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def curacodevelez():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9862.3,10083.6,10157.4,10354.2,10378.8,	10403.3,10501.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Curaco de Velez")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def dalcahue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11334.5,11493.8,11546.9,11659.7,11812.3,	11898.6,11965.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Dalcahue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def fresia():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10943.4,11006.6,11030.3,11125.2,11220.0,	11283.2,11346.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Fresia")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def frutillar():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12540.2,12649.0,12757.8,12876.4,12955.5,	13034.7,13123.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Frutillar")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def futaleufu():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [2815.4,2815.4,2851.0,2851.0,2886.7,	2886.7,2922.3]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Futaleufu")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def hualaihue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12105.0,12136.5,12157.5,12189.0,12189.0,	12199.5,12231.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Hualaihue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def llanquihue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [12362.4,12464.4,12534.2,12657.8,12759.8,	12797.4,12899.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Llanquihue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def losmuermos():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11533.9,11573.2,11635.0,11719.1,11780.9,	11853.8,11932.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Los Muermos")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def maullin():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [15234.3,15314.9,15375.3,15408.9,15462.6,	15523.0,15570.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Maullin")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def osorno():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10630.9,10760.6,10835.6,10925.6,11036.3,	11128.5,11209.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Osorno")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def palena():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7225.0,7225.0,7225.0,7279.7,7334.4,	7334.4,7334.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Palena")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def puertomontt():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10701.3,10816.0,10883.2,10943.7,11024.6,	11088.4,11137.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Puerto Montt")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def puertooctay():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9551.8,9617.1,9725.8,9845.5,9899.9,	9954.3,9997.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Puerto Octay")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def puertovaras():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8833.8,8990.1,9088.9,9193.7,9302.8,	9374.7,9415.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Puerto Varas")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def puqueldon():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11663.9,11854.3,11997.1,12282.8,12687.5,	13282.6,13544.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Puqueldon")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def purranque():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11565.5,11660.3,11760.0,11797.9,11864.3,	11935.5,11992.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Purranque")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def puyehue():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10087.4,10180.7,10291.0,10452.2,10604.9,	10698.2,10876.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Puyehue")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def queilen():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7883.8,8100.3,8244.6,8352.9,8551.3,8641.5,8785.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Queilen")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quellon():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8352.4,8441.1,8557.1,8604.9,8642.4,	8710.6,8778.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quellon")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quemchi():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10395.1,10554.5,10577.3,10622.8,10668.3,	10702.5,10736.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quemchi")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def quinchao():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10339.8,10400.1,10448.3,10460.4,10508.6,	10568.8,10592.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Quinchao")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def rionegro():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11649.7,11901.9,12105.1,12252.2,12609.5,	12798.6,13001.8]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Rio Negro")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanjuandelacosta():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [16441.9,16559.8,16651.4,16795.4,16900.1,	17096.5,17175.0]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Juan de la Costa")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sanpablo():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10755.2,10859.5,10935.3,11067.9,11191.1,	11314.3,11418.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Pablo")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def aysen():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5871.5,6143.5,6527.5,6659.5,6827.5,6967.4,7071.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Aysen")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def chilechico():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [7186.1,7420.4,7674.3,7713.3,7791.4,7889.1,7947.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Chile Chico")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def cisnes():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8493.5,9059.7,9265.6,9437.2,9574.5,9711.7,9780.4]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cisnes")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def cochrane():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [5454.5,5590.2,5997.3,6160.1,6377.2,6540.0,6675.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cochrane")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def coyhaique():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8436.5,8601.5,8815.6,9014.9,9134.1,9250.1,9364.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Coyhaique")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def guaitecas():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [11569.7,11569.7,11569.7,11757.3,11757.3,	11757.3,11819.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Guaitecas")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lagoverde():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [4130.4,4347.8,4673.9,4673.9,4565.2,4565.2,4565.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Lago Verde")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def OHiggins():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [1512.9,1512.9,1512.9,1512.9,1512.9,1512.9,1512.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en OHiggins")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def rioibañez():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6150.4,6595.0,7299.0,7447.2,7595.4,7632.5,7669.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Rio Ibañez")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def tortel():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6998.0,7117.3,7395.6,7514.9,7514.9,7594.4,7634.2]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Tortel")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def antartica():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [43065.7,43065.7,43065.7,43065.7,43065.7,	43065.7,43065.7]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Antartica")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def cabodehornos():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [18406.5,18406.5,18406.5,18356.0,18406.5,	18406.5,18406.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Cabo de Hornos")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def lagunablanca():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [9090.9,9090.9,9090.9,9090.9,9090.9,	9090.9,9090.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Laguna Blanca")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def natales():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [22710.5,22861.8,22975.4,23084.7,23118.3,	23164.6,23236.1]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Natales")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def porvenir():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [16004.4,16195.5,16468.7,16564.2,16755.4,	16878.3,16905.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Porvenir")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def primavera():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [8789.6,8789.6,8789.6,8789.6,8789.6,	8789.6,8789.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Primavera")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def puntaarenas():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [17160.4,17268.8,17336.5,17394.9,17425.2,	17473.8,17506.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Punta Arenas")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def rioverde():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [6161.1,6161.1,6161.1,6161.1,6161.1,	7582.9,8056.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Rio Verde")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def sangregorio():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [10425.8,10425.8,10425.8,10425.8,10425.8,	10425.8,10719.5]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en San Gregorio")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def timaukel():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [14893.6,14893.6,14893.6,14893.6,14893.6,	14893.6,14893.6]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Timaukel")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def torresdelpaine():
        from matplotlib import pyplot
        pinchito = ["11/6/21","14/6/21","18/6/21","21/6/21","25/6/21","29/6/21","2/7/21"]
        Valores = [1860.9,1860.9,1860.9,1860.9,1860.9,	1860.9,1860.9]
        colores = ["red","blue","green","pink","yellow","gray","brown"]
        pyplot.title ("Tasa de Incidencia en Torres del Paine")
        pyplot.bar (pinchito, height=Valores,color=colores,width=0.5)
        pyplot.show ()
def graficoregiones():
        from matplotlib import pyplot
        MayorYMenorDensidadTasaDeIncidencia = ["Magallanes","Coquimbo"]
        Valores = [18133.3,6466.7]
        colores = ["red","blue"]
        pyplot.title ("Mayor y menor densidad tasa de incidencia(5/7/21)")
        pyplot.bar (MayorYMenorDensidadTasaDeIncidencia, height=Valores,color=colores,width=0.5)
        pyplot.show ()

# ESTE ES EL MENU 
print("1-Ver una región")
print("2-Ver una comuna")
print("3-Ver región con mayor y menor tasa de incidencia")
print("0-Salir") # 
opción = int(input("Ingrese una opción\n"))

while opción != 0:                 # ESTAS SON LAS OPCIONES


    if opción == 1:                # EN ESTA OPCIÓN  SE MUESTRAN LAS REGIONES                         
        print(Regiónes2,"\n")
        print("0-TERMINAR PROGRAMA")
        r = input("Ingrese una región\n")
        if r == "Tarapaca" or r == "01":
                print("1-ver grafico")          # LAS OPCIONES PARA VER SU GRAFICO O COMUNA 
                print("2-ver comunas de esta región") 
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        tara()    # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(Tarapaca,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "Antofagasta" or r == "02":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        anto() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(Antofagasta,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "Atacama" or r == "03":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        atac() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(Atacama,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "Coquimbo" or r == "04":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        coqu() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(Coquimbo,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "Valparaiso" or r == "05":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        valpa() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(Valparaiso,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "Ohiggins" or r == "06":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        ohig() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(O_Higgins,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0     
        elif r == "Maule" or r == "07":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        ma() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(Maule,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
                
        elif r == "Biobio" or r == "08":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        bi() # MUESTRA SU GRAFICO 
                elif ver == "2": 
                        print(Biobio,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
                
        elif r == "La Araucanía" or r == "09":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        laara() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(La_Araucania,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "Los Lagos" or r == "10":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        los() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(Los_Lagos,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "Aysen" or r == "11":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        ay() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(Aysen,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "Magallanes" or r == "12":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        maga() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(Magallanes_y_la_Antartica,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "Metropolitana" or r == "13":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        metro() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(Metropolitana,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "Los Rios" or r == "14":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        rios() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(Los_Rios,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "Arica y Parinacota" or r == "15":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        ari() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(AricayParinacota,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "Ñuble" or r == "16":
                print("1-ver grafico")
                print("2-ver comunas de esta región")
                print("0-TERMINAR PROGRAMA")
                ver = input("Ingrese una opción\n")
                if ver == "1":
                        ñu() # MUESTRA SU GRAFICO 
                elif ver == "2":
                        print(Ñuble,"\n","----------°----------")# AQUI MUESTRA TODAS LAS COMUNAS DE ESA REGIÓN 
                opción = 0
        elif r == "0":
                opción = 0
        else:
                print("Error, Ingrese región valida\n") # AQUI ES POR SI SE EQUIVOCAN DE OPCIÓN
                print(Regiónes2)              

    elif opción == 2:            # EN ESTA OPCIÓN ESTAN TODAS LAS COMUNAS CON SU GRAFICO 
        print(Comunas)
        print("0-TERMINAR PROGRAMA")  # CON ESTA OPCIÓN SE CIERRA EL PROGRAMA 
        c = input("Mostrar grafico de\n")   
        if c == "Arica" or c == "15101":
                arica() # MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Camarones" or c == "15102":
                camarones()
                opción = 0 
        elif c == "General Lagos" or c == "15202":
                generallagos()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Putre" or c == "15201":
                putre()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Alto Hospicio" or c == "01107":
                altohospicio()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Camina" or c == "01402":
                camina()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Colchane" or c == "01403":
                colchane()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Huara" or c == "01404":
                huara()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Iquique" or c == "01101":
                iquique()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Pica" or c == "01405":
                pica()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Pozo Almonte" or c == "01401":
                pozoalmonte()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Antofagasta" or c == "02101":
                antofagasta()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Calama" or c == "02201":
                calama()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Maria Elena" or c == "02302":
                mariaelena()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Mejillones" or c == "02102":
                mejillones()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Ollague" or c == "02202":
                ollague()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "San Pedro de Atacama" or c == "02203":
                sanpedrodeatacama()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Sierra Gorda" or c == "02103":
                sierragorda()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Taltal" or  c == "02104":
                taltal()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Tocopilla" or c == "02301":
                tocopilla()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Alto del Carmen" or  c == "03302":
                altodelcarmen()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Caldera" or c == "03102":
                caldera()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Chanaral" or c == "03201":
                chanaral()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Copiapo" or c == "03101":
                copiapo()
                opción = 0 
        elif c == "Diego de Almagro" or c == "03202":
                diegodealmagro()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Freirina" or c == "03303":
                freirina()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Huasco" or c == "03304":
                huasco()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Tierra Amarilla" or c == "03103":
                tierraamarilla()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Vallenar" or  c == "03301":
                vallenar()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Andacollo" or c == "04103":
                andacollo()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Canela" or c == "04202":
                canela()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Combarbala" or c == "04302":
                combarbala()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Coquimbo" or c == "04102":
                coquimbo()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Illapel" or c == "04201":
                illapel()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "La Higuera" or c == "04104":
                lahiguera()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "La Serena" or c == "04101":
                laserena()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Los Vilos" or c == "04203":
                losvilos()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Monte Patria" or c == "04303":
                montepatria()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Ovalle" or c == "04301":
                ovalle()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Paiguano" or c == "04105":
                paiguano()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Punitaqui" or c == "04304":
                punitaqui()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Rio Hurtado" or c == "04305":
                riohurtado()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Salamanca" or c == "04204":
                salamanca()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Vicuña" or c == "04106":
                vicuña()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Algarrobo" or c == "05602":
                algarrobo()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Cabildo" or c == "05402":
                cabildo()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Calera" or c == "05502":
                calera()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Calle Larga" or c == "05302":
                callelarga()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Cartagena" or c == "05603":
                cartagena()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Casablanca" or  c == "05102":
                casablanca()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Catemu" or c == "05702":
                catemu()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Concon" or c == "05103":
                concon()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "El Quisco" or c == "05604":
                elquisco()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "El Tabo" or c == "05605":
                eltabo()# MUESTRA SU GRAFICO 
        elif c == "Hijuelas" or c == "05503":
                hijuelas()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Isla de Pascua" or  c == "05201":
                isladepascua()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Juan Fernandez" or c == "05104":
                juanfernandez()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "La Cruz" or c == "05504":
                lacruz()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "La Ligua" or c == "05401":
                laligua()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Limache" or c == "05802":
                limache() # MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Llaillay" or c == "05703":
                llaillay()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Los Andes" or c == "05301":
                losandes()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Nogales" or c == "05506":
                nogales()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Olmue" or c == "05803":
                olmue()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Panquehue" or c == "05704":
                panquehue()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Papudo" or c == "05403":
                papudo()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Petorca" or c == "05404":
                petorca()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Puchuncavi" or c == "05105":
                puchuncavi()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Putaendo" or c == "05705":
                putaendo()# MUESTRA SU GRAFICO 
                opción = 0 
        elif c == "Quillota" or c == "05501":
                quillota()# MUESTRA SU GRAFICO
                opción = 0 
        elif c == "Quilpue" or c == "05801":
                quilpue()# MUESTRA SU GRAFICO
                opción = 0 
        elif c == "Quintero" or c == "05107":
                quintero()# MUESTRA SU GRAFICO
                opción = 0 
        elif c == "Rinconada" or c == "05303":
                rinconada()# MUESTRA SU GRAFICO
                opción = 0 
        elif c == "San Antonio" or c == "05601":
                sanantonio()# MUESTRA SU GRAFICO
                opción = 0 
        elif c == "San Esteban" or c == "05304":
                sanesteban()# MUESTRA SU GRAFICO
                opción = 0 
        elif c == "San Felipe" or c == "05701":
                sanfelipe()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Santa Maria" or c == "05706":
                santamaria()
                opción = 0
        elif c == "Santo Domingo" or c == "05606":
                santodomingo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Valparaiso" or c == "05101":
                valparaiso()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Villa Alemana" or c == "05804":
                villaalemana()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Viña del Mar" or c == "05109":
                viñadelmar()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Zapallar" or c == "05405":
                zapallar()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Alhue" or c == "13502":
                alhue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Buin" or c == "13402":
                buin()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Calera de Tango" or c == "13403":
                caleradetango()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Cerrillos" or c == "13102":
                Cerrillos()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Cerro Navia" or c == "13103":
                cerronavia()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Colina" or c == "13301":
                colina()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Conchali" or c == "13104":
                conchali()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Curacavi" or c == "13503":
                curacavi()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "El Bosque" or c == "13105":
                elbosque()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "El Monte" or c == "13602":
                elmonte()
                opción = 0
        elif c == "Estacion Central" or c == "13106":
                estacioncentral()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Huechuraba" or c == "13107":
                huechuraba()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Independencia" or c == "13108":
                independencia()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Isla de Maipo" or c == "13603":
                islademaipo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "La Cisterna" or c == "13109":
                lacisterna()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "La Florida" or c == "13110":
                laflorida()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "La Granja" or c == "13111":
                lagranja()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "La Pintana" or c == "13112":
                lapintana()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "La Reina" or c == "13113":
                lareina()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lampa" or c == "13302":
                lampa()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Las Condes" or c == "13114":
                lascondes()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lo Barnechea" or c == "13115":
                lobarnechea()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lo Espejo" or c == "13116":
                loespejo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lo Prado" or c == "13117":
                loprado()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Macul" or c == "13118":
                macul()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Maipu" or c == "13119":
                maipu()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Maria Pinto" or c == "13504":
                mariapinto()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Melipilla" or c == "13501":
                melipilla()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Ñuñoa" or c == "13120":
                nuñoa()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Padre Hurtado" or c == "13604":
                padrehurtado()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Paine" or c == "13404":
                paine()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pedro Aguirre Cerda" or c == "13121":
                pedroaguirrecerda()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Peñaflor" or c == "13605":
                penaflor()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Peñalolen" or c == "13122":
                penalolen()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pirque" or c == "13202":
                pirque()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Providencia" or c == "13123":
                providencia()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pudahuel" or c == "13124":
                pudahuel()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Puente Alto" or c == "13201":
                puentealto()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Quilicura" or c == "13125":
                quilicura()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Quinta Normal" or c == "13126":
                quintanormal()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Recoleta" or c == "13127":
                recoleta()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Renca" or c == "13128":
                renca()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Bernardo" or c == "13401":
                sanbernardo()# MUESTRA SU GRAFICO
                opción= 0
        elif c == "San Joaquin" or c == "13129":
                sanjoaquin()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Jose de Maipo" or c == "13203":
                sanjosedemaipo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Miguel" or c == "13130":
                sanmiguel()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Pedro" or c == "13505":
                sanpedro()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Ramon" or c == "13131":
                sanramon()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Santiago" or c == "13101":
                santiago()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Talagante" or c == "13601":
                talagante()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Tiltil" or c == "13303":
                tiltil()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Vitacura" or c == "13132":
                vitacura()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Chepica" or c == "06302":
                chepica()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Chimbarongo" or c == "06303":
                chimbarongo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Codegua" or c == "06102":
                codegua()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Coinco" or c == "06103":
                Coinco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Coltauco" or c == "06104":
                coltauco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Donihue" or c == "06105":
                donihue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Graneros" or c == "06106":
                graneros()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "La Estrella" or c == "06202":
                laestrella()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Las Cabras" or c == "06107":
                lascabras()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Litueche" or c == "06203":
                litueche()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lolol" or c == "06304":
                lolol()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Machali" or c == "06108":
                machali()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Malloa" or c == "06109":
                malloa()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Marchihue" or c == "06204":
                marchihue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Mostazal" or c == "06110":
                mostazal()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Nancagua" or c == "06305":
                nancagua()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Navidad" or c == "06205":
                navidad()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Olivar" or c == "06111":
                olivar()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Palmilla" or c == "06306":
                palmilla()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Paredones" or c == "06206":
                paredones()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Peralillo" or c == "06307":
                peralillo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Peumo" or c == "06112":
                peumo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pichidegua" or c == "06113":
                pichidegua()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pichilemu" or c == "06201":
                pichilemu()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Placilla" or c == "06308":
                placilla()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pumanque" or c == "06309":
                pumanque()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Quinta de Tilcoco" or c == "06114":
                quintadetilcoco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Rancagua" or c == "06101":
                rancagua()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Rengo" or c == "06115":
                rengo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Requinoa" or c == "06116":
                requinoa()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Fernando" or c == "06301":
                sanfernando()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Vicente" or c == "06117":
                sanvicente()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Santa Cruz" or c == "06310":
                santacruz()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Cauquenes" or c == "07201":
                cauquenes()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Chanco" or c == "07202":
                chanco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Colbun" or c == "07402":
                colbun()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Constitucion" or c == "07102":
                constitucion()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Curepto" or c == "07103":
                curepto()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Curico" or c == "07301":
                curico()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Empedrado" or c == "07104":
                empedrado()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Hualane" or c == "07302":
                hualane()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Licanten" or c == "07303":
                licanten()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Linares" or c == "07401":
                linares()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Longavi" or c == "07403":
                longavi()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Maule" or c == "07105":
                maule()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Molina" or c == "07304":
                molina()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Parral" or c == "07404":
                parral()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pelarco" or c == "07106":
                pelarco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pelluhue" or c == "07203":
                pelluhue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pencahue" or c == "07107":
                pencahue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Rauco" or c == "07305":
                rauco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Retiro" or c == "07405":
                retiro()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Rio Claro" or c == "07108":
                rioclaro()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Romeral" or c == "07306":
                romeral()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Sagrada Familia" or c == "07307":
                sagradafamilia()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Clemente" or c == "07109":
                sanclemente()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Javier" or c == "07406":
                sanjavier()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Rafael" or c == "07110":
                sanrafael()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Talca" or c == "07101":
                talca()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Teno" or c == "07308":
                teno()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Vichuquen" or c == "07309":
                vichuquen()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Villa Alegre" or c == "07407":
                villaalegre()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Yerbas Buenas" or c == "07408":
                yerbasbuenas()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Bulnes" or c == "16102":
                bulnes()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Chillan" or c == "16101":
                chillan()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Chillan Viejo" or c == "16103":
                chillanviejo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Cobquecura" or c == "16202":
                cobquecura()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Coelemu" or c == "16203":
                coelemu()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Coihueco" or c == "16302":
                coihueco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "El Carmen" or c == "16104":
                elcarmen()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Ninhue" or c == "16204":
                ninhue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Niquen" or c == "16303":
                niquen()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pemuco" or c == "16105":
                pemuco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pinto" or c == "16106":
                pinto()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Portezuelo" or c == "16205":
                portezuelo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Quillon" or c == "16107":
                quillon()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Quirihue" or c == "16201":
                quirihue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Ranquil" or c == "16206":
                ranquil()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Carlos" or c == "16301":
                sancarlos()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Fabian" or c == "16304":
                sanfabian()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Ignacio" or c == "16108":
                sanignacio()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Nicolas" or c == "16305":
                sannicolas()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Treguaco" or c == "16207":
                treguaco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Yungay" or c == "16109":
                yungay()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Alto Biobio" or c == "08314":
                altobiobio()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Antuco" or c == "08302":
                antuco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Arauco" or c == "08202":
                arauco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Cabrero" or c == "08303":
                cabrero()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Canete" or c == "08203":
                canete()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Chiguayante" or c == "08103":
                chiguayante()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Concepcion" or c == "08101":
                concepcion()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Contulmo" or c == "08204":
                contulmo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Coronel" or c == "08102":
                coronel()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Curanilahue" or c == "08205":
                curanilahue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Florida" or c == "08104":
                florida()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Hualpen" or c == "08112":
                hualpen()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Hualqui" or c == "08105":
                hualqui()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Laja" or c == "08304":
                laja()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lebu" or c == "08201":
                lebu()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Los Alamos" or c == "08206":
                losalamos()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Los Angeles" or c == "08301":
                losangeles()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lota" or c == "08106":
                lota()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Mulchen" or c == "08305":
                mulchen()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Nacimiento" or c == "08306":
                nacimiento()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Negrete" or c == "08307":
                negrete()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Penco" or c == "08107":
                penco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Quilaco" or c == "08308":
                quilaco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Quilleco" or c == "08309":
                quilleco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Pedro de la Paz" or c == "08108":
                sanpedrodelapaz()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Rosendo" or c == "08310":
                sanrosendo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Santa Barbara" or c == "08311":
                santabarbara()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Santa Juana" or c == "08109":
                santajuana()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Talcahuano" or c == "08110":
                talcahuano()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Tirua" or c == "08207":
                tirua()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Tome" or c == "08111":
                tome()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Tucapel" or c == "Tucapel":
                tucapel()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Yumbel" or c == "08313":
                yumbel()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Angol" or c == "09201":
                angol()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Carahue" or c == "09102":
                carahue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Cholchol" or c == "09121":
                cholchol()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Collipulli" or c == "09202":
                collipulli()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Cunco" or c == "09103":
                cunco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Curacautin" or c == "09203":
                curacautin()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Curarrehue" or c == "09104":
                curarrehue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Ercilla" or c == "09204":
                ercilla()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Freire" or c == "09105":
                freire()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Galvarino" or c == "09106":
                galvarino()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Gorbea" or c == "09107":
                gorbea()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lautaro" or c == "09108":
                lautaro()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Loncoche" or c == "09109":
                loncoche()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lonquimay" or c == "09205":
                lonquimay()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Los Sauces" or c == "09206":
                lossauces()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lumaco" or c == "09207":
                lumaco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Melipeuco" or c == "09110":
                melipeuco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Nueva Imperial" or c == "09111":
                nuevaimperial()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Padre Las Casas" or c == "09112":
                padrelascasas()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Perquenco" or c == "09113":
                perquenco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pitrufquen" or c == "09114":
                pitrufquen()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Pucon" or c == "09115":
                pucon()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Renaico" or c == "09209":
                renaico()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Saavedra" or c == "09116":
                saavedra()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Temuco" or c == "09101":
                temuco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Teodoro Schmidt" or c == "09117":
                teodoroschmidt()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Tolten" or c == "09118":
                tolten()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Traiguen" or c == "09210":
                traiguen()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Victoria" or c == "09211":
                victoria()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Vilcun" or c == "09119":
                vilcun()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Villarrica" or c == "09120":
                villarrica()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Corral" or c == "Corral":
                corral()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Futrono" or c == "14202":
                futrono()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "La Union" or c == "14201":
                launion()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lago Ranco" or c == "14203":
                lagoranco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lanco" or c == "14103":
                lanco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Los Lagos" or c == "14104":
                loslagos()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Mafil" or c == "14105":
                mafil()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Mariquina" or c == "14106":
                mariquina()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Paillaco" or c == "14107":
                paillaco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Panguipulli" or c == "14108":
                panguipulli()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Rio Bueno" or c == "14204":
                riobueno()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Valdivia" or c == "14101":
                valdivia()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Ancud" or c == "10202":
                ancud()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Calbuco" or c == "10102":
                calbuco()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Castro" or c == "10201":
                castro()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Chaiten" or c == "10401":
                chaiten()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Chonchi" or c == "10203":
                chonchi()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Cochamo" or c == "10103":
                cochamo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Curaco de Velez" or c == "10204":
                curacodevelez()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Dalcahue" or c == "10205":
                dalcahue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Fresia" or c == "10104":
                fresia()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Frutillar" or c == "Frutillar":
                frutillar()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Futaleufu" or c == "10402":
                futaleufu()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Hualaihue" or c == "10403":
                hualaihue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Llanquihue" or c == "10107":
                llanquihue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Los Muermos" or c == "10106":
                losmuermos()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Maullin" or c == "Maullin":
                maullin()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Osorno" or c == "10301":
                osorno()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Palena" or c == "10404":
                palena()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Puerto Montt" or c == "10101":
                puertomontt()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Puerto Octay" or c == "10302":
                puertooctay()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Puerto Varas" or c == "10109":
                puertovaras()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Puqueldon" or c == "10206":
                puqueldon()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Purranque" or c == "10303":
                purranque()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Puyehue" or c == "10304":
                puyehue()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Queilen" or c == "10207":
                queilen()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Quellon" or c == "10208":
                quellon()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Quemchi" or c == "10209":
                quemchi()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Quinchao" or c == "10210":
                quinchao()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Rio Negro" or c == "10305":
                rionegro()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Juan de la Costa" or c == "10306":
                sanjuandelacosta()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Pablo" or c == "10307":
                sanpablo()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Aysen" or c == "11201":
                aysen()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Chile Chico" or c == "11401":
                chilechico()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Cisnes" or c == "11202":
                cisnes()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Cochrane" or c == "11301":
                cochrane()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Coyhaique" or c == "11101":
                coyhaique()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Guaitecas" or c == "11203":
                guaitecas()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Lago Verde" or c == "11102":
                lagoverde()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "OHiggins" or c == "11302":
                OHiggins()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Rio Ibañez" or c == "11402":
                rioibañez()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Tortel" or c == "11303":
                tortel()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Antartica" or c == "12202":
                antartica()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Cabo de Hornos" or c == "12201":
                cabodehornos()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Laguna Blanca" or c == "12102":
                lagunablanca()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Natales" or c == "12401":
                natales()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Porvenir" or c == "12301":
                porvenir()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Primavera" or c == "12302":
                primavera()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Punta Arenas" or c == "12101":
                puntaarenas()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Rio Verde" or c == "12103":
                rioverde()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "San Gregorio" or c == "12104":
                sangregorio()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Timaukel" or c == "12303":
                timaukel()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "Torres del Paine" or c == "12402":
                torresdelpaine()# MUESTRA SU GRAFICO
                opción = 0
        elif c == "0":         # CON ESTA OPCIÓN SE CIERRA EL PROGRAMA  
                opción = 0
        else :
                print("Ingrese una comuna valida") # AQUI ES POR SI SE EQUIVOCAN DE OPCIÓN

 
    elif opción == 3: # AQUI MUESTRA  LA REGION CON MAYOR Y MENOR TASA DE INCIDENCIA 
        graficoregiones()
        opción = 0
    
    else:
        opción = int(input("Error, Ingrese una opción valida\n"))  # AQUI ES POR SI SE EQUIVOCAN DE OPCIÓN