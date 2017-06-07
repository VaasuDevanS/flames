FLAMES
******
>>>
 A python module for our famous childhood game..! 
 FLAMES : Friend Love Affection Marriage Enemy Siblings

>>>
 We all love to play this game during our childhood days.
 Putting FLAMES with your name and our crush name and getting L, M or A
 will be the most happiest moment of our time.
 Or even Worse..! we will be teased by our friend if we get S or E...

Now you can do this in python with ease and also get your Relationship percentage..

Developed with love by Vaasu Devan S <vaasuceg.96@gmail.com>

Github Url https://www.github.com/VaasuDevanS/flames

Installation
************

$ pip install flames

     or

$ pip3 install flames

Importing the Package
=============================================

>>> from flames import flames

USAGE
=====
syntax:-
             
 >>> i = flames("india", "china")
 >>> i
 <-india:FLAMES:china->
 >>> i.result()
             ,       ,
            /(       )`
            \ \__   / |
            /- _ `-/  '
           (/\/ \ \   /\
           / /   | `    \
           O O   )      |
           `-^--'`<     '
          (_.)  _ )    /
           `.___/`    /
             `-----' /
 <----.     __ / __   \
 <----|====O)))==) \) /=============
 <----'    `--' `.__,' \
             |         |
              \       /
          ____( (_   / \______
        ,'  ,----'   |        \
        `--{__________)       \/

 >>> i.info()
 Name                     : india
 Crush                    : china
 Result                   : ENEMY
 FLAMES Count             : 4
 Common Letters           : i, a, n
 Order                    : M, L, F, A, S
 Relationship Percentage  : 74
 >>> i.value
 ENEMY 

 >>> i = flames("india", "america")
 >>> i
 <-india:FLAMES:america->
 >>> i.result()
          ,;;;;;,
        ,;;;;;;;;,
        ;;;'____ ;
        ;;;(\\\\\;
        `/'((|||||
    ___ <  C))||||
   ,'    \__(((||),
   |    \  _)))))))\,_
  /|    |/"\`\`""""' |)
  ;  \    \  ) \_____/_|
  |  |\    '    _.,-' |
  |  ' \    \.,-'   _./ |
  (  _,-\      _.-''  |  ;
   "'|___\__.-'       ;  )
    |----|   _.--,;'   ;
   ,'  , | (     __.,-'
   | ,' ,'  `""''   `.
   |    ;            )
   `,   (            )
    |   (           ,'
    |   |           (
    |   |           |
    |   |           |
    |   |___________|
    |   |      |    |

 >>> i.info()
 Name                     : india
 Crush                    : america
 Result                   : AFFECTION
 FLAMES Count             : 8
 Common Letters           : i, a
 Order                    : L, E, M, F, S
 Relationship Percentage  : 39
 >>> i.value
 AFFECTION

 >>> i = flames("india", "australia")
 >>> i
 <-india:FLAMES:australia->
 >>> i.result()
               __        __        __        __
  .*.        /~ .~\    /~  ~\    /~ .~\    /~  ~\
  ***       '      `\/'      *  '      `\/'      *
   V       (                .*)(               . *)
 /\|/\      \            . *./  \            . *./
   |         `\ .      . .*/'    `\ .      . .*/'       .*.
   |           `\ * .*. */' _    _ `\ * .*. */'         ***
                 `\ * */'  ( `\/'*)  `\ * */'          /\V
                   `\/'     \   */'    `\/'              |/\
                             `\/'                        |

 >>> i.info()
 Name                     : india
 Crush                    : australia
 Result                   : LOVE
 FLAMES Count             : 10
 Common Letters           : i, a
 Order                    : M, A, S, F, E
 Relationship Percentage  : 22
 >>> i.value
 LOVE

 >>> details = i.getinfo()
 >>> type(details)
 <type 'dict'>     # All the details shown in i.info method()

time
====
>>> i.result(time=1)                 # 0.09 is default time, #Just for Animation

More patterns
=============
>>> i = flames("india", "australia")
>>> i
 <-india:FLAMES:australia->
>>> i.result(no=3)
        ...e$e.$...e$                 ...e$e.$...e
     !$6lkasd!$6lkasd!$6l          !$6lkasd!$6lkasd!
   ;,a1wert;,a1wert;,a1wert     ;,a1wert;,a1wert;,a1we
 .asxzcvb.asxzcvb.asxzcvb.as   .asxzcvb.asxzcvb.asxzcvb.
1qaswedfqas1wedfqas1wedfqas1wedfqas1wedfqas1edfqas1ewdfqa
:lkjhgfdlkj:hgfdlkj:hgfdlkj:hgfdlkj:hgfdlkj:gfdhlkj:gfdhlk
3edcvfr4edc3vfr4edc3vfr4edc3vfr4edc3vfr4edc3fr4vedc3fr4ved
1234ewqa2341ewqa2341ewqa2341ewqa2341ewqa2341wqa2341weqa234
o[piuytr[piouytr[piouytr[piouytr[piouytr[pioytru[pioytru[p
z/xcvbnm/xczvbnm/xczvbnm/xczvbnm/xczvbnm/xczbnmv/xczbnmv/x
 `1qazxs`1qazxs`1wqazs`1wqazxs`1qazwxs1qa`zws1qa`zwsx1qa`
  mznxbcvfmznxbcvfmzxbcnvfzxbmcnfzxvbmnfzcxvbmnfzcxvbmnf
   %t^y&ujm%t^y&ujm%^y&tuj%^ym&tu%^yj&tum%^yj&tum%^yj&t
     )oiuytre)oiuytr)oieuyr)otieur)oyieutr)oyieutr)oyi
      z.xcvgy7z.xcvg7z.yxcg7zv.yxc7zv.ygxc7zv.ygxc7z
        q[wertyuq[weryuq[wertyuq[wetyurq[wetyurq[w
           a;sdfghja;sdfghja;sdfghja;sdfghja;sdf
              qmprootiqmprootimprootqimproot
                 mtu1qaz@mtu1qa@mtuz1qa@m
                    !qwe$rty!qwe$rty!q
                       -p=oiuyt-p=o
                           asdfg
                             l
>>> i.result(no=4)
         LoveLoveLov                eLoveLoveLo
     veLoveLoveLoveLove          LoveLoveLoveLoveLo
  veLoveLoveLoveLoveLoveL      oveLoveLoveLoveLoveLove
 LoveLoveLoveLoveLoveLoveL    oveLoveLoveLoveLoveLoveLo
veLoveLoveLoveLoveLoveLoveL  oveLoveLoveLoveLoveLoveLove
LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
 LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo
 veLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
   LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo
     veLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
       LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo
         veLoveLoveLoveLoveLoveLoveLoveLoveLove
           LoveLoveLoveLoveLoveLoveLoveLoveLo
             veLoveLoveLoveLoveLoveLoveLove
               LoveLoveLoveLoveLoveLoveLo
                  veLoveLoveLoveLoveLo
                      veLoveLoveLo
                           ve
 >>> i.result(no=6)
    ***     ***                   ***     ***                   ***     ***
  **   ** **   **               **   ** **   **               **   ** **   **
 *       *       *             *       *       *             *       *       *
 *               *             *               *             *               *
  *     LOVE    *               *     LOVE    *               *     LOVE    *
   **         **   ***     ***   **         **   ***     ***   **         **
     **     **   **   ** **   **   **     **   **   ** **   **   **     **
       ** **    *       *       *    ** **    *       *       *    ** **
         *      *               *      *      *               *      *
                 *     LOVE    *               *     LOVE    *
    ***     ***   **         **   ***     ***   **         **   ***     ***
  **   ** **   **   **     **   **   ** **   **   **     **   **   ** **   **
 *       *       *    ** **    *       *       *    ** **    *       *       *
 *               *      *      *               *      *      *               *
  *     LOVE    *               *     LOVE    *               *     LOVE    *
   **         **   ***     ***   **         **   ***     ***   **         **
     **     **   **   ** **   **   **     **   **   ** **   **   **     **
       ** **    *       *       *    ** **    *       *       *    ** **
         *      *               *      *      *               *      *
                 *     LOVE    *               *     LOVE    *
                  **         **                 **         **
                    **     **                     **     **
                      ** **                         ** **
                        *                             *

FRIENDSHIP
==========
>>>
 _________________##_________##
 _ ______________###*_______*###
 __________ _.*#####_________#####*.
 __________*######__________######*
 ________*#######____ _______#######*
 _______*########.______ ____.########*
 ______*#########.__________.#########*
 ______*######@###*_______* ###@######*
 _____*#########*###____###*#########*
 ____*##########*__*####*__*### #######*
 __*###########_____*_*______###########*
 _############_______________## ##########
 *##*#########____FRIENDS____#########*##*
 _____########______________ __########
 _______#######_____ _________#######
 ________*######________ ____######*
 _________*#####*__________*#####*
 ___________*####*________*####*
 _ ____________*####______####*
 ___________ ____*##*____*##*
 _________________*##__# #*
 __________________*####*
 ___________ ______.######.
 _______________.#########
             
SIBLINGS
======== 
>>>
        .===.
       / _/\ \
       \/6.6\/
       (  _  )         .===.
       _)---(_        / ,,, \
      /  `~`  \      ( /6.6\ )
     /\/     \/\     )(  _  )(
     \ |     | /    (_/;---;\_)
      \|_____|/      / `"*"` \
       |  L  |      ( (_.@._) )
       |__|__|      /'._\|/_.'\
        | | |      /. . . . . .\
        |_|_|      `"`"|"|"|"`"`
       _|_|_|_        _|_|_|_
      (___|___)      (___|___)

MARRIAGE
========
>>>
      /   \
    // / \_/
    \/* * )
     | <  |
     | _  |
      \__/
      |  |
   __/\  /\__
  /|| \||/ ||\     /|||\
 |  \\  .  // |  "/"|"|"|"
 |   \\ . //  | / ||* *|| \
 |    \\ //   |/ /|| ^ ||  \
 |  |  \ / |  |  /|| m |\   \
 |  |   |  |  |__\_/\_/\/____\
 |  |  o|o |  |     | |
 |  |   |  |  |    /...\
 |  |  o|o |  |  /~\___/~\
 |  |   |  |  | :         :
 |  |  o|o |  | : :     : :
 |  |   |  |  | : :     : :
 |__|  o|o |__| : : *@* : :
  \_:___|__|_/   \ *O*@% /
    |       |     \%0*YO/
    |       |     /*@O*%\
    |       |    : 0* *  :
    |   |   |    : * **  :
    |   |   |    : *  :  :
    |   |   |   /:       :\
    |   |   |  / :       : \
    |   |   | /  :       :  \
    |   |   |    :       :   \
    |   |   |    :       :    \
    |   |   |    :       :     \
    |   |   |    :       :      \
    |___|___|    :       :       \
    /   :   \    :       :        \
    \___:___/____:       :_________\
                 ~~~~~~~~~                 
\
                 ,    ,    .
               , ~@  `@ @~  `@  ,
             ~@ @ZXZ%%X&ZX%Z%XZ@`,
          ;@ %  @.~@,-.&&,-.@~ @ @H @~
          ,@X  ~  @(   )(   )@"  ~@X
          H  @     )   ()   (      ;@H@. ,
      `@X ,   `   '-=o=-'=o=-'         %@
   `@ %  @                            ,@ X@~
   ~ X@   "                            "  %  ,
  ;@H                      ,-.             H@.
    %@~            .,.    (/)_)          `@X
    H `          ,*@@@*.  d " b          ,@%@~
    %@~           &&&-b    \ /           ~@%
    X@.           && /: ,-/[x]\-.        ' X@
  ~@H              &!! /  \|M|/  \         H `
   'X@           /](  )[\ /|M|\~| |        X@:
    H           | ( ~~ ) !\| |/ | |      `@%
    H@.         `='8  [`=' |-|  | |      ~ H
  ,@X            \\(@*)//  |-|  |/         H@~
    %@~         / (*@@*) \_| |__|        `@X
    H `        /   (*@)   \ |  |         ,@%@~
    X@        /  ,~ ;: ~`  \|  |           H
  `@% '      /     :  ;     \  |         ~@% ,
    H       /~       ;       \ |           X@.
    X@.    /.,   ~@~    ~@~   \|           H
    H      /  '"*.,,*"'*,.,*'"\|         `@H
   @X@~   /                    \          X@
  ~ %@,  /                      \        ,@H ~
    H   /                        \         H
    H@.@~                       ~@\        %@,
  ,@X `'"*'*,  ~@~     ~@~  ,.*'"*"      ~@X
    H@~      '"*,.*"'"*.,*"'               H@.
    H><>gpyy<><><><><><><><><><><><><><><><H
\
          .::\)`:`,
       .:;\/~`\``;)                    ,.~-----,
       ;;==`_  ~:;(                ,,~{*}\~~--,.`.
      ;:==  6   6;;)             ,(((((({*});~~. .\
      ;;C      } )'             (('`)))~({*}) . \ .\
      :;`    `--';               >6  6`({*}))) . \~~
        |  `____/                ( {    ))())) . .`,
  ____._|      |_____.            `--' (((()))  .  |
 /    \  \__  _| |    \            `--  )))))) .  .|
|      )  \/\/\_{@}    |           ,-| (((((((  .  |
|       \_ \ \  | /    |          / | / )))))))   .|
|    |\   : \ |/ |  Y  |         (/*@@*( '   ` ) . |
\     \    \_\/_/   |  |         /  */  \ \'/ /.   |
 \     \     |o     |  |         \.  \   |'@'|    .|
  \     \    |      ; ,'--,.,.,.,  \     ~*@*~.  . |
   \     \_________._--`((,:{@}.:))_\    |~@~|  .  |
    \    '         |   ((,{@}:{@}.))-----'   ;/\   (,
     \._____________`-__((;,{@},:))_________/|{ | . ;
     |       |     |      `';{@},)   /`-----'\  |.  |
     |    .__/\__  |       `{@};,;  / / | \ \ \/   .|
     |   /   :;  \ |        `(@))\ /           \. . |
     |  /!   |    \|         ';; ))_/`-'/`_`.,  \.  |
     | | !   |     |          ';((   |   |  ! `_ \ .|
     | | !   |     |             ))  |   |  ! |.\_| |
     |/  !   |     |            (/   |   |  ! |  .  |
      |  !   |     |                 |   |  ! |~~~~'
      |  !   |     |                 |   |  ! |
      |  !   |     |                 |   |  ! |
      |  !  `|    `|                 |'  |' ! |
      |  !  -|    -|                 |`  |` ! |
      |  !   |     |                 |   |  ! |
      |  !   |     |                 |   |  ! |
      |  !   |     |                 |   |  ! |
      |  !   |     |                 |   |  ! |
      |  !   |     |                 |   |  ! |
      |  !   |     |                 |   |  ! |
      |  !   |     |                 |   |  ! |
      |  !   |     |                 ~~~~|~~~~~
      |======|=====|                 /__//__/|
       |     \___  \___            _/) _/)  _J
       L_--______)-____)          (___(____/ Y


