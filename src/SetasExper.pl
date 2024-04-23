/* Sistema experto de idetificación y clasificación de setas,
*  para la asignatura de Programación Declarativa- Curso 2023/2024.
*   Autores:
*  - Alberto Barrais Bellerín
*  - Franciosco Javier Luna Ortiz
*
*  Versión 1.0
*  Fecha: 18/04/2024
*
*  Descripción:
*  El sistema experto es un programa que permite identificar y clasificar 
*  setas en función de sus características.
*  Para ello, se ha utilizado una base de conocimiento que contiene las
*  características de las setas y las reglas que permiten clasificarlas.
*  
*
*  La base de datos contine la información de 25 especies de setas que habitan la 
*  peninsula iberica.
*
*
*  Uso:
*  Para utilizar el sistema experto, el usuario debe ejecutar el archivo "interface.py".
*/
:- dynamic known/3. % Para saber si se conoce una característica
:- dynamic salida/2. % Respuestas que se mostrarán en la interfaz: Habitat y comestibilidad
:- discontiguous seta/1. % Para que no de warning

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% INICIALIZACIÓN  (NOTE:USO EXPLUSIVO PARA PRUEBAS)%%%
iniciar :-
    assert(known(yes, sombrero, 'si')),
    assert(known(yes, 'superficie sombrero', 'seca')),
    assert(known(yes, 'tamano sombrero', 7)),
    assert(known(yes, sombrero, convexo)),
    assert(known(yes, 'forma sombrero', 'convexo')),
    assert(known(yes, 'color sombrero', 'blanquecino')),
    assert(known(yes, 'color himenio', 'rosado')),
    assert(known(yes, 'tipo laminas', 'apretadas')),
    assert(known(yes, pie, 'si')),
    assert(known(yes, 'anillo', 'si')),
    assert(known(yes, 'tipo himenio', laminado)),
    assert(known(yes, 'color pie', 'blanquecino')),
    assert(known(yes, 'tipo pie', 'grueso')).

iniciar :- true.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% CLAUSULAS DE VERIFICACIÓN %%%
verificar(A, ValorDeseado, MenuList) :- 
    (known(yes, A, ValorRecordado)->true;fail),
    verificarExiseCaracteristica(ValorRecordado,MenuList),
    ValorDeseado == ValorRecordado. 

verificarTamano(Valormax, Valormin):-
    (
        (
            known(yes, 'tamano sombrero', Valor),
            Valor >= Valormin,
            Valor =< Valormax
        )
        ->true;fail
    ).

verificarExiseCaracteristica(Valor,MenuList):-
    member(Valor, MenuList), 
    !. 

%%% CLAUSULAS AUXILIARES %%%    

% Borra todas las características conocidas y las salidas
limpiar :- retractall(known(_,_,_)), retractall(salida(_,_)).
limpiar :- true.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% CARACTERISTICAS %%%

%% Características: Sombrero %%
% Tiene sombrero
sombrero(X) :- verificar(sombrero, X, ['si', 'no']).
% Forma del sombrero
sombrero_forma(X) :- verificar('forma sombrero', X, ['convexo', 'plano', 'coraloide', 'centro hundido']).
% Color del sombrero
sombrero_color(X) :- verificar('color sombrero', X, ['pardo oscuro', 'rosa claro', 'pardo rojizo', 'anaranjado', 'ocre', 'blanquecino', 'escarlata', 'pardo gris', 'verde azulado', 'amarillento', 'negruzco']).
% Superficie del sombrero
sombrero_superficie(X) :- verificar('superficie sombrero', X, ['aterciopelada', 'seca', 'viscosa', 'lisa', 'escamada']).
% Tamaño del sombrero
sombrero_tamano(Vmin,Vmax) :- verificarTamano(Vmax,Vmin).

%% Características: Carpóforo %%
% Forma del carpóforo
carpoforo_forma(X) :- verificar('forma carpoforo', X, ['oreja','semicircular','pezuna']).
% Color del carpóforo
carpoforo_color(X) :- verificar('color carpoforo', X, ['pardo oscuro', 'marron rojizo', 'pardo gris', 'rojo cinabrio','grisaceo', 'pardo rojizo', 'circulo concentrico pardos y blanquecinos']).
% Superficie del carpóforo
carpoforo_superficie(X) :- verificar('superficie carpoforo', X, ['gelatinosa', 'aterciopelada', 'rugosa', 'seca', 'resinosa']).

