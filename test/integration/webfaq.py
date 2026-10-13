import math
import re
import unittest

import ir_datasets
from ir_datasets.datasets.webfaq import LANGS, QREL_DEFS
from ir_datasets.formats import GenericDoc, GenericQuery, GenericScoredDoc, TrecQrel

from .base import DatasetIntegrationTest


class TestWebFaq(DatasetIntegrationTest):
    def test_docs(self):
        self._test_docs('webfaq/ara', count=141089, items={
            0: GenericDoc('0', 'التحميد متوفر لفترة مستقبلة تبدا من تاريخ ارسال الطلب ولا يمكن ايقاف او تجميد الاشتراك عن فترات سابقة'),
            9: GenericDoc('9', re.compile(r'^في العادة لا يكون هنالك سبب خطير وراء هذه الشكوى اذا لم تكن مصاحبة باعراض اخرى\nفي اغلب الاحيان يكون .{188}ن المهم متابعة الاعراض اذا لم تتحسن يرجى مراجعة الطبيب اخصائي الاعصاب للخضوع لفحص سريري لتحديد السبب$', flags=48)),
            62098: GenericDoc('62689', re.compile(r'^خروج البول من المهبل قد يدل على وجود ناسور شرجي مهبلي، ولا بد من الفحص الطبي للتأكد من الموضوع، أما .{331}ة لاجراء الفحوصات الهرمونية اللازمة وكذلك فحص بجهاز الموجات الفوق صوتية للرحم والمبايض لتشخيص حالتك\.$', flags=48)),
            141088: GenericDoc('142663', 'عند السفر من براغ ، ستستخدم أحد المطارات التالية: روزين المطار. ستصل إلى هذه المطارات: الملك عبد العزيز العالمية المطار.'),
        })
        self._test_docs('webfaq/dan', count=136939, items={
            0: GenericDoc('0', re.compile(r'^Når du skal vælge en lægtehammer, er der flere faktorer, du bør overveje\. For det første er vægten a.{433} lægtehammer af høj kvalitet og holdbarhed, så den kan modstå gentagen brug og have en lang levetid\.$', flags=48)),
            9: GenericDoc('9', 'Det mest passende tidspunkt at besøge Ramnagar og reservere et hotel er fra november til juni, hvor vejret er behageligt.'),
            136938: GenericDoc('137685', re.compile(r'^Når du har søgt efter hoteller på KAYAK, kan du finjustere din søgning efter nabolag, så du kan vælg.{106}mt beliggenhed, f\.eks\. centrum af Amritsar Besøg vores Amritsar\-side for at finde de seneste tilbud!$', flags=48)),
        })
        self._test_docs('webfaq/deu', count=886794, items={
            0: GenericDoc('0', 'Nur möglich, bei kundeneigenen Fritzboxen! Ansonsten stellt der Kabelnetzbetreiber die Updates zur Verfügung.'),
            9: GenericDoc('9', re.compile('^Nachdem du deine Rechnung in Excel erstellt hast, kannst du sie ganz einfach als PDF speichern\\. Gehe.{191}chern“\\.\nDas PDF\\-Format sorgt dafür, dass deine Rechnung unveränderbar ist und professioneller wirkt\\.$', flags=48)),
            886793: GenericDoc('891200', re.compile('^Je schwerer du bist, desto härter sollte deine Matratze sein\\. Leichtgewichte unter 60 kg brauchen H1.{90} H3 \\(mittelfest\\-fest\\) besser\\. Für 110 kg und mehr ist H4 empfehlenswert\\. Ab 150 kg ist H5 am besten\\.$', flags=48)),
        })
        self._test_docs('webfaq/eng', count=5252530, items={
            0: GenericDoc('0', re.compile('^Fire Risk Management System and its elements A fire safety risk management system should include the.{682}ndependent Fire Risk Assessment Consultant, we help organisations to manage their fire safety risks\\.$', flags=48)),
            9: GenericDoc('9', re.compile("^While the content creation, our writers don't charge per word but give a collective quote to the cli.{6}bout the project\\. Therefore, it eases our clients to manage the budget for content writing services\\.$", flags=48)),
            5252529: GenericDoc('5278724', re.compile("^Supervisor roles come with a lot of responsibility, so it's a good idea to keep that fact in mind wh.{106}phy and the leadership strategies you would implement to make a team more profitable and productive\\.$", flags=48)),
        })
        self._test_docs('webfaq/fas', count=226446, items={
            0: GenericDoc('0', 'خیر. درمان فیستول حتما به جراحی لیزر نیاز دارد. در صورت عدم درمان برای مدت طولانی، احتمال ابتلا به سرطان در مجرای فیستول وجود دارد.'),
            9: GenericDoc('9', re.compile('^علت زود سفید شدن موهاغم و غصه …ترس ، هیجانات زیاد… غلبه مزاج سرد و…غذاهای طبع سرد ، اعم از سرد و تر .{136} ترشی بیش از حد خوردن ، عدس و \\.\\.\\.و بوهای سرد مثل مواد ضدعفونی کننده ها ، بوی الکل و مواد شیمیایی و …$', flags=48)),
            226445: GenericDoc('226939', re.compile('^در خصوص \u200cاحساس درد بیضه پس از عمل واریکوسل به ویژه درد بیضه چپ، باید گفت که این موضوع ناشی از گشاد ش.{44}الای آن ها، در طی عمل می باشد\\. این اتفاق، تورم بیضه را به همراه می آورد که\u200c عامل اصلی احساس درد است\\.$', flags=48)),
        })
        self._test_docs('webfaq/fra', count=565142, items={
            0: GenericDoc('0', 'Oui, le WiFi est disponible au 25hours Hotel Terminus Nord.'),
            9: GenericDoc('9', re.compile('^Non, la clause qui impose le mode de paiement du loyer par prélèvement automatique est interdite \\(ar.{23}juillet 1989\\)\\.\xa0 Cependant, il a été jugé comme licite, la clause prévoyant le paiement par virement\\.$', flags=48)),
            565141: GenericDoc('569504', re.compile("^Leur valeur varie selon quelques principes qu'il faut connaître et considérer : la date d'ouverture\\..{75}n perspective, la plupart des pops sorties en 2011 tournent désormais autour d'une centaine d'euros\\.$", flags=48)),
        })
        self._test_docs('webfaq/hin', count=99897, items={
            0: GenericDoc('0', 'पेटीएम फर्स्ट कार्ड क्रेडिट कार्ड है जो कि पेटीएम ग्राहकों के लिए बनाया गया है। इस कार्ड का इस्तेमाल आप भारत सहित विदेशों में शॉपिंग के लिए कर सकते हो।'),
            9: GenericDoc('9', 'राजस्थान अध्यापक पात्रता परीक्षा 2024 का आयोजन माध्यमिक शिक्षा बोर्ड , अजमेर द्वारा करवाया जाएगा।'),
            99896: GenericDoc('100030', re.compile('^नहीं, ऐसा इसलिए है क्योंकि YeetDL आपको वीडियो और ऑडियो फॉर्मेट में वीडियो डाउनलोड करने का विकल्प देत.{23}णवत्ता भी चुन सकते हैं। अपनी प्राथमिकताएं बनाने के बाद, डाउनलोड बटन दबाएं, और डाउनलोड शुरू हो जाएगा।$', flags=48)),
        })
        self._test_docs('webfaq/ind', count=109774, items={
            0: GenericDoc('0', re.compile('^Akses offline bisa diaktifkan di setelan Dokumen, Spreadsheet, atau Slide\\. File lainnya juga bisa di.{4}s secara offline jika kamu mengaktifkan akses offline untuk Dokumen, Spreadsheet, Slide, atau Drive\\.$', flags=48)),
            9: GenericDoc('9', re.compile('^Pilih Pgsoft slot untuk menerima kesan terbaik dalam perjudian slot online, Kami akan senantiasa loy.{382}jam, promosi terbesar, mutu game terbaik, cara transaksi terlengkap, fitur game terkini dan terbaru\\.$', flags=48)),
            109773: GenericDoc('111314', re.compile('^Kami adalah ahli dalam pemrograman, reprogram, dan pemecahan masalah sistem kunci keyless\\. Dengan pe.{27}latan yang tepat, kami dapat memastikan kunci keyless Anda berfungsi dengan sempurna, tanpa masalah\\.$', flags=48)),
        })
        self._test_docs('webfaq/ita', count=255534, items={
            0: GenericDoc('0', 'Usa lo shampoo con la stessa frequenza del siero, 3 volte a settimana. Lo shampoo dura circa 3 mesi.'),
            9: GenericDoc('9', 'Sì, The Tennessean Personal Luxury Hotel accetta gli animali domestici. Trova subito le ultime tariffe su KAYAK!'),
            255533: GenericDoc('257802', 'I liberi professionisti stanno sfruttando il ribasso dei prezzi per acquistare gli uffici in cui lavorare. Negli ultimi 10 anni è stato registrato un calo del 36,6% per gli immobili nuovi.'),
        })
        self._test_docs('webfaq/jpn', count=307368, items={
            0: GenericDoc('0', '=演算子とissubset()メソッドは、どちらも集合の部分集合を確認するために使用されますが、使い方に違いがあります。 <=演算子は、2つの集合を比較して、左側の集合が右側の集合の部分集合であるかどうかを返します。 一方、issubset()メソッドは、呼び出し元の集合が引数として渡された集合の部分集合であるかどうかを確認します。 機能的には同じ結果を得られますが、表現方法が異なります。'),
            9: GenericDoc('9', '買取すること自体は可能です。しかしアフターダイヤになりますとカルティエ製品としての買取ではなくなります。買取価格は地金+ダイヤの査定となります。'),
            307367: GenericDoc('309156', re.compile('^2016年1月以降、個人番号（マイナンバー）制度導入に伴う所得税法等の改正により、「金地金・プラチナ地金・金貨・プラチナ貨」をご売却されたお客様への支払金額が200万円を超えた場合、事業者が税務署に提.{281}・金貨・プラチナ貨」と判断した場合は支払調書を提出することがございます。あらかじめご了承ください。 該当されますお客様には、マイナンバーのご提示方法など詳しい情報をあらためて書面にてご案内いたします。$', flags=48)),
        })
        self._test_docs('webfaq/kor', count=101036, items={
            0: GenericDoc('0', '답변. 부산 동래구 안락동 일자리센터 홈페이지에 접속하신 후,모집 정보를 검색하실 수 있습니다. 원하시는 카테고리를 선택하여 원하는 일자리를 찾고,신청 방법을 확인한 뒤 지원하시면 됩니다.'),
            9: GenericDoc('9', '1) 10% 이상 돈을 올리는 BJ 홀덤 방법\n2) 100% BJ 홀덤 OK!\n3) 7/24 BJ, PUBG, FPS OK!\n4) ATM, PC OK!'),
            101035: GenericDoc('101999', '팀의 공식 웹 사이트 나 경기장에서 경기장에서 갤럭시 플레이를 구입할 수있는 티켓.'),
        })
        self._test_docs('webfaq/nld', count=368382, items={
            0: GenericDoc('0', 'Een cirkelzaag is voornamelijk bedoeld voor het maken van rechte sneden in verschillende materialen, terwijl een decoupeerzaag meer geschikt is voor gedetailleerd en bochtig zaagwerk.'),
            9: GenericDoc('9', re.compile('^Altijd leuk om te weten is wie er verantwoordelijk is voor een cursus\\. Bovendien laat het zien of de.{436}cryptocurrencies\\. Dat heeft uiteindelijk geresulteerd in deze cursus\\. Klik hier voor meer informatie$', flags=48)),
            368381: GenericDoc('370661', re.compile('^Na het afronden van de betaling ontvang je van ons jouw digitale cadeaubon\\. De code van je giftcard .{29}m en je ontvangt van ons de code ook in je mailbox\\. Verzilver de code en je kunt direct aan de slag!$', flags=48)),
        })
        self._test_docs('webfaq/pol', count=191578, items={
            0: GenericDoc('0', re.compile('^Jeśli nie masz pewności co do nazw serwerów pocztowych, zapoznaj się z artykułem zatytułowanym Ustaw.{151}erwer wychodzący i zaznacz pole oznaczone jako Mój serwer wychodzący \\(SMTP\\) wymaga uwierzytelnienia\\.$', flags=48)),
            9: GenericDoc('9', re.compile('^Materiałem, z którego są wykonane pojemniki GN jest głównie wysokiej klasy stal nierdzewna\\. Obecnie .{323} odpornością na wysokie temperatury, dlatego może być wykorzystywany przy obróbce termicznej potraw\\.$', flags=48)),
            191577: GenericDoc('192514', re.compile('^Utarło się, że na basen najlepiej wybrać jednoczęściowy strój kąpielowy dla dziewczynki, bo zapewnia.{255}asenie\\. Tak naprawdę strój dobieraj do preferencji swojego dziecka, czyli tak, aby dobrze się czuło\\.$', flags=48)),
        })
        self._test_docs('webfaq/por', count=208209, items={
            0: GenericDoc('0', re.compile('^Para modificar uma reserva existente é necessário realizar uma nova reserva com os novos dados e apó.{319}em duplicidade, logo, reservamo\\-nos o direito de cancelar reservas em duplicidade, sem aviso prévio\\.$', flags=48)),
            9: GenericDoc('9', re.compile('^A cirurgia de estrabismo geralmente é realizada sob anestesia geral, portanto, o paciente não sentir.{20}edimento\\. No pós\\-operatório, pode haver algum desconforto, que pode ser controlado com medicamentos\\.$', flags=48)),
            208208: GenericDoc('209352', re.compile('^Ao alugar um veículo o locatário poderá optar por vários tipos de seguros opcionais \\(não obrigatório.{120}obertura pessoal; PAE\\- Seguro de pertences pessoais; RSP\\- Assistência ao Veículo Plus, entre outros\\.$', flags=48)),
        })
        self._test_docs('webfaq/rus', count=383269, items={
            0: GenericDoc('0', re.compile('^Правильный уход за склонной к прыщам кожей включает в себя ежедневное очищение, увлажнение и защиту .{133}сладкой пищи, регулярно менять подушечки на подушке, избегать стрессовых ситуаций и плохой экологии\\.$', flags=48)),
            9: GenericDoc('9', re.compile('^Если правила допускают выбор видео\\-слотов для отыгрыша бонусных фриспинов, отдайте предпочтение игро.{60}иями\\. Например, хорошо зарекомендовали себя Mega Joker, Big Bad Wolf, The Money Game, Blood Suckers\\.$', flags=48)),
            383268: GenericDoc('387503', 'В отдельных игровых аппаратах минимальная сумма спина – меньше одной гривны.'),
        })
        self._test_docs('webfaq/spa', count=600855, items={
            0: GenericDoc('0', re.compile('^No es ni legal ni ilegal, sino alegal\\. Al no disponer de licencia de la DGOJ, no puede ofrecer en pl.{289}n de tu dispositivo a través de tu cuenta de usuario Apple para poder ejecutar la app sin problemas\\.$', flags=48)),
            9: GenericDoc('9', 'No, sólo se puede reclamar la devolución de seguro de vida de prima única. Es decir, de aquellos seguros que se pagaron de una vez y en forma vinculada a la hipoteca'),
            600854: GenericDoc('604660', re.compile('^No\\. Puedes enviar la solicitud y recibir el préstamo sin hacerte cliente\\. Tendrás que inscribirte me.{165}uro\\. La opción de abrir una cuenta con EVOBANCO es una opción, ni más ni menos, pero no obligatoria\\.$', flags=48)),
        })
        self._test_docs('webfaq/swe', count=157849, items={
            0: GenericDoc('0', 'Du kan enkelt sätta insättningsgränser genom casinots avsnitt för ansvarsfullt spelande eller genom att kontakta kundtjänst.'),
            9: GenericDoc('9', 'Du kan kontakta Mister Spex via telefon på 08 - 55 00 25 60 eller via mejl på support@misterspex.se. Du kan även få svar på många frågor på Cubus hemsida.'),
            157848: GenericDoc('158737', 'Sestriere �r �ppet men inte f�r skid�kning. Ist�llet kan du hitta aktiviteter som mountainbike, vandring, golf och sk�rmflygning under l�gs�song.'),
        })
        self._test_docs('webfaq/tur', count=144115, items={
            0: GenericDoc('0', re.compile('^Sürekli klavyeye bakarsanız dokunmatik yazmayı öğrenemezsiniz\\. Klavyedeki sembollerin yerlerini hatı.{202}tamamlayın, tüm ödülleri kazanın ve birkaç hafta içinde farklı yazdığınızı bile hatırlamayacaksınız\\.$', flags=48)),
            9: GenericDoc('9', "Vippark casino alt yapısının sistemlerinden en kayda değeri Centurion oyununu sorgulayın. Aylarca müşterilerin 335.000 TL'den fazla kazanç sağladığı canlı oyunda vakit kaçırmadan rezerveni yap."),
            144114: GenericDoc('144845', re.compile('^Sileo, Cydia‘nın alternatifi olan modern bir paket yöneticisidir\\( aka jailbreak appstore \\)\\. Sileo uy.{66}n tüm 64 bit cihazlar için tam destek sunan yenilenip geliştirilen bir Kullanıcı Arayüzüne sahiptir\\.$', flags=48)),
        })
        self._test_docs('webfaq/vie', count=123283, items={
            0: GenericDoc('0', re.compile('^Facial Cream Kone có khả năng chống nắng, bảo vệ da khỏi tác hại của các loại tia UV\\.nnTuy nhiên như.{123}goài trong thời gian dài thì vẫn nên che chắn, dùng kem chống nắng để có thể bảo vệ da tốt nhất nhé\\.$', flags=48)),
            9: GenericDoc('9', re.compile('^Trên địa bàn H\\. Đồng Văn, trong bán kính 30km tính từ Khách sạn Mã Pì Lèng, có 10 khu du du lịch hấp.{167}g, Sông Nho Quế, Hẻm Tu Sản, Làng văn hoá du lịch cộng đồng Pả Vi, Dinh thự họ Vương, Cột cờ Lũng Cú$', flags=48)),
            123282: GenericDoc('123971', 'Giới hạn cắt lỗ là số tiền mà người đặt cược sẵn sàng thua khi đặt cược trong một khoảng thời gian nhất định. Giới hạn này giúp người chơi bảo toàn vốn cược một cách hiệu quả.'),
        })
        self._test_docs('webfaq/zho', count=131606, items={
            0: GenericDoc('0', '是的，你需要。想了解更多 Official Deed Polls ？或者只是不想錯過最新的 Official Deed Polls 促銷代碼信息、新產品和其他有關的新聞 Official Deed Polls ？來到 official-deedpolls.co.uk 並註冊成為會員 Official Deed Polls 通過提供您的電子郵件地址！'),
            9: GenericDoc('9', '前提：所创建的询盘为私有询盘，且对方未报价或者此询盘为草稿状态\\r \\r 1、登录账号后，点击“模块切换”按钮，选择“采购商模块”\\r \\r \\r \\r \\r \\r 2、点击左侧菜单栏“询盘管理”中的“我的询盘”按钮，选择还未收到报价的询盘进行删除'),
            131605: GenericDoc('132490', '资本项目交易是指改变居住在印度的人在印度以外的资产或负债，包括所有或有负债，或改变居住在印度以外的人在印度的资产或负债的交易。它还包括FEMA1999第6(3)节中指定的事务。'),
        })

    def test_queries(self):
        self._test_queries('webfaq/ara/train', count=132664, items={
            0: GenericQuery('135771', 'كم يكلف تصنيع تصميم غرفة النوم'),
            9: GenericQuery('75193', 'هل الصراحة أهم من الحب؟'),
            132663: GenericQuery('76952', 'هل يتواجد لشركة نجوم الخليج فروع أخرى غيرشركة عزل اسطح بالدمام؟'),
        })
        self._test_queries('webfaq/ara/test', count=10000, items={
            0: GenericQuery('14384', 'هل استئصال المراره بالجراحه المفتوحه افضل من المنظار فى حالة وجود فتق بالسره وسمنه\nالسن 60 سنه ؟'),
            9: GenericQuery('90565', 'هل تتوفر خدمة الواي فاي في الداماي؟'),
            9999: GenericQuery('30805', 'هل يحتوي Xbox One على تقنية Bluetooth؟'),
        })
        self._test_queries('webfaq/dan/train', count=127686, items={
            0: GenericQuery('68046', 'Hvad gør jeg hvis min ordre er blevet skadet under levering?'),
            9: GenericQuery('98530', 'Kan et mobilt klimaanl�g bruges p� arbejdspladsen?'),
            127685: GenericQuery('59265', 'Hvad sker der, hvis jeg ikke henter min pakke indenfor den angivne tid?'),
        })
        self._test_queries('webfaq/dan/test', count=10000, items={
            0: GenericQuery('26645', 'Hvordan er området omkring Penzion Pleso?'),
            9: GenericQuery('55051', 'Hvor kan jeg finde brugsbetingelserne for jeres hjemmeside?'),
            9999: GenericQuery('55188', 'Hvad skal jeg gøre, hvis jeg modtog en defekt/forkert/plettet vare?'),
        })
        self._test_queries('webfaq/deu/train', count=881201, items={
            0: GenericQuery('680119', 'Ist Grand Hyatt Istanbul haustierfreundlich?'),
            9: GenericQuery('451591', 'Ist Trustly eine gute alternative zu PayPal?'),
            881200: GenericQuery('56588', 'BEZAHLE ICH FÜR DIE BERATUNGSGEBÜHR?'),
        })
        self._test_queries('webfaq/deu/test', count=10000, items={
            0: GenericQuery('376317', 'Wo ist meine Austriansupermarket-Bestellung?'),
            9: GenericQuery('200913', 'WAS SIND DIE EMPFOHLENEN ZYKLEN FÜR DIE VERWENDUNG VON MODAFINIL UND ARMODAFINIL?'),
            9999: GenericQuery('622074', 'Wie bewahre ich Avocados auf?'),
        })
        self._test_queries('webfaq/eng/train', count=5268725, items={
            0: GenericQuery('945763', 'How do I turn on Walk Assist?'),
            9: GenericQuery('4216294', 'Remanence (br)'),
            5268724: GenericQuery('4914719', 'Is natto miso rich in vitamin K?'),
        })
        self._test_queries('webfaq/eng/test', count=10000, items={
            0: GenericQuery('4495885', 'How much does it cost to transport a bike?'),
            9: GenericQuery('991190', 'What is mobile patrol security?'),
            9999: GenericQuery('4978031', 'Is Tarsar Marsar trek safe?'),
        })
        self._test_queries('webfaq/fas/train', count=216940, items={
            0: GenericQuery('126328', 'نحوه استفاده از روغن\u200cها در طول روز برای لاغری'),
            9: GenericQuery('60158', 'درمان با لیزر کیوسوئیچ را هر چند وقت یک بار می\u200cتوان انجام داد؟'),
            216939: GenericQuery('112951', 'شما برای حمل بار از تهران به زاوه چه خودروهایی دارید؟'),
        })
        self._test_queries('webfaq/fas/test', count=10000, items={
            0: GenericQuery('138497', 'آیا کار با رزین اپوکسی E06 خوزستان نیاز به دمای خاصی دارد؟'),
            9: GenericQuery('81644', 'تفاوت کلاه ساحلی و شهرزادی چیست ؟'),
            9999: GenericQuery('212715', 'آیا محصولات فروشگاه من نیز می تواند در راشین کالا قرار بگیرد؟'),
        })
        self._test_queries('webfaq/fra/train', count=559505, items={
            0: GenericQuery('377159', 'Quel taux pour un crédit camping-car ?'),
            9: GenericQuery('455114', 'Bonjour, Si le matelas ne convient pas y a t il un remboursement?'),
            559504: GenericQuery('100147', 'Combien de temps faut-il pour transporter ma marchandise ?'),
        })
        self._test_queries('webfaq/fra/test', count=10000, items={
            0: GenericQuery('148200', 'Comment écrire de la non-fiction professionnellement?'),
            9: GenericQuery('455091', "Bonjour, serait t'il possible d'avoir le sommier en latte de bois? 160/200 merci"),
            9999: GenericQuery('555163', 'Comment prendrez-vous en compte nos spécificités de voyage ?'),
        })
        self._test_queries('webfaq/hin/train', count=90031, items={
            0: GenericQuery('4897', 'क्या yaarii द्वारा आपसे प्रोसेसिंग शुल्क लिया जाता है?'),
            9: GenericQuery('76923', '2019 में किस भारतीय शहर को यूनेस्को की विश्व धरोहर स्थल घोषित किया गया?'),
            90030: GenericQuery('92018', 'महतारी वंदन योजना की लिस्ट में नाम चेक करने के लिए कैसे आवेदन करें?'),
        })
        self._test_queries('webfaq/hin/test', count=10000, items={
            0: GenericQuery('71329', 'Mp3 डाउनलोड कैसे करे?'),
            9: GenericQuery('67026', 'योगी आदित्यनाथ जी कौन से पार्टी से है?'),
            9999: GenericQuery('82132', 'क्या हमें इसके लिए इंटरनेट कनेक्शन की आवश्यकता पड़ेगी?'),
        })
        self._test_queries('webfaq/ind/train', count=101315, items={
            0: GenericQuery('81057', 'Bagaimana cara cek resi Indah Cargo bekerja dan apa cara paling efektif untuk memeriksanya?'),
            9: GenericQuery('12759', 'Apakah Malaikat88 dapat diakses melalui perangkat mobile seperti smartphone atau tablet?'),
            101314: GenericQuery('69187', 'Berapa gaji di PT Pillar Utama Contrindo?'),
        })
        self._test_queries('webfaq/ind/test', count=10000, items={
            0: GenericQuery('69557', 'Berapa lama proses verifikasi berlangsung?'),
            9: GenericQuery('89219', 'Apakah waktu daftar keluar di Mi Amor?'),
            9999: GenericQuery('26728', 'Apa saja metode pembayaran yang tersedia di bidwin88?'),
        })
        self._test_queries('webfaq/ita/train', count=247803, items={
            0: GenericQuery('126095', 'Differenza nella guida della cintura/posizionamento di iZi Up e iZi Flex'),
            9: GenericQuery('39392', "C'è un modo per convertire Windows Media Player in MP3?"),
            247802: GenericQuery('30514', 'Melissa & Doug 14837 - Costume da Muratore è buono come Pagliaccetti per Bambino Ispirato a Goku Ragazze Ragazzi Pigiama Neonato Tutina Fumetto Outfits?'),
        })
        self._test_queries('webfaq/ita/test', count=10000, items={
            0: GenericQuery('68975', 'Quale è meglio eSituro Portabici Posteriore per Auto Supporto Bici Portapacchi Portabicicletta Pieghevole capacità Fino a 2 Bike Nero SBC0005 o il Thule 532 New Freeride - Portabici?'),
            9: GenericQuery('74336', 'Il Atlante del legno. Guida ai legnami del mondo è migliore di Enciclopedia delle tecniche di lavorazione del legno?'),
            9999: GenericQuery('9073', "La maglieria spessa è adatta solo per l'abbigliamento casual?"),
        })
        self._test_queries('webfaq/jpn/train', count=299157, items={
            0: GenericQuery('58635', '入出金明細にデビット出金取消があり、状況を知りたい。'),
            9: GenericQuery('7023', '送られてきた商品は送り返すのでしょうか？'),
            299156: GenericQuery('301987', 'XMのMT4/MT5が正常にダウンロード・インストールされません。'),
        })
        self._test_queries('webfaq/jpn/test', count=10000, items={
            0: GenericQuery('176528', '相手に有利な（自分に不利な）遺産分割協議書にサインするように求められています。どうしたらいいでしょうか。'),
            9: GenericQuery('289995', '出金にかかる手数料はありますか？'),
            9999: GenericQuery('252219', '解体業者の都合により工事が遅延した場合に損害賠償請求はできますか？'),
        })
        self._test_queries('webfaq/kor/train', count=92000, items={
            0: GenericQuery('74888', 'Threat Manager는 DNS 차단기와 비슷한가요?'),
            9: GenericQuery('80402', '도톤보리 호텔에서 무료 와이파이를 사용할 수 있나요?'),
            91999: GenericQuery('41942', '질문. 대구 중구 서성로1가의 직업소개소 방문 시 준비해야 할 서류는 어떤 것이 있나요?'),
        })
        self._test_queries('webfaq/kor/test', count=10000, items={
            0: GenericQuery('54216', '카지노 게임에는 어떤 종류의 보너스가 있나요?'),
            9: GenericQuery('45224', '고객 서비스 전화 번호는 무엇입니까? 클레오 카지노'),
            9999: GenericQuery('83244', '카드로 선불금을 결제하는 것이 안전한가요?'),
        })
        self._test_queries('webfaq/nld/train', count=360662, items={
            0: GenericQuery('278491', 'Wat moet er in een evaluatieformulier staan?'),
            9: GenericQuery('116039', 'Is DumboFab compatibel met Mac-computers?'),
            360661: GenericQuery('89716', 'Hoe kan ik een inklapbare werkbank bestellen?'),
        })
        self._test_queries('webfaq/nld/test', count=10000, items={
            0: GenericQuery('148145', 'Is er praktijkgericht leren tijdens de training?'),
            9: GenericQuery('252553', 'Hoelang gaat een gasveer mee?'),
            9999: GenericQuery('106730', 'Wordt de prijs alleen verloot onder de verkochte loten of is het ook mogelijk dat de prijs valt op een niet verkocht lot?'),
        })
        self._test_queries('webfaq/pol/train', count=182515, items={
            0: GenericQuery('94493', 'Jak odstąpić od pożyczki Smartney?'),
            9: GenericQuery('34097', 'Co się stanie z moimi pieniędzmi po zakończeniu lokaty?'),
            182514: GenericQuery('40033', 'Jak szybko mogę otrzymać wypłatę z CasinoMega?'),
        })
        self._test_queries('webfaq/pol/test', count=10000, items={
            0: GenericQuery('68227', 'Na jaką wersje jest SzalonaMasakra?'),
            9: GenericQuery('70469', 'Gdzie w sieci znaleźć Big Time Gaming kasyno?'),
            9999: GenericQuery('35233', 'Ile kosztuje pomoc dobrego kominiarza w Mońkach?'),
        })
        self._test_queries('webfaq/por/train', count=199353, items={
            0: GenericQuery('71034', 'Como falar com a Mais Capital Promotora?'),
            9: GenericQuery('153998', 'Consigo fazer assinaturas de serviço com o virtual?'),
            199352: GenericQuery('182013', 'Quando se celebra Abastur?'),
        })
        self._test_queries('webfaq/por/test', count=10000, items={
            0: GenericQuery('161083', 'Quanto custa ficar em Terras - Agroturismo & Vinhos, em Beja?'),
            9: GenericQuery('14811', 'Devo deixar minha VPN permanentemente ligada?'),
            9999: GenericQuery('90648', 'Onde posso usufruir de estacionamento grátis com a minha estadia em Porec?'),
        })
        self._test_queries('webfaq/rus/train', count=377504, items={
            0: GenericQuery('244224', 'В чем заключается работа сантехника?'),
            9: GenericQuery('25948', 'При каких видах кожных заболеваний помогает препарат?'),
            377503: GenericQuery('165884', 'От чего зависит цена на фальцесклейку?'),
        })
        self._test_queries('webfaq/rus/test', count=10000, items={
            0: GenericQuery('350487', 'Предусмотрена ли возможность досрочного погашения кредита?'),
            9: GenericQuery('115721', 'Могу ли я получить образцы нержавеющей стали 321?'),
            9999: GenericQuery('6559', 'Почему у меня не работает приложение Leon?'),
        })
        self._test_queries('webfaq/spa/train', count=594661, items={
            0: GenericQuery('391630', '¿Las clases se darán con las ventanas abiertas? Hay estudios que dicen que esto funciona.'),
            9: GenericQuery('360753', '¿Cuáles son los costos de renovación anual de un sitio web?'),
            594660: GenericQuery('423072', '¿Qué kit de primeros auxilios es el mejor?'),
        })
        self._test_queries('webfaq/spa/test', count=10000, items={
            0: GenericQuery('406554', '¿Qué hacer si el filtro de mi depuradora pierde agua?'),
            9: GenericQuery('530', '¿Cómo hacer un curriculum perfecto?'),
            9999: GenericQuery('175983', '¿Me podréis ayudar a transmitir mi mensaje de marca?'),
        })
        self._test_queries('webfaq/swe/train', count=148738, items={
            0: GenericQuery('151860', 'Vilka typer av digitalisering kan ett företag använda?'),
            9: GenericQuery('80179', 'Vilken typ av frågor kommer fluidens intelligens att inkludera?'),
            148737: GenericQuery('20850', 'När är halloween?'),
        })
        self._test_queries('webfaq/swe/test', count=10000, items={
            0: GenericQuery('844', 'Hur man använder 1win bonus för sport och kasino?'),
            9: GenericQuery('28820', 'Kan jag skicka min egen design för att anpassa Blyertspennor?'),
            9999: GenericQuery('59109', 'Finns det billigare alternativ till en helrenovering?'),
        })
        self._test_queries('webfaq/tur/train', count=134846, items={
            0: GenericQuery('1166', 'Betclub Android Uygulaması'),
            9: GenericQuery('140641', 'İp Askı Hangi Bölgelere Uygulanabilir?'),
            134845: GenericQuery('42242', 'Turnuvalar Ne Zaman Başlıyor?'),
        })
        self._test_queries('webfaq/tur/test', count=10000, items={
            0: GenericQuery('135758', 'Hotel Arma İletişim Numarası Nedir?'),
            9: GenericQuery('1842', 'Retrobet İddaa Sayfası Güvenilir Mi?'),
            9999: GenericQuery('45616', 'Kaç Otobüs Firmasına hizmet veriyorsunuz?'),
        })
        self._test_queries('webfaq/vie/train', count=113972, items={
            0: GenericQuery('52798', '(3) Ninja School Hack 9 server lậu chơi có khó hay không?'),
            9: GenericQuery('15648', 'Tại sao nên trang bị tư duy win win khi tán gái?'),
            113971: GenericQuery('4400', 'Tham gia casino trực tuyến, casino online tại nhà cái EU9 có uy tín không?'),
        })
        self._test_queries('webfaq/vie/test', count=10000, items={
            0: GenericQuery('83342', 'Tôi có thể sử dụng thẻ thanh toán tại Nha Trang?'),
            9: GenericQuery('102933', 'Bánh tiêu có đắt không?'),
            9999: GenericQuery('43651', 'Phiên bản Supreme Edition là gì? Đây có phải là một nền tảng giao dịch?'),
        })
        self._test_queries('webfaq/zho/train', count=122491, items={
            0: GenericQuery('120409', '如何在線使用Gap優惠券？'),
            9: GenericQuery('49541', '星仙草的香檸仙草凍有什麼特色？'),
            122490: GenericQuery('26356', '通過創業移民獲得EP身份後是否存在移民監？需要常年待在新加坡嗎？'),
        })
        self._test_queries('webfaq/zho/test', count=10000, items={
            0: GenericQuery('112503', '林夏薇喜歡的名鐘品牌Patek Philippe不是人人買到？'),
            9: GenericQuery('63839', '我可以为 Bose 航空耳机购买更换零件吗？'),
            9999: GenericQuery('75141', '入住羅克斯酒店需要多少錢？'),
        })

    def test_qrels(self):
        self._test_qrels('webfaq/ara/train', count=132664, items={
            0: TrecQrel('135771', '99651', 1, '0'),
            9: TrecQrel('75193', '108312', 1, '0'),
            132663: TrecQrel('76952', '111451', 1, '0'),
        })
        self._test_qrels('webfaq/ara/test', count=10000, items={
            0: TrecQrel('14384', '43102', 1, '0'),
            9: TrecQrel('90565', '85256', 1, '0'),
            9999: TrecQrel('30805', '122902', 1, '0'),
        })
        self._test_qrels('webfaq/dan/train', count=127686, items={
            0: TrecQrel('68046', '54718', 1, '0'),
            9: TrecQrel('98530', '102829', 1, '0'),
            127685: TrecQrel('59265', '67543', 1, '0'),
        })
        self._test_qrels('webfaq/dan/test', count=10000, items={
            0: TrecQrel('26645', '99403', 1, '0'),
            9: TrecQrel('55051', '105898', 1, '0'),
            9999: TrecQrel('55188', '40902', 1, '0'),
        })
        self._test_qrels('webfaq/deu/train', count=881201, items={
            0: TrecQrel('680119', '358547', 1, '0'),
            9: TrecQrel('451591', '2681', 1, '0'),
            881200: TrecQrel('56588', '821513', 1, '0'),
        })
        self._test_qrels('webfaq/deu/test', count=10000, items={
            0: TrecQrel('376317', '358666', 1, '0'),
            9: TrecQrel('200913', '756802', 1, '0'),
            9999: TrecQrel('622074', '666917', 1, '0'),
        })
        self._test_qrels('webfaq/eng/train', count=5268725, items={
            0: TrecQrel('945763', '4493741', 1, '0'),
            9: TrecQrel('4216294', '1226357', 1, '0'),
            5268724: TrecQrel('4914719', '1723502', 1, '0'),
        })
        self._test_qrels('webfaq/eng/test', count=10000, items={
            0: TrecQrel('4495885', '21829', 1, '0'),
            9: TrecQrel('991190', '2202441', 1, '0'),
            9999: TrecQrel('4978031', '1540215', 1, '0'),
        })
        self._test_qrels('webfaq/fas/train', count=216940, items={
            0: TrecQrel('126328', '9634', 1, '0'),
            9: TrecQrel('60158', '192075', 1, '0'),
            216939: TrecQrel('112951', '18244', 1, '0'),
        })
        self._test_qrels('webfaq/fas/test', count=10000, items={
            0: TrecQrel('138497', '178654', 1, '0'),
            9: TrecQrel('81644', '161715', 1, '0'),
            9999: TrecQrel('212715', '4527', 1, '0'),
        })
        self._test_qrels('webfaq/fra/train', count=559505, items={
            0: TrecQrel('377159', '72464', 1, '0'),
            9: TrecQrel('455114', '97708', 1, '0'),
            559504: TrecQrel('100147', '28465', 1, '0'),
        })
        self._test_qrels('webfaq/fra/test', count=10000, items={
            0: TrecQrel('148200', '82765', 1, '0'),
            9: TrecQrel('455091', '105098', 1, '0'),
            9999: TrecQrel('555163', '213712', 1, '0'),
        })
        self._test_qrels('webfaq/hin/train', count=90031, items={
            0: TrecQrel('4897', '53256', 1, '0'),
            9: TrecQrel('76923', '74488', 1, '0'),
            90030: TrecQrel('92018', '5183', 1, '0'),
        })
        self._test_qrels('webfaq/hin/test', count=10000, items={
            0: TrecQrel('71329', '62713', 1, '0'),
            9: TrecQrel('67026', '10886', 1, '0'),
            9999: TrecQrel('82132', '74658', 1, '0'),
        })
        self._test_qrels('webfaq/ind/train', count=101315, items={
            0: TrecQrel('81057', '19753', 1, '0'),
            9: TrecQrel('12759', '27686', 1, '0'),
            101314: TrecQrel('69187', '27667', 1, '0'),
        })
        self._test_qrels('webfaq/ind/test', count=10000, items={
            0: TrecQrel('69557', '48046', 1, '0'),
            9: TrecQrel('89219', '95021', 1, '0'),
            9999: TrecQrel('26728', '52705', 1, '0'),
        })
        self._test_qrels('webfaq/ita/train', count=247803, items={
            0: TrecQrel('126095', '79377', 1, '0'),
            9: TrecQrel('39392', '200987', 1, '0'),
            247802: TrecQrel('30514', '40357', 1, '0'),
        })
        self._test_qrels('webfaq/ita/test', count=10000, items={
            0: TrecQrel('68975', '77124', 1, '0'),
            9: TrecQrel('74336', '116281', 1, '0'),
            9999: TrecQrel('9073', '33041', 1, '0'),
        })
        self._test_qrels('webfaq/jpn/train', count=299157, items={
            0: TrecQrel('58635', '190062', 1, '0'),
            9: TrecQrel('7023', '261129', 1, '0'),
            299156: TrecQrel('301987', '300914', 1, '0'),
        })
        self._test_qrels('webfaq/jpn/test', count=10000, items={
            0: TrecQrel('176528', '128962', 1, '0'),
            9: TrecQrel('289995', '116734', 1, '0'),
            9999: TrecQrel('252219', '42227', 1, '0'),
        })
        self._test_qrels('webfaq/kor/train', count=92000, items={
            0: TrecQrel('74888', '37793', 1, '0'),
            9: TrecQrel('80402', '73685', 1, '0'),
            91999: TrecQrel('41942', '95106', 1, '0'),
        })
        self._test_qrels('webfaq/kor/test', count=10000, items={
            0: TrecQrel('54216', '82942', 1, '0'),
            9: TrecQrel('45224', '18666', 1, '0'),
            9999: TrecQrel('83244', '90416', 1, '0'),
        })
        self._test_qrels('webfaq/nld/train', count=360662, items={
            0: TrecQrel('278491', '329303', 1, '0'),
            9: TrecQrel('116039', '47079', 1, '0'),
            360661: TrecQrel('89716', '321337', 1, '0'),
        })
        self._test_qrels('webfaq/nld/test', count=10000, items={
            0: TrecQrel('148145', '204411', 1, '0'),
            9: TrecQrel('252553', '49921', 1, '0'),
            9999: TrecQrel('106730', '285622', 1, '0'),
        })
        self._test_qrels('webfaq/pol/train', count=182515, items={
            0: TrecQrel('94493', '125658', 1, '0'),
            9: TrecQrel('34097', '27883', 1, '0'),
            182514: TrecQrel('40033', '30936', 1, '0'),
        })
        self._test_qrels('webfaq/pol/test', count=10000, items={
            0: TrecQrel('68227', '104141', 1, '0'),
            9: TrecQrel('70469', '174413', 1, '0'),
            9999: TrecQrel('35233', '24331', 1, '0'),
        })
        self._test_qrels('webfaq/por/train', count=199353, items={
            0: TrecQrel('71034', '55468', 1, '0'),
            9: TrecQrel('153998', '59176', 1, '0'),
            199352: TrecQrel('182013', '45813', 1, '0'),
        })
        self._test_qrels('webfaq/por/test', count=10000, items={
            0: TrecQrel('161083', '144188', 1, '0'),
            9: TrecQrel('14811', '181697', 1, '0'),
            9999: TrecQrel('90648', '47310', 1, '0'),
        })
        self._test_qrels('webfaq/rus/train', count=377504, items={
            0: TrecQrel('244224', '222917', 1, '0'),
            9: TrecQrel('25948', '286497', 1, '0'),
            377503: TrecQrel('165884', '117860', 1, '0'),
        })
        self._test_qrels('webfaq/rus/test', count=10000, items={
            0: TrecQrel('350487', '194880', 1, '0'),
            9: TrecQrel('115721', '2122', 1, '0'),
            9999: TrecQrel('6559', '286536', 1, '0'),
        })
        self._test_qrels('webfaq/spa/train', count=594661, items={
            0: TrecQrel('391630', '154079', 1, '0'),
            9: TrecQrel('360753', '135805', 1, '0'),
            594660: TrecQrel('423072', '41606', 1, '0'),
        })
        self._test_qrels('webfaq/spa/test', count=10000, items={
            0: TrecQrel('406554', '344211', 1, '0'),
            9: TrecQrel('530', '438084', 1, '0'),
            9999: TrecQrel('175983', '305271', 1, '0'),
        })
        self._test_qrels('webfaq/swe/train', count=148738, items={
            0: TrecQrel('151860', '117730', 1, '0'),
            9: TrecQrel('80179', '99457', 1, '0'),
            148737: TrecQrel('20850', '1162', 1, '0'),
        })
        self._test_qrels('webfaq/swe/test', count=10000, items={
            0: TrecQrel('844', '99334', 1, '0'),
            9: TrecQrel('28820', '157709', 1, '0'),
            9999: TrecQrel('59109', '71253', 1, '0'),
        })
        self._test_qrels('webfaq/tur/train', count=134846, items={
            0: TrecQrel('1166', '53096', 1, '0'),
            9: TrecQrel('140641', '63267', 1, '0'),
            134845: TrecQrel('42242', '49474', 1, '0'),
        })
        self._test_qrels('webfaq/tur/test', count=10000, items={
            0: TrecQrel('135758', '98940', 1, '0'),
            9: TrecQrel('1842', '102773', 1, '0'),
            9999: TrecQrel('45616', '61963', 1, '0'),
        })
        self._test_qrels('webfaq/vie/train', count=113972, items={
            0: TrecQrel('52798', '113414', 1, '0'),
            9: TrecQrel('15648', '96892', 1, '0'),
            113971: TrecQrel('4400', '79414', 1, '0'),
        })
        self._test_qrels('webfaq/vie/test', count=10000, items={
            0: TrecQrel('83342', '55363', 1, '0'),
            9: TrecQrel('102933', '105434', 1, '0'),
            9999: TrecQrel('43651', '86948', 1, '0'),
        })
        self._test_qrels('webfaq/zho/train', count=122491, items={
            0: TrecQrel('120409', '18811', 1, '0'),
            9: TrecQrel('49541', '37092', 1, '0'),
            122490: TrecQrel('26356', '15157', 1, '0'),
        })
        self._test_qrels('webfaq/zho/test', count=10000, items={
            0: TrecQrel('112503', '62043', 1, '0'),
            9: TrecQrel('63839', '75207', 1, '0'),
            9999: TrecQrel('75141', '95457', 1, '0'),
        })

    def test_scoreddocs(self):
        self._test_webfaq_scoreddocs('ara', count=6336393, query_count=32000, items={
            0: GenericScoredDoc('60766', '108738', 0.99853515625),
            9: GenericScoredDoc('60766', '94981', 0.071044921875),
            6336392: GenericScoredDoc('7062', '98801', 1.5914440155029297e-05),
        })
        self._test_webfaq_scoreddocs('dan', count=6123062, query_count=32000, items={
            0: GenericScoredDoc('78410', '7331', 0.340576171875),
            9: GenericScoredDoc('78410', '38148', 0.004085540771484375),
            6123061: GenericScoredDoc('126557', '97913', 1.6033649444580078e-05),
        })
        self._test_webfaq_scoreddocs('deu', count=18702436, query_count=96000, items={
            0: GenericScoredDoc('655890', '666732', 0.828125),
            9: GenericScoredDoc('655890', '605649', 0.00284576416015625),
            18702435: GenericScoredDoc('87724', '623291', 1.621246337890625e-05),
        })
        self._test_webfaq_scoreddocs('eng', count=25632193, query_count=128000, items={
            0: GenericScoredDoc('3197688', '5031718', 1.0),
            9: GenericScoredDoc('3197688', '2211286', 0.89599609375),
            25632192: GenericScoredDoc('5186071', '4216565', 1.6033649444580078e-05),
        })
        self._test_webfaq_scoreddocs('fas', count=12654983, query_count=64000, items={
            0: GenericScoredDoc('74115', '174422', 0.978515625),
            9: GenericScoredDoc('74115', '62861', 0.00572967529296875),
            12654982: GenericScoredDoc('198105', '44180', 1.6033649444580078e-05),
        })
        self._test_webfaq_scoreddocs('fra', count=19140183, query_count=96000, items={
            0: GenericScoredDoc('478829', '390652', 0.99755859375),
            9: GenericScoredDoc('478829', '388486', 0.021575927734375),
            19140182: GenericScoredDoc('365034', '462459', 1.621246337890625e-05),
        })
        self._test_webfaq_scoreddocs('hin', count=6374233, query_count=32000, items={
            0: GenericScoredDoc('78546', '4509', 0.97802734375),
            9: GenericScoredDoc('78546', '21227', 0.019561767578125),
            6374232: GenericScoredDoc('26027', '92434', 1.5914440155029297e-05),
        })
        self._test_webfaq_scoreddocs('ind', count=6134393, query_count=32000, items={
            0: GenericScoredDoc('38453', '54660', 0.92236328125),
            9: GenericScoredDoc('38453', '5874', 0.80029296875),
            6134392: GenericScoredDoc('111049', '92495', 1.621246337890625e-05),
        })
        self._test_webfaq_scoreddocs('ita', count=18887103, query_count=96000, items={
            0: GenericScoredDoc('42516', '6372', 0.81591796875),
            9: GenericScoredDoc('42516', '248230', 0.04248046875),
            18887102: GenericScoredDoc('145531', '55960', 1.5914440155029297e-05),
        })
        self._test_webfaq_scoreddocs('jpn', count=19111766, query_count=96000, items={
            0: GenericScoredDoc('150118', '3930', 0.3916015625),
            9: GenericScoredDoc('150118', '303157', 0.050994873046875),
            19111765: GenericScoredDoc('36070', '38492', 1.6033649444580078e-05),
        })
        self._test_webfaq_scoreddocs('kor', count=6347985, query_count=32000, items={
            0: GenericScoredDoc('21838', '46725', 0.99951171875),
            9: GenericScoredDoc('21838', '32380', 0.0010204315185546875),
            6347984: GenericScoredDoc('2331', '12451', 1.5914440155029297e-05),
        })
        self._test_webfaq_scoreddocs('nld', count=18627158, query_count=96000, items={
            0: GenericScoredDoc('166508', '34136', 0.99853515625),
            9: GenericScoredDoc('166508', '327775', 0.0982666015625),
            18627157: GenericScoredDoc('336434', '58120', 1.633167266845703e-05),
        })
        self._test_webfaq_scoreddocs('pol', count=12775737, query_count=64000, items={
            0: GenericScoredDoc('35859', '86014', 0.99658203125),
            9: GenericScoredDoc('35859', '40064', 0.08404541015625),
            12775736: GenericScoredDoc('136630', '94056', 1.5914440155029297e-05),
        })
        self._test_webfaq_scoreddocs('por', count=12731380, query_count=64000, items={
            0: GenericScoredDoc('16001', '192830', 0.94140625),
            9: GenericScoredDoc('16001', '183541', 0.767578125),
            12731379: GenericScoredDoc('83132', '9936', 1.6033649444580078e-05),
        })
        self._test_webfaq_scoreddocs('rus', count=19040146, query_count=96000, items={
            0: GenericScoredDoc('107123', '36703', 1.0),
            9: GenericScoredDoc('107123', '281908', 0.10125732421875),
            19040145: GenericScoredDoc('171628', '314151', 1.6570091247558594e-05),
        })
        self._test_webfaq_scoreddocs('spa', count=19015957, query_count=96000, items={
            0: GenericScoredDoc('5211', '219409', 1.0),
            9: GenericScoredDoc('5211', '415271', 0.29296875),
            19015956: GenericScoredDoc('511973', '65822', 1.6033649444580078e-05),
        })
        self._test_webfaq_scoreddocs('swe', count=6155553, query_count=32000, items={
            0: GenericScoredDoc('57809', '79436', 0.99755859375),
            9: GenericScoredDoc('57809', '46781', 0.00130462646484375),
            6155552: GenericScoredDoc('106710', '5253', 1.5914440155029297e-05),
        })
        self._test_webfaq_scoreddocs('tur', count=6327043, query_count=32000, items={
            0: GenericScoredDoc('18437', '65738', 0.2147216796875),
            9: GenericScoredDoc('18437', '122822', 0.09857177734375),
            6327042: GenericScoredDoc('28705', '105668', 7.253885269165039e-05),
        })
        self._test_webfaq_scoreddocs('vie', count=6401341, query_count=32000, items={
            0: GenericScoredDoc('44221', '28405', 0.99853515625),
            9: GenericScoredDoc('44221', '75292', 0.01322174072265625),
            6401340: GenericScoredDoc('3335', '73856', 1.5914440155029297e-05),
        })
        self._test_webfaq_scoreddocs('zho', count=6379527, query_count=32000, items={
            0: GenericScoredDoc('72543', '53566', 0.9990234375),
            9: GenericScoredDoc('72543', '66974', 0.450439453125),
            6379526: GenericScoredDoc('26778', '77333', 1.6033649444580078e-05),
        })

    def _test_webfaq_scoreddocs(self, language, count, query_count, items):
        dataset = ir_datasets.load(f'webfaq/{language}/train')
        document_ids = {doc.doc_id for doc in dataset.docs_iter()}
        training_query_ids = {query.query_id for query in dataset.queries_iter()}
        remaining_items = dict(items)
        seen_query_ids = set()
        current_query_id = None
        current_doc_ids = set()
        previous_score = None
        actual_count = 0

        for index, scoreddoc in enumerate(dataset.scoreddocs_iter()):
            actual_count += 1
            if index in remaining_items:
                self._assert_namedtuple(scoreddoc, remaining_items.pop(index))
            if scoreddoc.query_id not in training_query_ids:
                self.fail(f'Unknown {language} scoreddoc query ID: {scoreddoc.query_id}')
            if scoreddoc.doc_id not in document_ids:
                self.fail(f'Unknown {language} scoreddoc document ID: {scoreddoc.doc_id}')
            if not math.isfinite(scoreddoc.score):
                self.fail(f'Non-finite {language} score: {scoreddoc.score}')

            if scoreddoc.query_id != current_query_id:
                if scoreddoc.query_id in seen_query_ids:
                    self.fail(f'Non-contiguous {language} scoreddoc query: {scoreddoc.query_id}')
                seen_query_ids.add(scoreddoc.query_id)
                current_query_id = scoreddoc.query_id
                current_doc_ids = set()
                previous_score = None
            if scoreddoc.doc_id in current_doc_ids:
                self.fail(
                    f'Duplicate {language} scoreddoc pair: '
                    f'{scoreddoc.query_id}/{scoreddoc.doc_id}'
                )
            if previous_score is not None and scoreddoc.score > previous_score:
                self.fail(f'Unsorted {language} scores for query {scoreddoc.query_id}')
            current_doc_ids.add(scoreddoc.doc_id)
            previous_score = scoreddoc.score

        self.assertEqual(count, actual_count)
        self.assertEqual({}, remaining_items)
        self.assertEqual(query_count, len(seen_query_ids))

    def test_referential_integrity(self):
        expected_counts = {
            'ara': {'docs': 141089, 'train': 132664, 'test': 10000},
            'dan': {'docs': 136939, 'train': 127686, 'test': 10000},
            'deu': {'docs': 886794, 'train': 881201, 'test': 10000},
            'eng': {'docs': 5252530, 'train': 5268725, 'test': 10000},
            'fas': {'docs': 226446, 'train': 216940, 'test': 10000},
            'fra': {'docs': 565142, 'train': 559505, 'test': 10000},
            'hin': {'docs': 99897, 'train': 90031, 'test': 10000},
            'ind': {'docs': 109774, 'train': 101315, 'test': 10000},
            'ita': {'docs': 255534, 'train': 247803, 'test': 10000},
            'jpn': {'docs': 307368, 'train': 299157, 'test': 10000},
            'kor': {'docs': 101036, 'train': 92000, 'test': 10000},
            'nld': {'docs': 368382, 'train': 360662, 'test': 10000},
            'pol': {'docs': 191578, 'train': 182515, 'test': 10000},
            'por': {'docs': 208209, 'train': 199353, 'test': 10000},
            'rus': {'docs': 383269, 'train': 377504, 'test': 10000},
            'spa': {'docs': 600855, 'train': 594661, 'test': 10000},
            'swe': {'docs': 157849, 'train': 148738, 'test': 10000},
            'tur': {'docs': 144115, 'train': 134846, 'test': 10000},
            'vie': {'docs': 123283, 'train': 113972, 'test': 10000},
            'zho': {'docs': 131606, 'train': 122491, 'test': 10000},
        }
        for language, counts in expected_counts.items():
            collection = ir_datasets.load(f'webfaq/{language}')
            documents = list(collection.docs_iter())
            document_ids = {doc.doc_id for doc in documents}
            document_texts = {doc.text for doc in documents}
            with self.subTest(language=language, component='documents'):
                self.assertEqual(counts['docs'], len(documents))
                self.assertEqual(counts['docs'], len(document_ids))
                self.assertEqual(counts['docs'], len(document_texts))

            query_ids_by_split = {}
            for split in ('train', 'test'):
                dataset = ir_datasets.load(f'webfaq/{language}/{split}')
                queries = list(dataset.queries_iter())
                query_ids = {query.query_id for query in queries}
                qrel_query_ids = set()
                with self.subTest(language=language, split=split):
                    self.assertEqual(counts[split], len(queries))
                    self.assertEqual(counts[split], len(query_ids))
                    for qrel in dataset.qrels_iter():
                        self.assertEqual(1, qrel.relevance)
                        self.assertIn(qrel.query_id, query_ids)
                        self.assertIn(qrel.doc_id, document_ids)
                        self.assertNotIn(qrel.query_id, qrel_query_ids)
                        qrel_query_ids.add(qrel.query_id)
                    self.assertEqual(query_ids, qrel_query_ids)
                query_ids_by_split[split] = query_ids
            self.assertTrue(
                query_ids_by_split['train'].isdisjoint(query_ids_by_split['test'])
            )

    def test_dataset_components(self):
        expected_components = {'webfaq': (False, False, False, False)}
        for language in LANGS:
            expected_components[f'webfaq/{language}'] = (True, False, False, False)
            expected_components[f'webfaq/{language}/train'] = (True, True, True, True)
            expected_components[f'webfaq/{language}/test'] = (True, True, True, False)
        for dataset_id, expected in expected_components.items():
            with self.subTest(dataset=dataset_id):
                dataset = ir_datasets.load(dataset_id)
                actual = (
                    dataset.has_docs(),
                    dataset.has_queries(),
                    dataset.has_qrels(),
                    dataset.has_scoreddocs(),
                )
                self.assertEqual(expected, actual)

        for language in LANGS:
            with self.assertRaises(KeyError):
                ir_datasets.load(f'webfaq/{language}/validation')

    def test_metadata(self):
        for language in LANGS:
            collection = ir_datasets.load(f'webfaq/{language}')
            train = ir_datasets.load(f'webfaq/{language}/train')
            test = ir_datasets.load(f'webfaq/{language}/test')
            with self.subTest(language=language):
                self.assertIs(collection.docs_handler(), train.docs_handler())
                self.assertIs(collection.docs_handler(), test.docs_handler())
                self.assertEqual(f'webfaq/{language}', collection.docs_namespace())
                self.assertEqual(language, collection.docs_lang())
                self.assertEqual(f'webfaq/{language}', train.queries_namespace())
                self.assertEqual(f'webfaq/{language}', test.queries_namespace())
                self.assertEqual(language, train.queries_lang())
                self.assertEqual(language, test.queries_lang())
                self.assertEqual(QREL_DEFS, train.qrels_defs())
                self.assertEqual(QREL_DEFS, test.qrels_defs())
                self.assertEqual(GenericDoc, collection.docs_cls())
                self.assertEqual(GenericQuery, train.queries_cls())
                self.assertEqual(TrecQrel, train.qrels_cls())
                self.assertEqual(GenericScoredDoc, train.scoreddocs_cls())

    def test_documentation(self):
        expected_citations = {'webfaq': ['Dinzinger2025WebFAQ', 'Dinzinger2026WebFAQ2']}
        for language in LANGS:
            expected_citations[f'webfaq/{language}'] = ['Dinzinger2025WebFAQ']
            expected_citations[f'webfaq/{language}/train'] = ['Dinzinger2025WebFAQ', 'Dinzinger2026WebFAQ2']
            expected_citations[f'webfaq/{language}/test'] = ['Dinzinger2025WebFAQ']
        for dataset_id, citations in expected_citations.items():
            with self.subTest(dataset=dataset_id):
                documentation = ir_datasets.load(dataset_id).documentation()
                self.assertIn('WebFAQ', documentation['desc'])
                self.assertEqual(citations, documentation['bibtex_ids'])


if __name__ == '__main__':
    unittest.main()
