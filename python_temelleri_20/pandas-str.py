import pandas as pd

data = pd.read_csv("NBA_list_new.csv")

data.dropna(inplace = True)  # Nan değerlere sahip rowlar gider kayıtlar içinden gider.

print(data.head(10))
"""
            PLAYER TEAM  AGE  HEIGHT  WEIGHT  ...   DREB%    USG%     TS%    AST% COUN_CODE
0     Aaron Gordon  ORL   23      81     220  ...  16.50%  21.20%  53.80%  16.60%       USA
1    Aaron Holiday  IND   22      73     185  ...   8.80%  20.40%  51.80%  18.00%       USA
2      Abdel Nader  OKC   25      78     225  ...  13.90%  14.70%  52.20%   4.40%       EGY
3       Al Horford  BOS   33      82     245  ...  16.10%  18.70%  60.50%  20.30%       DOM
4  Al-Farouq Aminu  POR   28      81     220  ...  20.40%  13.30%  56.80%   5.70%       USA
5    Alan Williams  BKN   26      80     265  ...  40.50%  22.20%  61.00%  17.60%       USA
6       Alec Burks  SAC   27      78     214  ...  15.10%  18.40%  52.30%  14.20%       USA
7     Alex Abrines  OKC   25      78     200  ...   6.70%  11.90%  50.70%   4.70%       ESP
8      Alex Caruso  LAL   25      77     186  ...   7.90%  18.40%  56.90%  20.50%       USA
9         Alex Len  ATL   25      85     250  ...  15.90%  21.20%  57.50%   8.60%       UKR

[10 rows x 21 columns]
"""


column_info = data.columns
print(column_info)
"""
Index(['PLAYER', 'TEAM', 'AGE', 'HEIGHT', 'WEIGHT', 'COLLEGE', 'COUNTRY',     
       'DRAFT YEAR', 'DRAFT ROUND', 'DRAFT NUMBER', 'GP', 'PTS', 'REB', 'AST',
       'NETRTG', 'OREB%', 'DREB%', 'USG%', 'TS%', 'AST%', 'COUN_CODE'],       
      dtype='object')
"""


data["PLAYER"] = data["PLAYER"].str.lower()
print(data.head(10))
"""
            PLAYER TEAM  AGE  HEIGHT  WEIGHT  ...   DREB%    USG%     TS%    AST% COUN_CODE
0     aaron gordon  ORL   23      81     220  ...  16.50%  21.20%  53.80%  16.60%       USA
1    aaron holiday  IND   22      73     185  ...   8.80%  20.40%  51.80%  18.00%       USA
2      abdel nader  OKC   25      78     225  ...  13.90%  14.70%  52.20%   4.40%       EGY
3       al horford  BOS   33      82     245  ...  16.10%  18.70%  60.50%  20.30%       DOM
4  al-farouq aminu  POR   28      81     220  ...  20.40%  13.30%  56.80%   5.70%       USA
5    alan williams  BKN   26      80     265  ...  40.50%  22.20%  61.00%  17.60%       USA
6       alec burks  SAC   27      78     214  ...  15.10%  18.40%  52.30%  14.20%       USA
7     alex abrines  OKC   25      78     200  ...   6.70%  11.90%  50.70%   4.70%       ESP
8      alex caruso  LAL   25      77     186  ...   7.90%  18.40%  56.90%  20.50%       USA
9         alex len  ATL   25      85     250  ...  15.90%  21.20%  57.50%   8.60%       UKR

[10 rows x 21 columns]
"""


data["PLAYER"] = data["PLAYER"].str.upper()
# data["PLAYER"] = data.PLAYER.str.upper()  yukardakiyle aynı kullanımı 
print(data.head(10))
"""
            PLAYER TEAM  AGE  HEIGHT  WEIGHT  ...   DREB%    USG%     TS%    AST% COUN_CODE
0     AARON GORDON  ORL   23      81     220  ...  16.50%  21.20%  53.80%  16.60%       USA
1    AARON HOLIDAY  IND   22      73     185  ...   8.80%  20.40%  51.80%  18.00%       USA
2      ABDEL NADER  OKC   25      78     225  ...  13.90%  14.70%  52.20%   4.40%       EGY
3       AL HORFORD  BOS   33      82     245  ...  16.10%  18.70%  60.50%  20.30%       DOM
4  AL-FAROUQ AMINU  POR   28      81     220  ...  20.40%  13.30%  56.80%   5.70%       USA
5    ALAN WILLIAMS  BKN   26      80     265  ...  40.50%  22.20%  61.00%  17.60%       USA
6       ALEC BURKS  SAC   27      78     214  ...  15.10%  18.40%  52.30%  14.20%       USA
7     ALEX ABRINES  OKC   25      78     200  ...   6.70%  11.90%  50.70%   4.70%       ESP
8      ALEX CARUSO  LAL   25      77     186  ...   7.90%  18.40%  56.90%  20.50%       USA
9         ALEX LEN  ATL   25      85     250  ...  15.90%  21.20%  57.50%   8.60%       UKR

[10 rows x 21 columns]
"""

data["INDEX"] = data["PLAYER"].str.find("A") # isimlerde ilk a karakterin indexini verir.

