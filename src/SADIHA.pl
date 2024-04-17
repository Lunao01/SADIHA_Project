%----------------------------------------------------%                                               
%                       HECHOS                       %
%----------------------------------------------------%

% ¿Tiene sombrero?
tiene_sombrero(si).
tiene_sombrero(no).

% ¿Tamaño del sombrero? diametro_sombrero(min,max).
diametro_sombrero(2,4).

% ¿Forma del sombrero?
forma_sombrero(convexo).
forma_sombrero(plano).
forma_sombrero(coraloide).
forma_sombrero(centro_hundido).

% ¿Color del sombrero?
color_sombrero(pardo_oscuro).
color_sombrero(rosa_claro).
color_sombrero(pardo_rojizo).
color_sombrero(anaranjado).
color_sombrero(ocre).
color_sombrero(blanquecino).
color_sombrero(escarlata).
color_sombrero(pardo_gris).
color_sombrero(verde_azulado).
color_sombrero(amarillento).
color_sombrero(negruzco).

% ¿Superficie del sombrero?
superficie_sombrero(aterciopelada).
superficie_sombrero(seca).
superficie_sombrero(viscosa).
superficie_sombrero(lisa).
superficie_sombrero(escamada).

% ¿Forma del carpóforo? (en el caso de no tener sombrero)
forma_carpoforo(oreja).
forma_carpoforo(semicircular).
forma_carpoforo(pezuna).

% ¿Color carpoforo?
color_carpoforo(pardo_oscuro).
color_carpoforo(marron_rojizo).
color_carpoforo(pardo_gris).
color_carpoforo(rojo_cinabrio).
color_carpoforo(grisaceo).
color_carpoforo(pardo_rojizo).
color_carpoforo(circulos_concentricos_pardos_y_blanquecinos).

% ¿Superficie del carpóforo?
superficie_carpoforo(gelatinosa).
superficie_carpoforo(aterciopelada).
superficie_carpoforo(rugosa).
superficie_carpoforo(seca).
superficie_carpoforo(resinosa).

% ¿Tipo de himenio?
tipo_himenio(plegado).
tipo_himenio(laminado).
tipo_himenio(poroso).
tipo_himenio(aguijones).
tipo_himenio(liso).

% ¿Color de himenio?
color_himenio(pardo_oscuro).
color_himenio(marron_rojizo).
color_himenio(blanquecino).
color_himenio(anaranjado).
color_himenio(amarillento).
color_himenio(pardo_rojizo).
color_himenio(rosado).
color_himenio(verde_palido).
color_himenio(pardo_gris).
color_himenio(rojo_cinabrio).
color_himenio(gris_claro).

% ¿Tipo de láminas? (para el caso de tener un himenio laminado)
tipo_laminas(apretadas).
tipo_laminas(separadas).
tipo_laminas(bifurcadas).
tipo_laminas(anastomasadas).

% ¿Tiene pie?
tiene_pie(si).
tiene_pie(no).

% ¿Pie con anillo?
pie_anillo(si).
pie_anillo(no).

% ¿Color de pie? 
color_pie(ocre).
color_pie(amarillento).
color_pie(pardo_rojizo).
color_pie(blanquecino).
color_pie(pardo).
color_pie(verde_azulado).
color_pie(pardo_oscuro).
color_pie(negruzco).
color_pie(grisaceo).

% ¿Tipo de pie?
tipo_pie(grueso).
tipo_pie(fino).
tipo_pie(proporcional).


% Rasgos comunes de las distintas órdenes (un total de 6 órdenes)
orden(agaricales)   :-  tiene_sombrero(si), 
                        tipo_himenio(laminado), 
                        tiene_pie(si).

orden(auriculariales)   :-  superficie_carpoforo(gelatinosa), 
                            tipo_himenio(plegado).

orden(boletales)    :-  tiene_sombrero(si), 
                        tiene_pie(si).

orden(polyporales)  :-  tiene_sombrero(no), 
                        tipo_himenio(poroso), 
                        tiene_pie(no).

orden(thelephorales)    :-  forma_sombrero(coraloide).

orden(cantharellales)   :-  tiene_sombrero(si),
                            forma_sombrero(centro_hundido). 



%% SETAS DE LA ORDEN DE LAS Auriculariales (orden 2)
seta(auricularia_auricula-judae)    :-  orden(auriculariales), 
                                        tiene_sombrero(no), 
                                        forma_carpoforo(oreja), 
                                        color_carpoforo(pardo_oscuro), 
                                        color_himenio(pardo_oscuro), 
                                        tiene_pie(no).

seta(auricularia_mesenterica)   :-  orden(auriculariales),
                                    tiene_sombrero(no), 
                                    forma_carpoforo(semicircular), 
                                    color_carpoforo(marron_rojizo), 
                                    color_himenio(marron_rojizo), 
                                    tiene_pie(no).


%% SETAS DE LA ORDEN DE LAS Thelephorales (orden 5)
seta(hydnellum_ferrugineum) :-  orden(thelephorales),
                                tiene_sombrero(si),
                                diametro_sombrero(2,4).


seta(thelephora_terrestris) :-  orden(thelephorales).

