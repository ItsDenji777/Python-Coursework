article= """
Markus Alexej Persson (/ˈpɪərsən/ ⓘ PEER-sən, Swedish: [ˈmǎrːkɵs ˈpæ̌ːʂɔn] ⓘ; born 1 June 1979), also known by the pseudonym Notch, is a Swedish video game programmer and designer. He is the creator of Minecraft, the best-selling video game in history.[a] He founded the video game development company Mojang Studios in 2009.

Persson began developing video games at an early age. His commercial success began after he published an early version of Minecraft in 2009. Prior to the game's official retail release in 2011, it had sold over four million copies. After this point Persson stood down as the lead designer and transferred his creative authority to Jens Bergensten. In September 2014, Persson announced his intention to leave Mojang, and in November of that year the company was sold to Microsoft reportedly for US$2.5 billion, which made him a billionaire.

Since 2016, several of Persson's posts on Twitter regarding feminism, race, and transgender rights have caused public controversies. He has been described as "an increasingly polarizing figure, tweeting offensive statements regarding race, the LGBTQ community, gender, and other topics". In an effort to distance itself from Persson, Microsoft removed mentions of his name from Minecraft (excluding one instance in the game's end credits) and did not invite him to the game's tenth anniversary celebration.[5] Persson co-founded a separate game studio called Rubberbrain in 2015, which was relaunched in 2024 as Bitshift Entertainment.
"""

article = article.replace("/ˈpɪərsən/", "")
article = article.replace("ⓘ", "")
article = article.replace("PEER-sən", "")
article = article.replace("[ˈmǎrːkɵs ˈpæ̌ːʂɔn]", "")
article = article.replace("Swedish:", "")

article = article.replace("[a]", "")

article = article.replace("[", "")
article = article.replace("]", "")
article = article.replace("(", "")
article = article.replace(")", "")

article = article.replace("0", "")
article = article.replace("1", "")
article = article.replace("2", "")
article = article.replace("3", "")
article = article.replace("4", "")
article = article.replace("5", "")
article = article.replace("6", "")
article = article.replace("7", "")
article = article.replace("8", "")
article = article.replace("9", "")

article = article.replace("/", "")
article = article.replace(";", "")
article = article.replace(":", "")
article = article.replace(",", "")
article = article.replace(".", "")
article = article.replace("!", "")
article = article.replace("?", "")
article = article.replace('"', "")
article = article.replace("'", "")
article = article.replace("-", "")
article = article.replace("$", "")

article = " ".join(article.split())

print(article)

words = article.split()
print("Word count:", len(words))