print(data.tail(10))                         # burda biz kendimiz yeni bir INDEX adlı column oluşturduk.
"""
              PLAYER TEAM  AGE  HEIGHT  WEIGHT  ...    USG%     TS%    AST% COUN_CODE INDEX
520  WILSON CHANDLER  LAC   32      81     225  ...  11.50%  53.70%   8.90%       USA     9
521      YANTE MATEN  MIA   22      80     240  ...  13.30%  25.00%   0.00%       USA     1
522     YOGI FERRELL  SAC   26      72     180  ...  15.80%  55.00%  17.60%       USA    -1
523    YUTA WATANABE  MEM   24      81     205  ...  14.80%  35.20%   6.30%       JPN     3
524     ZACH COLLINS  POR   21      84     235  ...  16.40%  56.20%   7.60%       USA     1
525      ZACH LAVINE  CHI   24      77     200  ...  29.60%  57.40%  22.40%       USA     1
526      ZACH LOFTON  DET   26      76     180  ...  25.00%   0.00%   0.00%       USA     1
527    ZAZA PACHULIA  DET   35      83     270  ...  14.60%  53.90%  16.10%       GEO     1
528     ZHAIRE SMITH  PHI   20      76     199  ...  16.40%  53.30%  10.10%       USA     2
529          ZHOU QI  HOU   23      85     210  ...  33.30%    100%   0.00%       CHN    -1

[10 rows x 22 columns]
"""


result = data.PLAYER.str.contains("JORDAN")
# result = data["PLAYER"].str.contains("JORDAN")
print(result)
"""
0      False
1      False
2      False
3      False
4      False
       ...
525    False
526    False
527    False
528    False
529    False
Name: PLAYER, Length: 530, dtype: bool
"""

print(data[result])
"""
              PLAYER TEAM  AGE  HEIGHT  WEIGHT  ...    USG%      TS%    AST% COUN_CODE INDEX
106   DEANDRE JORDAN  NYK   30      83     265  ...  14.80%   67.40%  11.90%       USA     2
272      JORDAN BELL  GSW   24      81     224  ...  13.20%   53.10%  13.40%       USA     4
273  JORDAN CLARKSON  CLE   27      77     194  ...  26.40%   53.90%  15.30%       USA     4
274      JORDAN LOYD  TOR   25      76     210  ...  15.70%   63.50%  18.20%       USA     4
275     JORDAN MCRAE  WAS   28      77     179  ...  19.00%   55.00%  13.10%       USA     4
276    JORDAN SIBERT  ATL   26      76     187  ...   8.30%  150.00%   0.00%       USA     4

[6 rows x 22 columns]
"""


result1 = data.PLAYER.str.replace(" ","-")
# result1 = data["PLAYER"].str.replace(" ","-")
print(result1.head(10))
"""
0       AARON-GORDON
1      AARON-HOLIDAY
2        ABDEL-NADER
3         AL-HORFORD
4    AL-FAROUQ-AMINU
5      ALAN-WILLIAMS
6         ALEC-BURKS
7       ALEX-ABRINES
8        ALEX-CARUSO
9           ALEX-LEN
Name: PLAYER, dtype: object
"""


result2 = data.PLAYER.str.replace(" ","-").str.replace("A","*")
# result2 = data["PLAYER"].str.replace(" ","-")
print(result2.head(10))
"""
0       **RON-GORDON
1      **RON-HOLID*Y
2        *BDEL-N*DER
3         *L-HORFORD
4    *L-F*ROUQ-*MINU
5      *L*N-WILLI*MS
6         *LEC-BURKS
7       *LEX-*BRINES
8        *LEX-C*RUSO
9           *LEX-LEN
Name: PLAYER, dtype: object
"""

data[["FirstName","LastName"]] = data["PLAYER"].loc[ data["PLAYER"].str.split().str.len() == 2 ].str.split(expand=True)  # PLAYER da iki karakterli olan isimleri firstName ve lastNAme olark yeni column oluşturur.
print(data)
"""
              PLAYER TEAM  AGE  HEIGHT  WEIGHT  ...    AST% COUN_CODE INDEX  FirstName  LastName
0       AARON GORDON  ORL   23      81     220  ...  16.60%       USA     0      AARON    GORDON        
1      AARON HOLIDAY  IND   22      73     185  ...  18.00%       USA     0      AARON   HOLIDAY        
2        ABDEL NADER  OKC   25      78     225  ...   4.40%       EGY     0      ABDEL     NADER        
3         AL HORFORD  BOS   33      82     245  ...  20.30%       DOM     0         AL   HORFORD        
4    AL-FAROUQ AMINU  POR   28      81     220  ...   5.70%       USA     0  AL-FAROUQ     AMINU        
..               ...  ...  ...     ...     ...  ...     ...       ...   ...        ...       ...        
525      ZACH LAVINE  CHI   24      77     200  ...  22.40%       USA     1       ZACH    LAVINE        
526      ZACH LOFTON  DET   26      76     180  ...   0.00%       USA     1       ZACH    LOFTON        
527    ZAZA PACHULIA  DET   35      83     270  ...  16.10%       GEO     1       ZAZA  PACHULIA        
528     ZHAIRE SMITH  PHI   20      76     199  ...  10.10%       USA     2     ZHAIRE     SMITH        
529          ZHOU QI  HOU   23      85     210  ...   0.00%       CHN    -1       ZHOU        QI        

[530 rows x 24 columns]
"""