%% Características: Himenio %%
% Tipo de himenio
himenio_tipo(X) :- verificar('tipo himenio', X, ['plegado', 'laminado', 'poroso', 'aguijones', 'liso']).
% Color del himenio
himenio_color(X) :- verificar('color himenio', X, ['pardo oscuro', 'marron rojizo', 'blanquecino', 'anaranjado', 'amarillento', 'pardo rojizo', 'rosado', 'verde palido', 'pardo gris', 'rojo cinabrio', 'gris claro']).
% Tipo de láminas
laminas_tipo(X) :- verificar('tipo laminas', X, ['apretadas', 'separadas', 'bifurcadas', 'anastomasadas']).

%% Características: Pie %%
% Tiene pie
pie(X) :- verificar(pie, X, ['si', 'no']).
% Tiene anillo
pie_anillo(X) :- verificar(anillo, X, ['si', 'no']).
% Color del pie
pie_color(X) :- verificar('color pie', X, ['ocre', 'amarillento', 'pardo rojizo', 'blanquecino', 'pardo', 'verde azulado', 'pardo oscuro', 'negruzco', 'grisaceo']).
% Tipo de pie
pie_tipo(X) :- verificar('tipo pie', X, ['grueso', 'fino', 'proporcional']).


%%% ORDENES %%%

orden('Agaricales'):-
    sombrero('si'),
    himenio_tipo('laminado'),
    pie('si').

orden('Boletales'):-
    sombrero('si'),
    pie('si').

orden('Auriculariales'):-
    sombrero('no'),
    carpoforo_superficie('gelatinosa'),
    himenio_tipo('plegado'),
    pie('no').

orden('Polyporales'):-
    sombrero('no'),
    himenio_tipo('poroso'),
    pie('no').

orden('Thelephorales'):-
    sombrero('si'),
    sombrero_forma('coraloide'),
    pie('si'),
    pie_anillo('no').

orden('Cantharellales'):-
    sombrero('si'),
    sombrero_forma('centro hundido'),
    pie('si'),
    pie_anillo('no').

%%% FAMILIAS %%%
familia('Amanitaceae'):-
    orden('Agaricales'),
    sombrero_superficie('escamada'),
    himenio_color('blanquecino'),
    pie_anillo('si'),
    pie_color('blanquecino'),
    pie_tipo('proporcional').

familia('Boletaceae'):-
    orden('Boletales'),
    sombrero_forma('convexo'),
    himenio_tipo('poroso'),
    pie_anillo('no'),
    pie_tipo('grueso').

%%% SETAS %%%

%% Aaricales %%
seta('Agaricus arvensis'):-
    orden('Agaricales'),
    sombrero_forma('convexo'),
    sombrero_tamano(7,20),
    sombrero_color('blanquecino'),
    sombrero_superficie('seca'),
    himenio_color('rosado'),
    laminas_tipo('apretadas'),
    pie_anillo('si'),
    pie_color('blanquecino'),
    pie_tipo('grueso'),
    assertz(salida(habitat,'Suele dar un primer brote en primavera, en el otoño vuelve a aparecer de nuevo, ligada normalmente a los pastizales y campas, aunque también la hemos visto en claros herbosos de pinares.')),
    assertz(salida(comestibilidad,'Constituye un buen comestible esta seta habitual en las campas de nuestra geografía, recolectable solo en estado joven, cuando las láminas no se han puesto todavía marrones. Es ciertamente parecida la especie, también comestible, Agaricus urinascens, propia de pastizales de montaña y páramos, de tamaño aún más grande y con la cutícula netamente agrietada.')).

seta('Amanita muscaria'):-
    familia('Amanitaceae'),
    sombrero_tamano(5,25),
    sombrero_forma('convexo'),
    sombrero_color('escarlata'),
    laminas_tipo('separadas'),
    assertz(salida(habitat,'Es muy abundante en algunas zonas, y encuentra especialmente en bosques de coníferas y en menor grado de planifolios, sobre suelos preferentemente ácidos, y con mayor frecuencia en áreas de media y alta montaña. Los cuerpos fructíferos aparecen a finales de verano y durante el otoño.')),
    assertz(salida(comestibilidad,'Es una seta muy venenosa, de hecho, el nombre de "muscaria" y su nombre común alternativo "matamoscas" indica su capacidad de paralizar a los insectos que entran en contacto con ella. En grandes cantidades pueden inducir al coma.')).

