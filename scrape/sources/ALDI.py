# ALDI specific code
module_name = "ALDI"
name = "ALDI_Nord"

def urls():
	urls_list = (
	'https://www.aldi-nord.de/produkte/neu-im-sortiment.html',
	'https://www.aldi-nord.de/produkte/preissenkung.html',
	'https://www.aldi-nord.de/produkte/winter-sortiment.html',
	'https://www.aldi-nord.de/produkte/gourmet.html',
	'https://www.aldi-nord.de/produkte/schneekoppe.html',
	'https://www.aldi-nord.de/produkte/der-koenig-der-loewen.html',
	'https://www.aldi-nord.de/produkte/editions-weine.html',
	'https://www.aldi-nord.de/produkte/ausgezeichnete-qualitaet/sonstiges.html',
	'https://www.aldi-nord.de/produkte/ausgezeichnete-qualitaet/kosmetik.html',
	'https://www.aldi-nord.de/produkte/ausgezeichnete-qualitaet/lebensmittel.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/alkoholfreie-getraenke/eistee-energy-drinks.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/alkoholfreie-getraenke/limonaden-schorlen.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/alkoholfreie-getraenke/saefte-nektare.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/alkoholfreie-getraenke/wasser.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/alkoholische-getraenke/bier.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/alkoholische-getraenke/wein.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/alkoholische-getraenke/sekt-weinhaltigegetraenke.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/alkoholische-getraenke/likoere.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/alkoholische-getraenke/spirituosen.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/babyprodukte.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/back-kochzutaten/backhelfer-aromen.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/back-kochzutaten/dips-saucen-dressing.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/back-kochzutaten/eier.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/back-kochzutaten/fette-oele-essige.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/back-kochzutaten/gewuerze-kraeuter-fix-produkte.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/back-kochzutaten/mehl-zucker.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/back-kochzutaten/nuesse-kerne-samen.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/backwaren/brot-broetchen-croissants.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/backwaren/kuchen-gebaeck-kekse.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/blumen.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/brotaufstrich.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/eis.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fertiggerichte/antipasti-feinkost.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fertiggerichte/obst-gemuese.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fertiggerichte/kartoffelprodukte.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fertiggerichte/nachspeisen.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fertiggerichte/pfannengerichte-mikrowellengerichte.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fertiggerichte/pizza-pasta.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fertiggerichte/salat.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fertiggerichte/suppen-eintoepfe.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fertiggerichte/to-go.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fisch-meeresfruechte.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fleisch-wurst/gefluegel.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fleisch-wurst/gemischtes-fleisch.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fleisch-wurst/lamm.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fleisch-wurst/rind.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fleisch-wurst/schwein.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/fleisch-wurst/wurst-aufschnitt.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/guthabenkarten-geschenkkarten.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/haushalt/batterien-akkus-feuerzeuge.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/haushalt/folien-beutel-tueten.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/haushalt/reinigungsprodukte.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/haushalt/papierprodukte.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/haushalt/tragetaschen.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/haushalt/waschmittel-weichspueler.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/kaffee-tee-kakao/kaffee.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/kaffee-tee-kakao/tee-und-kakao.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/konserven.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/kosmetik-pflege/damenhygieneartikel.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/kosmetik-pflege/gesichtspflege.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/kosmetik-pflege/haarpflege-styling.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/kosmetik-pflege/koerperpflege.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/kosmetik-pflege/make-up.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/kosmetik-pflege/nahrungsergaenzung-sportnahrung.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/kosmetik-pflege/papierprodukte.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/kosmetik-pflege/zahnpflege.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/milchprodukte-kaese/joghurt-quark-desserts.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/milchprodukte-kaese/kaese.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/milchprodukte-kaese/milch-milchersatz.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/milchprodukte-kaese/butter-sahne-sauerrahm.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/muesli-cornflakes-cerealien.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/nudeln-reis.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/snacks-suessigkeiten/bonbons-kaugummi.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/snacks-suessigkeiten/fruchtgummi.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/snacks-suessigkeiten/nuesse-trockenfruechte.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/snacks-suessigkeiten/salziges-gebaeck.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/snacks-suessigkeiten/schokolade.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/snacks-suessigkeiten/suesses-gebaeck.html',
	'https://www.aldi-nord.de/produkte/aus-unserem-sortiment/tiernahrung.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/biscotto.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/chateau.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/confifrucht-marmelinchen.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/confifrucht-marmelinchen.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/conradl.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/eskimo.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/fair.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/feurich.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/fishfinesse.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/fjoerdens.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/gletscherkrone.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/goldaehren.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/golden-seafood.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/gourmet-fruits-de-mer.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/gut-bio.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/gut-drei-eichen.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/gueldenhof.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/hofburger.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/jacks-farm.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/landbeck.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/mama-mancini.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/mamia.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/markus.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/meierkamp.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/mein-bestes.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/milsa.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/milsani.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/moreno.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/moser-roth.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/mucci.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/nordholmer.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/nusskati.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/ofterdinger.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/pottkieker.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/proformance.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/pure-fruit.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/quellbrunn.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/river.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/rolffes.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/rookhus.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/satessa.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/schovit.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/soelde.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/sonniger.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/sontner.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/tamara.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/tandil.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/ursi.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/wellissa.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/wiesgart.html',
	'https://www.aldi-nord.de/produkte/unsere-marken/westminster.html',
	'https://www.aldi-nord.de/produkte/marken-aus-unserem-sortiment.html',
	'https://www.aldi-nord.de/produkte/veganes-entdecken.html',
	'https://www.aldi-nord.de/produkte/multimedia.html',
	'https://www.aldi-nord.de/produkte/zucker-und-salzreduktion.html',
	'https://www.aldi-nord.de/aldi-liefert/',
	'https://www.aldi-blumen.de/blumen-online-bestellen' )
	for url in urls_list:
		yield url

def process_url(url):
	# add ALDI root url
	return 'https://www.aldi-nord.de/' + url