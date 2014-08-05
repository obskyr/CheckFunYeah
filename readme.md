##CheckFunYeah

CheckFunYeah lets you know when people are playing [Kill Fun Yeah](http://killfunyeah.com/). Not many people are playing most of the time, so it can be nice to get notified whenever someone goes online.

This little program solves that! Keep it running in the background and it'll make a sound whenever people are playing, so you can just boot up the game and meet up with them. It'll even show which people are playing - you don't even have to start the game to check!

Want to keep idle in the lobby, but don't want CheckFunYeah to react to you? No problem! Just add yourself to the `ignore.txt` list and it'll ignore your presence.

##How to run

Before you do anything else, make sure you have [Python 2](https://www.python.org/downloads/) and [Pip](http://pip.readthedocs.org/en/latest/installing.html) (get the file called "get-pip.py") installed. Both of those are very important.

Once you have both of those, just run `CheckFunYeah.py` by double-clicking on it or lauching it via the command line. The first time you run it, it should install a few modules it needs. If it runs into trouble you might have to do it manually, but it should hopefully work without any problems. Once those are installed, it'll run as it normally would.

##Settings

There are a multitude of settings you can change, all in `settings.cfg`. Just open up the file with any text editor and you can change the parameters to the right. Here are the possible parameters:

* **Play sound:** True or False. If True, plays a sound when it notices people are playing.
* **Time between server checks (in seconds):** A number of seconds. How often CheckFunYeah checks for new players.
* **Notify on every check:** True or False. If CheckFunYeah should make a sound every time it checks and people are playing. Normally, it only makes a sound if no one was playing last time it checked. This parameter is overridden by `Play sound`.
* **Max number of players to show names of:** A number. When this many or less people are playing, CheckFunYeah shows you a player list. If more than that are playing, it only shows a number.

There is also `ignored.txt`. In this file, write all the players you want CheckFunYeah to ignore. It's recommended that you put yourself in there - otherwise CheckFunYeah will notify you when *you* are playing. If only ignored people are playing, you will not be notified.

##Talk to me!
Have any questions? Any feedback? Maybe you just want to talk? Hit me up on [Twitter](http://twitter.com/obskyr/), via [e-mail](mailto:powpowd@gmail.com) or on the Kill Fun Yeah forum post about CheckFunYeah. Twitter is your best bet!
