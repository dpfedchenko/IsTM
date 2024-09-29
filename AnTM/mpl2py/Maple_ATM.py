import numpy as np

MS = [[749.6251874, .6966649055], [749.2507496, .6969161480], [748.8766852, .6975050013], [748.5029940, .6984313815], [748.1296762, .6996933199], [747.7567300, .7012866081], [747.3841555, .7032044930], [747.0119526, .7054378418], [746.6401196, .7079737607], [746.2686567, .7107961135], [745.8975638, .7138846180], [745.5268392, .7172143201], [745.1564829, .7207552016], [744.7864949, .7244714504], [744.4168736, .7283208178], [744.0476190, .7322539913], [743.6787312, .7362144190], [743.3102083, .7401369852], [742.9420505, .7439482794], [742.5742578, .7475658556], [742.2068285, .7508982641], [741.8397626, .7538453833], [741.4730602, .7562983712], [741.1067196, .7581413104], [740.7407407, .7592519719], [740.3751238, .7595041278], [740.0098670, .7587697607], [739.6449704, .7569225569], [739.2804341, .7538408553], [738.9162563, .7494125839], [738.5524372, .7435388472], [738.1889767, .7361387755], [737.8258733, .7271538130], [737.4631268, .7165514794], [737.1007375, .7043283602], [736.7387035, .6905120033], [736.3770250, .6751620561], [736.0157020, .6583689484], [735.6547329, .6402520884], [735.2941176, .6209564496], [734.9338563, .6006471914], [734.5739473, .5795050200], [734.2143906, .5577200599], [733.8551863, .5354852545], [733.4963327, .5129910131], [733.1378299, .4904202456], [732.7796779, .4679436016], [732.4218752, .4457165519], [732.0644217, .4238766863], [731.7073174, .4025426076], [731.3505609, .3818133866], [730.9941520, .3617688995], [730.6380910, .3424706982], [730.2823760, .3239633587], [729.9270073, .3062762422], [729.5719848, .2894252475], [729.2173069, .2734146017], [728.8629738, .2582388077], [728.5089853, .2438843460], [728.1553400, .2303312444], [727.8020378, .2175546057], [727.4490789, .2055257252], [727.0964616, .1942133578], [726.7441860, .1835844772], [726.3922522, .1736052216], [726.0406585, .1642412935], [725.6894049, .1554587170], [725.3384916, .1472239856], [724.9879170, .1395046004], [724.6376812, .1322691162], [724.2877840, .1254873314], [723.9382241, .1191305217], [723.5890014, .1131713148], [723.2401161, .1075838289], [722.8915664, .1023436953], [722.5433526, 0.9742794378e-1], [722.1954746, 0.9281505062e-1], [721.8479309, 0.8848483806e-1], [721.5007215, 0.8441844350e-1], [721.1538465, 0.8059824840e-1], [720.8073044, 0.7700784410e-1], [720.4610951, 0.7363191293e-1], [720.1152188, 0.7045620719e-1], [719.7696739, 0.6746746113e-1], [719.4244604, 0.6465333801e-1], [719.0795785, 0.6200237369e-1], [718.7350265, 0.5950390481e-1], [718.3908046, 0.5714802068e-1], [718.0469127, 0.5492551462e-1], [717.7033495, 0.5282782520e-1], [717.3601148, 0.5084699998e-1], [717.0172088, 0.4897564711e-1], [716.6746299, 0.4720689352e-1], [716.3323782, 0.4553434482e-1], [715.9904538, 0.4395205951e-1], [715.6488551, 0.4245450538e-1], [715.3075823, 0.4103654383e-1], [714.9666352, 0.3969337687e-1], [714.6260126, 0.3842055357e-1], [714.2857143, 0.3721391552e-1], [713.9457405, 0.3606958900e-1], [713.6060896, 0.3498397115e-1], [713.2667618, 0.3395369526e-1], [712.9277570, 0.3297562383e-1], [712.5890738, 0.3204682877e-1], [712.2507122, 0.3116457545e-1], [711.9126724, 0.3032631271e-1], [711.5749527, 0.2952965273e-1], [711.2375533, 0.2877237216e-1], [710.9004743, 0.2805238189e-1], [710.5637140, 0.2736773953e-1], [710.2272727, 0.2671662009e-1], [709.8911504, 0.2609732047e-1], [709.5553455, 0.2550824396e-1], [709.2198582, 0.2494789804e-1], [708.8846884, 0.2441488519e-1], [708.5498348, 0.2390789334e-1], [708.2152974, 0.2342569950e-1], [707.8810763, 0.2296715420e-1], [707.5471700, 0.2253117970e-1], [707.2135785, 0.2211676993e-1], [706.8803019, 0.2172298137e-1], [706.5473388, 0.2134892995e-1], [706.2146893, 0.2099378734e-1], [705.8823533, 0.2065677976e-1], [705.5503294, 0.2033718283e-1], [705.2186178, 0.2003431776e-1], [704.8872184, 0.1974755303e-1], [704.5561298, 0.1947629656e-1], [704.2253521, 0.1921999594e-1], [703.8948849, 0.1897813879e-1], [703.5647281, 0.1875024585e-1], [703.2348804, 0.1853587372e-1], [702.9053419, 0.1833460914e-1], [702.5761126, 0.1814607292e-1], [702.2471910, 0.1796991270e-1], [701.9185773, 0.1780580632e-1], [701.5902714, 0.1765345773e-1], [701.2622721, 0.1751259772e-1], [700.9345793, 0.1738298103e-1], [700.6071931, 0.1726439118e-1], [700.2801120, 0.1715663256e-1], [699.9533363, 0.1705953180e-1], [699.6268658, 0.1697294180e-1], [699.3006993, 0.1689673712e-1], [698.9748367, 0.1683081147e-1], [698.6492782, 0.1677508613e-1], [698.3240223, 0.1672949978e-1], [697.9990692, 0.1669401581e-1], [697.6744188, 0.1666861830e-1], [697.3500697, 0.1665331448e-1], [697.0260226, 0.1664813302e-1], [696.7022761, 0.1665312686e-1], [696.3788301, 0.1666837096e-1], [696.0556848, 0.1669396629e-1], [695.7328388, 0.1673003550e-1], [695.4102921, 0.1677672885e-1], [695.0880448, 0.1683422206e-1], [694.7660956, 0.1690272065e-1], [694.4444444, 0.1698245563e-1], [694.1230915, 0.1707369056e-1], [693.8020353, 0.1717672077e-1], [693.4812760, 0.1729187360e-1], [693.1608131, 0.1741951432e-1], [692.8406468, 0.1756004381e-1], [692.5207756, 0.1771390472e-1], [692.2011997, 0.1788158271e-1], [691.8819190, 0.1806360834e-1], [691.5629322, 0.1826056450e-1], [691.2442395, 0.1847308471e-1], [690.9258408, 0.1870186220e-1], [690.6077348, 0.1894764890e-1], [690.2899216, 0.1921126890e-1], [689.9724013, 0.1949361484e-1], [689.6551724, 0.1979566489e-1], [689.3382351, 0.2011847737e-1], [689.0215895, 0.2046320832e-1], [688.7052342, 0.2083111834e-1], [688.3891692, 0.2122358048e-1], [688.0733947, 0.2164209121e-1], [687.7579092, 0.2208828498e-1], [687.4427129, 0.2256394856e-1], [687.1278059, 0.2307103181e-1], [686.8131868, 0.2361167006e-1], [686.4988557, 0.2418820502e-1], [686.1848126, 0.2480320150e-1], [685.8710562, 0.2545947602e-1], [685.5575867, 0.2616012728e-1], [685.2444040, 0.2690856493e-1], [684.9315068, 0.2770854452e-1], [684.6188953, 0.2856422050e-1], [684.3065695, 0.2948017745e-1], [683.9945280, 0.3046150192e-1], [683.6827710, 0.3151382739e-1], [683.3712986, 0.3264342349e-1], [683.0601093, 0.3385726739e-1], [682.7492033, 0.3516313932e-1], [682.4385807, 0.3656974225e-1], [682.1282401, 0.3808681063e-1], [681.8181817, 0.3972527799e-1], [681.5084054, 0.4149743713e-1], [681.1989101, 0.4341714095e-1], [680.8896957, 0.4550002808e-1], [680.5807624, 0.4776381305e-1], [680.2721088, 0.5022859354e-1], [679.9637351, 0.5291720587e-1], [679.6556413, 0.5585569712e-1], [679.3478261, 0.5907380633e-1], [679.0402896, 0.6260557564e-1], [678.7330318, 0.6649006406e-1], [678.4260516, 0.7077215918e-1], [678.1193489, 0.7550354287e-1], [677.8129238, 0.8074382282e-1], [677.5067751, 0.8656177284e-1], [677.2009028, 0.9303685052e-1], [676.8953070, .1002607899], [676.5899865, .1083393768], [676.2849412, .1173942808], [675.9801714, .1275647638], [675.6756757, .1390091191], [675.3714541, .1519052014], [675.0675069, .1664493552], [674.7638327, .1828525774], [674.4604315, .2013322141], [674.1573035, .2220960943], [673.8544474, .2453159975], [673.5518633, .2710859544], [673.2495513, .2993602329], [672.9475101, .3298703578], [672.6457398, .3620229207], [672.3442404, .3947973105], [672.0430108, .4266775345], [671.7420509, .4556754708], [671.4413609, .4795044468], [671.1409396, .4959282372], [670.8407870, .5032261120], [670.5409031, .5006220485], [670.2412869, .4884924418], [669.9419382, .4682547346], [669.6428573, .4419927525], [669.3440428, .4119875394], [669.0454949, .3803256001], [668.7472137, .3486725975], [668.4491979, .3182067445], [668.1514475, .2896613425], [667.8539627, .2634174859], [667.5567423, .2396046245], [667.2597863, .2181882097], [666.9630949, .1990365574], [666.6666667, .1819678307], [666.3705019, .1667807345], [666.0746005, .1532733771], [665.7789614, .1412540945], [665.4835846, .1305467000], [665.1884702, .1209928206], [664.8936170, .1124519309], [664.5990251, .1048005185], [664.3046946, 0.9793064965e-1], [664.0106242, 0.9174831264e-1], [663.7168140, 0.8617182036e-1], [663.4232642, 0.8113020813e-1], [663.1299735, 0.7656184967e-1], [662.8369420, 0.7241317125e-1], [662.5441698, 0.6863755705e-1], [662.2516556, 0.6519434143e-1], [661.9593997, 0.6204805769e-1], [661.6674020, 0.5916764961e-1], [661.3756614, 0.5652589502e-1], [661.0841779, 0.5409888513e-1], [660.7929517, 0.5186555467e-1], [660.5019815, 0.4980732980e-1], [660.2112675, 0.4790778550e-1], [659.9208096, 0.4615235169e-1], [659.6306069, 0.4452811014e-1], [659.3406592, 0.4302354870e-1], [659.0509668, 0.4162840713e-1], [658.7615283, 0.4033352241e-1], [658.4723440, 0.3913069054e-1], [658.1834139, 0.3801255967e-1], [657.8947368, 0.3697251742e-1], [657.6063129, 0.3600462418e-1], [657.3181421, 0.3510352088e-1], [657.0302234, 0.3426437410e-1], [656.7425568, 0.3348281860e-1], [656.4551424, 0.3275490169e-1], [656.1679790, 0.3207703969e-1], [655.8810668, 0.3144599077e-1], [655.5944057, 0.3085880729e-1], [655.3079948, 0.3031281195e-1], [655.0218339, 0.2980557151e-1], [654.7359233, 0.2933487317e-1], [654.4502618, 0.2889870399e-1], [654.1648494, 0.2849523254e-1], [653.8796863, 0.2812279099e-1], [653.5947712, 0.2777986456e-1], [653.3101044, 0.2746507344e-1], [653.0256858, 0.2717716952e-1], [652.7415144, 0.2691501199e-1], [652.4575901, 0.2667757595e-1], [652.1739132, 0.2646393251e-1], [651.8904824, 0.2627324148e-1], [651.6072979, 0.2610475424e-1], [651.3243597, 0.2595779768e-1], [651.0416667, 0.2583177470e-1], [650.7592189, 0.2572615772e-1], [650.4770166, 0.2564048719e-1], [650.1950585, 0.2557436406e-1], [649.9133447, 0.2552745281e-1], [649.6318754, 0.2549947073e-1], [649.3506494, 0.2549019295e-1], [649.0696667, 0.2549944666e-1], [648.7889275, 0.2552711121e-1], [648.5084306, 0.2557311315e-1], [648.2281762, 0.2563743247e-1], [647.9481643, 0.2572009484e-1], [647.6683938, 0.2582117208e-1], [647.3888648, 0.2594078709e-1], [647.1095774, 0.2607911084e-1], [646.8305304, 0.2623635605e-1], [646.5517240, 0.2641278969e-1], [646.2731583, 0.2660872425e-1], [645.9948320, 0.2682452417e-1], [645.7167454, 0.2706060476e-1], [645.4388986, 0.2731743233e-1], [645.1612903, 0.2759552630e-1], [644.8839208, 0.2789546606e-1], [644.6067900, 0.2821788638e-1], [644.3298969, 0.2856348273e-1], [644.0532416, 0.2893301342e-1], [643.7768242, 0.2932730584e-1], [643.5006435, 0.2974725437e-1], [643.2246997, 0.3019383020e-1], [642.9489929, 0.3066807733e-1], [642.6735218, 0.3117112742e-1], [642.3982868, 0.3170419533e-1], [642.1232878, 0.3226859116e-1], [641.8485237, 0.3286571963e-1], [641.5739947, 0.3349709505e-1], [641.2997005, 0.3416433896e-1], [641.0256410, 0.3486919355e-1], [640.7518153, 0.3561353068e-1], [640.4782235, 0.3639935420e-1], [640.2048656, 0.3722881875e-1], [639.9317405, 0.3810422949e-1], [639.6588483, 0.3902806377e-1], [639.3861893, 0.4000298003e-1], [639.1137621, 0.4103182747e-1], [638.8415670, 0.4211766160e-1], [638.5696041, 0.4326376400e-1], [638.2978722, 0.4447366215e-1], [638.0263715, 0.4575112927e-1], [637.7551020, 0.4710023351e-1], [637.4840628, 0.4852533018e-1], [637.2132538, 0.5003110917e-1], [636.9426752, 0.5162260639e-1], [636.6723258, 0.5330523238e-1], [636.4022059, 0.5508480415e-1], [636.1323155, 0.5696758181e-1], [635.8626535, 0.5896028823e-1], [635.5932201, 0.6107016454e-1], [635.3240152, 0.6330499695e-1], [635.0550380, 0.6567316328e-1], [634.7862883, 0.6818367017e-1], [634.5177665, 0.7084620981e-1], [634.2494713, 0.7367121783e-1], [633.9814029, 0.7666990655e-1], [633.7135615, 0.7985434569e-1], [633.4459458, 0.8323748392e-1], [633.1785561, 0.8683324031e-1], [632.9113924, 0.9065656659e-1], [632.6444537, 0.9472351064e-1], [632.3777400, 0.9905122634e-1], [632.1112516, .1036581194], [631.8449872, .1085638275], [631.5789471, .1137893146], [631.3131313, .1193569022], [631.0475388, .1252902955], [630.7821696, .1316145632], [630.5170240, .1383561916], [630.2521007, .1455429686], [629.9874000, .1532039711], [629.7229219, .1613694005], [629.4586654, .1700703564], [629.1946306, .1793387285], [628.9308176, .1892066745], [628.6672254, .1997063323], [628.4038539, .2108691171], [628.1407035, .2227252455], [627.8777730, .2353026130], [627.6150625, .2486260513], [627.3525721, .2627160114], [627.0903009, .2775871441], [626.8282488, .2932469646], [626.5664160, .3096938566], [626.3048015, .3269155276], [626.0434054, .3448868321], [625.7822278, .3635680427], [625.5212676, .3829028886], [625.2605250, .4028170990], [625.0000000, .4232170443], [624.7396917, .4439892499], [624.4796001, .4650004757], [624.2197253, .4860984375], [623.9600664, .5071143478], [623.7006234, .5278654236], [623.4413965, .5481596423], [623.1823846, .5678005868], [622.9235878, .5865935480], [622.6650062, .6043521433], [622.4066389, .6209046010], [622.1484858, .6361000692], [621.8905473, .6498136889], [621.6328221, .6619512849], [621.3753104, .6724514479], [621.1180124, .6812870158], [620.8609270, .6884641145], [620.6040544, .6940204987], [620.3473945, .6980221323], [620.0909465, .7005586794], [619.8347105, .7017390892], [619.5786865, .7016861755], [619.3228735, .7005321336], [619.0672717, .6984138866], [618.8118812, .6954686235], [618.5567009, .6918312133], [618.3017310, .6876309093], [618.0469716, .6829896120], [617.7924216, .6780202526], [617.5380813, .6728262338], [617.2839506, .6675008593], [617.0300287, .6621273326], [616.7763155, .6567790620], [616.5228113, .6515202046], [616.2695151, .6464059931], [616.0164269, .6414839415], [615.7635468, .6367941100], [615.5108739, .6323700237], [615.2584083, .6282394569], [615.0061501, .6244251475], [614.7540982, .6209452372], [614.5022529, .6178139146], [614.2506142, .6150422299], [613.9991812, .6126380470], [613.7479539, .6106070107], [613.4969325, .6089524341], [613.2461160, .6076759155], [612.9955044, .6067774751], [612.7450980, .6062556200], [612.4948958, .6061078644], [612.2448977, .6063306694], [611.9951040, .6069195085], [611.7455137, .6078690757], [611.4961269, .6091733333], [611.2469438, .6108254732], [610.9979632, .6128179739], [610.7491854, .6151427324], [610.5006105, .6177909452], [610.2522375, .6207530233], [610.0040664, .6240188083], [609.7560976, .6275772877], [609.5083298, .6314168328], [609.2607634, .6355247882], [609.0133983, .6398879055], [608.7662336, .6444919118], [608.5192695, .6493217312], [608.2725061, .6543614228], [608.0259423, .6595939182], [607.7795784, .6650014268], [607.5334143, .6705651799], [607.2874493, .6762653463], [607.0416833, .6820814492], [606.7961165, .6879919987], [606.5507480, .6939747977], [606.3055778, .7000070133], [606.0606061, .7060652345], [605.8158319, .7121253641], [605.5712553, .7181633831], [605.3268765, .7241548260], [605.0826945, .7300752123], [604.8387094, .7359004458], [604.5949214, .7416067178], [604.3513295, .7471707954], [604.1079337, .7525703747], [603.8647343, .7577841109], [603.6217303, .7627920236], [603.3789217, .7675753665], [603.1363088, .7721172419], [602.8938906, .7764025720], [602.6516671, .7804182195], [602.4096386, .7841532444], [602.1678040, .7875988176], [601.9261635, .7907487348], [601.6847172, .7935988281], [601.4434642, .7961474321], [601.2024046, .7983954678], [600.9615385, .8003459236], [600.7208649, .8020043267], [600.4803841, .8033779821], [600.2400960, .8044766642], [599.9999999, .8053117974]]

MS1 = np.zeros(len(MS))
MS2 = np.zeros(len(MS))

for i in range(len(MS)):
    MS1[i] = MS[i][0]
    MS2[i] = MS[i][1]