seta('Amanita pantherina'):-
    familia('Amanitaceae'),
    sombrero_tamano(3,14),
    (
        sombrero_forma('convexo'); 
        sombrero_forma('plano')
    ),
    sombrero_color('pardo gris'),
    laminas_tipo('apretadas'),
    assertz(salida(habitat,'Es una especie frecuente y otoñal, que sale por igual en bosques de coníferas y de planifolios, sobre todo en los claros de los propios bosques.')),
    assertz(salida(comestibilidad,'Es una especie muy tóxica, que comida en grandes cantidades puede provocar graves envenenamientos, además no tiene mal sabor por lo que resulta muy peligrosa.')).

seta('Callistosporium luteo-olivaceum'):-
    orden('Agaricales'),
    sombrero_forma('convexo'),
    sombrero_tamano(1,4), % NOTA: 1.5 - 4
    sombrero_color('ocre'),
    sombrero_superficie('seca'),
    himenio_color('amarillento'),
    laminas_tipo('apretadas'),
    pie_anillo('no'),
    pie_color('ocre'),
    pie_tipo('fino'),
    assertz(salida(habitat,'Crece en otoño formando pequeños grupos sobre restos de madera en descomposición.')),
    assertz(salida(comestibilidad,'Sin ser tóxica, la calidad de su carne no invita al consumo.')).

seta('Clitocybe odora'):-
    orden('Agaricales'),
    sombrero_forma('convexo'),
    sombrero_tamano(1,8),
    sombrero_color('verde azulado'),
    sombrero_superficie('lisa'),
    himenio_color('verde palido'),
    laminas_tipo('separadas'),
    pie_anillo('no'),
    pie_color('verde azulado'),
    pie_tipo('fino'),
    assertz(salida(habitat,'Vive en bosques de coníferas o planifolios siendo frecuente de agosto a noviembre. Posee un intenso olor a anís.')),
    assertz(salida(comestibilidad,' Es una especie comestible pero de mala calidad, utilizable solo mezclada con otras setas. El molesto olor a anís se conserva al cocinarlo.')).

seta('Armillaria gallica'):-
    orden('Agaricales'),
    sombrero_forma('convexo'),
    sombrero_tamano(5,8),
    sombrero_color('ocre'),
    sombrero_superficie('seca'),
    himenio_color('blanquecino'),
    laminas_tipo('apretadas'),
    pie_anillo('si'),
    pie_color('pardo'),
    pie_tipo('proporcional'),
    assertz(salida(habitat,'Crece en otoño formando pequeños grupos parasitando la madera de caducifolios.')),
    assertz(salida(comestibilidad,'Es comestible en estado joven, conviene tirar el agua de cocinarla para evitar su amargor, cruda puede causar trastornos digestivos.')).

%% Boletales %%
seta('Boletus aerus'):-
    familia('Boletaceae'),
    sombrero_tamano(10,20),
    sombrero_color('pardo oscuro'),
    sombrero_superficie('aterciopelada'),
    himenio_color('blanquecino'),
    pie_color('ocre'),
    assertz(salida(habitat,'Es una especie que sale en árboles de hoja caduca, como por ejemplo castaño, roble o haya, además de en encinares y alcornocales. Es bastante termófila, por lo que gusta de salir en los meses estivales o en principio del otoño. Adaptada al clima mediterráneo, es abundante en algunas regiones.')),
    assertz(salida(comestibilidad,'Es un comestible excelente, una de las especies más codiciadas por los buscadores de setas.')).

seta('Boletus lupinus'):-
    familia('Boletaceae'),
    sombrero_tamano(3,15),
    sombrero_color('rosa claro'),
    sombrero_superficie('aterciopelada'),
    himenio_color('anaranjado'),
    pie_color('amarillento'),
    assertz(salida(habitat,'Esta seta se la puede encontrar desde finales de primavera hasta el otoño, casi siempre ligada a bosques de caducifolios.')),
    assertz(salida(comestibilidad,'A pesar de no ser popular por el color rojo de los poros e intenso azuleamiento de la carne, de joven y bien cocinado, resulta excelente.')).

