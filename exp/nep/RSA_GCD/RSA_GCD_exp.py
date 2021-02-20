from Crypto.Util.number import *

c1 = 14617094664547143588835612166539019259019556827725131406704474099507762198023101386887569685838651124817323416709185466107661347188087238066212618031870679316233155742459689693666379572893412218757980574758299939399993905398492147957493236406232810173797000915531471363634159091903530179205559011696688437112482650226131419745506291952860346713914550032504669101771617236495641513512605873636213325713545594525388276471739911539438780271494507671606569375129395062640386039482769626106359136050612985036985942445426780156568356171304121556002061783820628600683744762705068452614270513748150192353463212578621696188222
n1 = 27869904946491996402895516595031727496821245463122984190552086420945633593419620875644657232582857421196314696046085050182860843660737597290194420488503986808256629904878322158158138395122551503165667269355286459527268458354617622267018261129069643304814164525211042984241690039934130953446677872162924750111499453966376827044083791553415790408332287499877448208501682250931684632835556702955922986290384835864878913726848050421425941885667810849016560642546101800372861925623895137418710887891048883541779327025558359082011405733984358676071094952554563356919613709417468662736863408209280231524769580321279013389837
c2 = 19460492464347799537265707564099050969287242344388151951433645045229717645603665539642759313422959488578218799168392783303887594350267263722066737022631924782498876208466162359174788796524562217947458256254765449044918971304807420070926853840183693867067647077237373554214469915975010086659583569664804099742745250696218805426613996049368044510290496142134678011352104014492745528833153138452599185503575418963974552453171022036151429106423349713034336842961268757174804681431867061341385816681455659630343147033130526259675169116912518362341420571434933911789926779566740904463894440616415743547466074689840075232993
n2 = 25382990345903234470046112360844130887586055184215824811043668009650090501075406131990722193131508718035851434243508916358922884782055965526704229277887825216642383198639583914682768713545710253161121917660793535885836036394219280335851506733887347044727214786831560204805078006474222996718795669405454504087615047794991587224715991320447968163892037624475583375997273506124676020428414872873301792836777703237457384916335931576598258521655601425801907843461477817922847958909993035587636406617863563330601493792836839999383952927002552604252386771795987042278173015671608882324664236077753195826319533743430285918839

e = 65537

p = GCD(n1, n2)
q1 = n1//p

d1 = inverse(e, (p-1)*(q1-1))
m = pow(c1, d1, n1)
print(long_to_bytes(m))
