from diaries.DiarySample import DiarySample

from diaries.hanadaDiary import hanadaDiary

from diaries.DiarySasaki import DairySasaki

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    DairySasaki(),
  　hanadaDiary(),
] 


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