seta('Boletus queletii'):-
    familia('Boletaceae'),
    sombrero_tamano(6,12),
    (
        sombrero_color('anaranjado');
        sombrero_color('pardo rojizo')
    ),
    sombrero_superficie('seca'),
    himenio_color('amarillento'),
    pie_color('amarillento'),
    assertz(salida(habitat,'Fructifica en verano y sobre todo en otoño, más habitual en bosques de caducifolios, la encontramos tanto en hayedos como en robledales. Es una especie relativamente frecuente.')),
    assertz(salida(comestibilidad,'Comestible, aunque carece del aroma de los Boletus del grupo edulis.')).

seta('Hygrophoropsis pallida'):-
    orden('Boletales'),
    (
        sombrero_forma('convexo');
        sombrero_forma('plano')
    ),
    sombrero_tamano(1,5), %NOTE: 1.5 - 5
    sombrero_color('ocre'),
    sombrero_superficie('aterciopelada'),
    himenio_tipo('laminado'),
    himenio_color('blanquecino'),
    laminas_tipo('bifurcadas'),
    pie_anillo('no'),
    pie_color('amarillento'),
    pie_tipo('fino'),
    assertz(salida(habitat,'Aparece al menos en Europa, aunque se desconoce su distribución completa. Es una especie poco común que crece en bosques y praderas arboladas, sobre suelos ricos en restos vegetales.')),
    assertz(salida(comestibilidad,'Hygrophoropsis pallida es una especie raramente registrada cuya comestibilidad desconocemos.')).

seta('Chroogomphus fulmineus'):-
    orden('Boletales'),
    sombrero_forma('convexo'),
    sombrero_tamano(4,8),
    sombrero_color('pardo rojizo'),
    sombrero_superficie('lisa'),
    himenio_tipo('laminado'),
    himenio_color('pardo rojizo'),
    laminas_tipo('separadas'),
    pie_anillo('no'),
    pie_color('pardo rojizo'),
    pie_tipo('proporcional'),
    assertz(salida(habitat,'Esta seta mediterránea parece en otoño e invierno solitariamente o en grupos, generalmente ligado al árbol Pinus pinaster.')),
    assertz(salida(comestibilidad,'Comestible. Sin olor significativo; sabor dulce pero no distintivo.')).

setas('Suillus luteus'):-
    orden('Boletales'),
    sombrero_forma('convexo'),
    sombrero_tamano(4,12),
    sombrero_color('pardo oscuro'),
    sombrero_superficie('viscosa'),
    himenio_tipo('poroso'),
    himenio_color('amarillento'),
    pie_anillo('no'),
    pie_color('amarillento'),
    pie_tipo('proporcional'),
    assertz(salida(habitat,'Es nativa de las zonas templadas y frías de Europa y Asia, pero ha sido introducido en todo el mundo. Vive en simbiosis con las raíces de algunas especies de pino (género Pinus). Puede ser muy común en su hábitat.')),
    assertz(salida(comestibilidad,'Es una especie comestible si se elimina la cutícula, que es laxante, pero no es una seta valorada.')).

%% Auriculariales %%
seta('Auricularia auricula-judae'):-
    orden('Auriculariales'),
    carpoforo_forma('oreja'),
    carpoforo_color('pardo oscuro'),
    himenio_color('pardo oscuro'),
    assertz(salida(habitat,'Es una seta que puede aparecer en cualquier época del año, incluso en invierno, y lo hace siempre sobre tocones o troncos abatidos de árboles planifolios.')),
    assertz(salida(comestibilidad,'Comestible. A pesar de su poco agraciado aspecto resulta que es una seta comestible.')).

seta('Auricularia mesenterica'):-
    orden('Auriculariales'),
    carpoforo_forma('semicircular'),
    carpoforo_color('marron rojizo'),
    himenio_color('marron rojizo'),
    assertz(salida(habitat,'Frecuente, crece en lugares húmedos sobre madera caída de diferentes frondosas especialmente de olmo (Ulmus sp) y álamo (Populus alba).')),
    assertz(salida(comestibilidad,'Comestible sin interés y gastronómicamente inferior a la “oreja de Judas”.')).

%% Polyporales %%
seta('Cerrena unicolor'):-
    orden('Polyporales'),
    carpoforo_forma('semicircular'),
    carpoforo_color('pardo gris'),
    carpoforo_superficie('aterciopelada'),
    himenio_color('blanquecino'),
    assertz(salida(habitat,'Se ha encontrado al menos en el Hemisferio Norte. Crece sobre troncos muertos, generalmente de planifolios. Los cuerpos fructíferos son anuales y pueden aparecer en cualquier época del año.')),
    assertz(salida(comestibilidad,'Es demasiado fibroso y coriáceo para ser comestible. Además debido a que se suele encuentra en troncos muertos y tiene relaciones simbióticas con las avispas puede presentar parásitos o contaminaciones no deseadas. Es recomendable no consumirlo.')).

seta('Pycnoporus cinnabarinus'):-
    orden('Polyporales'),
    carpoforo_forma('semicircular'),
    carpoforo_color('rojo cinabrio'),
    carpoforo_superficie('rugoso'),
    himenio_color('rojo cinabrio'),
    assertz(salida(habitat,'Aparece por todo el Hemisferio Norte. Fructifica sobre madera muerta con preferencia por árboles de hoja caduca como los géneros Fagus o Quercus. Puede aparecer en cualquier época del año siempre y cuando haya humedad.')),
    assertz(salida(comestibilidad,'Su carne, fibrosa con humedad y leñosa en seco, es mal comestible.')).
    
seta('Fomes fomentarius'):-
    orden('Polyporales'),
    carpoforo_forma('pezuna'),
    carpoforo_color('grisaceo'),
    carpoforo_superficie('seca'),
    himenio_color('gris claro'),
    assertz(salida(habitat,'Un hongo que suele parasitar abedules (Betula sp) o hayas (Fagus sp) y que puede econtrarse tanto en Eurásia como Norteamérica. Puede vivir tanto en árboles vivos, comportándose como parásito, como en estos mismos árboles tras morir, pasando a una vida saprofítica.')),
    assertz(salida(comestibilidad,'La seta tiene una textura muy dura y leñosa, lo que la hace desagradable al paladar y difícil de digerir.')).

seta('Formitopsis pinicola'):-
    orden('Polyporales'),
    carpoforo_forma('semicircular'),
    carpoforo_color('pardo rojizo'),
    carpoforo_superficie('resinosa'),
    himenio_color('blanquecino'),
    assertz(salida(habitat,'Se ha encontrado por todo el Hemisferio Norte, creciendo sobre troncos de coníferas o planifolios, tanto en arboles vivos como muertos. Cuando crece sobre árboles vivos se comporta como parásito, pudiendo llegar a matarlos.')),
    assertz(salida(comestibilidad,'No es comestible por su sabor y consistencia dura y fibrosa.')).

% NOTE: Trametes hirsuta y Trametes versicolor son muy parecidos
% Pero a la familia que pertenecen engloba a mas setas de este programa
% Que no comparten las mismas caracteristicas
seta('Trametes hirsuta'):-
    orden('Polyporales'),
    carpoforo_forma('semicircular'),
    carpoforo_color('pardo gris'),
    carpoforo_superficie('aterciopelada'),
    himenio_color('pardo gris'),
    assertz(salida(habitat,'Es una especie de distribución mundial, especialmente en climas templados. Aparece en cualquier época del año sobre madera en descomposición, especialmente no de coníferas.')),
    assertz(salida(comestibilidad,'Es demasiado dura y correosa para ser comestible.')).

seta('Trametes versicolor'):-
    orden('Polyporales'),
    carpoforo_forma('semicircular'),
    carpoforo_color('circulo concentrico pardos y blanquecinos'),
    carpoforo_superficie('aterciopelada'),
    himenio_color('gris claro'),
    assertz(salida(habitat,'Es una especie que fructifica sobre madera de árboles planifolios, coníferas, e incluso sobre algunos frutales, provocando en el árbol una podredumbre blanca. Es un hongo muy frecuente y extendido que puede hacer acto de aparición en cualquier época del año si las condiciones ambientales son adecuadas.')),
    assertz(salida(comestibilidad,'No comestible, es dura y correosa por lo que resulta desagradable al paladar y difícil de digerir.')).

%% Thelephorales %%
seta('Hydnellum ferrugineum'):-
    orden('Thelephorales'),
    sombrero_tamano(5,10),
    sombrero_color('blanquecino'),
    sombrero_superficie('aterciopelada'),
    himenio_tipo('aguijones'),
    himenio_color('blanquecino'),
    pie_color('blanquecino'),
    pie_tipo('proporcional'),
    assertz(salida(habitat,'Se trata de una especie propia de los pinares, aunque no descartamos su presencia bajo otras coníferas. Hace muchos años era una especie que se veía con más frecuencia, pero pensamos que se encuentra en recesión. Es fundamentalmente otoñal.')),
    assertz(salida(comestibilidad,'Como casi todos los yesqueros poliporiáceos, su carne tiene consistencia coriácea, por lo que carece de interés culinario.')).

seta('Thelephora terrestris'):-
    orden('Thelephorales'),
    sombrero_tamano(2,4),
    sombrero_color('pardo oscuro'),
    (
        sombrero_superficie('aterciopelada');
        sombrero_superficie('seca')
    ),
    himenio_tipo('plegado'),
    himenio_color('pardo oscuro'),
    pie_color('pardo oscuro'),
    pie_tipo('proporcional'),
    assertz(salida(habitat,'Aparece al menos en Europa y las zonas cercanas. Habita zonas boscosas o incluso zonas ajardinadas.')),
    assertz(salida(comestibilidad,'Es una especie no comestible. Vive en simbiosis principalmente con coníferas, pero también en otras especies de plantas con flor, como Eucalyptus.')).

%% Cantharellales %%
seta('Cantharellus cibarius'):-
    orden('Cantharellales'),
    sombrero_tamano(1,12),
    sombrero_color('amarillento'),
    sombrero_superficie('lisa'),
    himenio_tipo('plegado'),
    himenio_color('amarillento'),
    pie_color('amarillento'),
    pie_tipo('grueso'),
    assertz(salida(habitat,'Habita en bosques variados e incluso zonas de matorral. Tiene una distribución prácticamente mundial.')),
    assertz(salida(comestibilidad,'Es una especie comestible, que suele fructificar desde finales de primavera hasta finales de otoño.')).

seta('Cantharellus cinereus'):-
    orden('Cantharellales'),
    sombrero_tamano(3,5),
    sombrero_color('negruzco'),
    sombrero_superficie('aterciopelada'),
    himenio_tipo('plegado'),
    himenio_color('pardo gris'),
    pie_color('negruzco'),
    pie_tipo('fino'),
    assertz(salida(habitat,'La localizamos durante el otoño bajo árboles planifolios, sobre todo bajo Fagus sylvatica, curiosamente en los mismos lugares donde fructifica el Craterellus cornucopioides, al igual que este sale en placas, si bien menos numerosas y copiosas.')),
    assertz(salida(comestibilidad,'Es un buen comestible, menos apreciado que el Craterellus cornucopioides, con el cual se confunde a menudo, que tiene un color más negruzco y cuyo himenio es más liso, sin pliegues tan definidos como esta seta.')).

seta('Craterellus cornucopioides'):-
    orden('Cantharellales'),
    sombrero_tamano(4,10),
    sombrero_color('pardo gris'),
    sombrero_superficie('escamada'),
    himenio_tipo('liso'),
    himenio_color('pardo gris'),
    pie_color('grisaceo'),
    pie_tipo('grueso'),
    assertz(salida(habitat,'La recolectamos en bosque de robles y hayas, donde aparece sobre todo en los meses otoñales, en placas de numerosos ejemplares. Le gustan los terrenos muy húmedos.')),
    assertz(salida(comestibilidad,'Excelente comestible a pesar de su aspecto, ideal para el acompañamiento como guarnición de todo tipo de guisos.')).

seta('Craterellus tubaeformis'):-
    orden('Cantharellales'),
    sombrero_tamano(2,6),
    sombrero_color('ocre'),
    sombrero_superficie('seca'),
    himenio_tipo('plegado'),
    himenio_color('gris claro'),
    pie_color('amarillento'),
    pie_tipo('fino'),
    assertz(salida(habitat,'La recolectamos en bosque de robles y hayas, donde aparece sobre todo en los meses otoñales, en placas de numerosos ejemplares. Le gustan los terrenos muy húmedos.')),
    assertz(salida(comestibilidad,'Excelente comestible a pesar de su aspecto, ideal para el acompañamiento como guarnición de todo tipo de guisos.')).